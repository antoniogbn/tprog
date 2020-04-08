import json

class process():

    def __init__(self, object, task_data):
        self.task_data = task_data
        self.task     = object
        self._json_edges = []

    def __parse_json(self, treedict, parent=""):

        for i in treedict:

            name = i

            if parent is not "":
                self._json_edges.append((parent,name))
            value = treedict.get(name)

            if isinstance(value, list):                   
                self._json_edges.append((parent,name))

            if isinstance(value, dict):
               self.__parse_json(value, parent=name)

    def load_data(self):

        self.__parse_json(self.task_data)

        attr_line = {}
        exclude = []

        for row in self._json_edges:

            parent = attr_line.get(row[0],"")

            if (parent is not "") :
                if (row[0] not in exclude):                   
                    exclude.append(row[0]) 
                line = parent + '.{0}___'.format(row[1])    
            else:
                children = ''
                for z in row:
                    if z is not "":
                        children += '.{0}___'.format(z)
                line = parent + children 

            attr_line[row[1]] = line

        for i in exclude:
            del attr_line[i]

        for i in attr_line:
            temp_str = attr_line[i].split('.')
            del temp_str[0]
            yaml_str = ""
            for j in temp_str:
                z = j.replace("___","")
                yaml_str += "['%s']" % (z)
            exec_line = 'self.task' + attr_line[i] + ' =  self.task_data' + yaml_str + ''     
            #print(exec_line)
            exec(exec_line) 

    def get_data(self):
        data = json.dumps(self.task.get())
        data = json.loads(data.replace("___",""))
        return data 
