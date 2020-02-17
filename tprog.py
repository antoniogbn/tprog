#external libs
import json
import yaml
import sys
import csv
import ruamel.yaml
import time

start_time = time.time()

#internal libs
import equipment
from process import process

global_vars = {}
#var_return = ""

#service_file = 'addPhone.yaml'
#service_file = 'encana_setup.yaml'
#service_file = 'update_accounts.yaml'
#service_file = 'new_setup_cucm.yaml'
service_file = 'add_accounts.yaml'
#service_file = 'get_account_info.yaml'
#service_file = 'set_inbound_vg.yaml'
#service_file = 'new_setup.yaml'
#service_file = 'lab_setup.yaml'
#service_file = 'cucm_lab_setup.yaml'
#service_file = 'set_remote_sw.yaml'
#service_file = 'set_remote_rt.yaml'
#service_file = 'gearbulk.yaml'

yaml = ruamel.yaml.YAML(typ='safe')

with open(service_file) as f:
    service_data = yaml.load(f)
    for task in service_data:
        job_params = service_data.get(task)
        job_type   = job_params.get('type','')
        job_action = job_params.get('action','')
        job_return = job_params.get('return','')
        job_data   = job_params.get('data','')
        job_csv    = job_params.get('csv','')

        job_data_list = []
        if job_csv is not "":
            job_data_csv = ""
            with open(job_csv) as f:
                csv_reader = csv.reader(f)
                csv_line_count = 0
                csv_header = []
                csv_line = []
                for row in csv_reader:
                    if csv_line_count == 0:
                        csv_header = row
                    else:
                        csv_line = row
                        job_data_csv =  json.dumps(job_data)
                        for i in range(len(csv_header)):
                            job_data_csv =  job_data_csv.replace('_' + csv_header[i], csv_line[i])
                        # replace global_var on job string 
                        for var in global_vars:
                            job_data_csv = job_data_csv.replace('$'+var, str(global_vars.get(var,'')))
                        job_data_list.append(eval(job_data_csv))
                    csv_line_count += 1
        else:
            job_data_list.append(job_data)

        exec_line = 'import %s' % (job_action)
        exec(exec_line)
        
        exec_line = 'my_job = %s.%s()' % (job_action, job_action)
        exec(exec_line)
        
        my_process = process(my_job)
        exec_line = 'my_equipment = equipment.%s(job_params, my_process)' % (job_type)
        exec(exec_line)    

        if job_return is not "" and job_return not in global_vars.keys():    
            global_vars[job_return] = []

        for job_data_line in job_data_list:

            my_process.jobdata = job_data_line
            my_process.load_data()
            job_res = my_equipment.execute(True)        

            if job_return is not "":    
                global_vars[job_return] = job_res.get(job_return,'')
                '''for k, v in job_res.items():
                    for k1, v1 in v.items():
                        if k1 == job_return:
                           var_return += ' %s'%(v1)
                           #global_vars[job_return].append(v1)'''

#print(var_return)
print("--- %2.5f seconds ---" % (time.time() - start_time))