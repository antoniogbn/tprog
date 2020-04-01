##################################################################
##################################################################

##external libs
import json
import yaml
import sys
import csv
import ruamel.yaml
import time
import os

##internal libs
import interface
from task import task 
from process import process

##Var initilization
start_time = time.time()
DEBUG = True
global_vars = {}

if len(sys.argv) != 2:
    print('ERROR : Please provide YAML file name')
    sys.exit(1)
else:
    service_file = sys.argv[1]

if not os.path.exists(service_file):
    print('ERROR : YAML file not found')
    sys.exit(1)

yaml = ruamel.yaml.YAML(typ='safe')

with open(service_file) as f:

    service_data = yaml.load(f)

    for task_key in service_data:

        my_task = task(service_data.get(task_key))

        ## Reading YAML parameters
        task_type   = my_task.data.get('type','')
        task_action = my_task.data.get('action','')
        task_return = my_task.data.get('return','')
        task_data   = my_task.data.get('data','')
        task_csv    = my_task.data.get('csv','')
        
        task_data_list = []
        
        ## Loading tasks
        if task_csv is not "": ## If csv file is present on YAML file

            task_data_csv = ""

            with open(task_csv) as f:

                csv_reader = csv.reader(f)
               
                csv_line_count = 0
                csv_header = []
                csv_line   = []

                for row in csv_reader:
                    
                    read_line = ''.join(row).strip()
                    
                    if read_line == "" or read_line.startswith('#'):
                        continue

                    if csv_line_count == 0:
                        csv_header = row
                    else:
                        csv_line = row
                        task_data_csv = json.dumps(task_data)

                        ##replace with csv columns values
                        for i in range(len(csv_header)) :
                            task_data_csv =  task_data_csv.replace('_' + csv_header[i].strip(), csv_line[i])

                        ##replace global_var on job string 
                        for var in global_vars :
                            task_data_csv = json.loads(task_data_csv.replace('$'+var, str(global_vars.get(var,''))))

                        task_data_list.append(eval(task_data_csv))

                    csv_line_count += 1
        else:
            task_data_list.append(task_data)

        #DEBUG POINT
        for row in task_data_list:
            print(row)
        #continue

        #Action Model Object Importing
        exec_line = 'import %s' % (task_action)
        exec(exec_line)
             
        exec_line = 'my_yang_object = %s.%s()' % (task_action, task_action)
        exec(exec_line)
        
        my_process = process(my_yang_object, task_data)

        exec_line = 'my_equipment = interface.%s(my_task.data, my_process)' % (task_type)
        exec(exec_line)    

        if task_return is not "" and task_return not in global_vars.keys():    
            global_vars[task_return] = []

        for task_data_line in task_data_list:

            my_process.task_data = task_data_line
            my_process.load_data()

            task_returned = my_equipment.execute(DEBUG)  
          
            if task_return is not "":    
                global_vars[task_return] = task_returned.get(task_return,'')


#print(global_vars)
print("--- %2.5f seconds ---" % (time.time() - start_time))