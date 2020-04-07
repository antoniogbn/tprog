# TPROG - Telecomunications programming tool

TPROG is a tool developed using the Python scripting language for automation of telecommunications processes on heterogenous enviroments. 
It uses equipment´s interfaces to interact with them in order to acomplish configuration tasks, the currently version supports the follow integration technologies :

* [REST](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
* [SOAP](https://www.w3.org/TR/soap/) 
* [SSH](https://tools.ietf.org/html/rfc4253)


## Requirements

### Python
```
Python 3.6.8 or higher
```

### Libraries
```
bcrypt==3.1.7
bitarray==1.0.1
certifi==2019.9.11
cffi==1.13.2
chardet==3.0.4
cryptography==2.8
enum34==1.1.6
future==0.18.2
idna==2.8
lxml==4.4.1
netmiko==2.4.2
paramiko==2.6.0
pyang==2.1
pyangbind==0.8.1
pybind11==2.4.3
pycparser==2.19
PyNaCl==1.3.0
pyserial==3.4
PyYAML==5.1.2
regex==2019.8.19
requests==2.22.0
ruamel.yaml==0.16.5
ruamel.yaml.clib==0.2.0
scp==0.13.2
siesta==0.5.1
simplejson==3.16.0
six==1.12.0
textfsm==1.1.0
urllib3==1.25.6
xmltodict==0.12.0
```

## Install

1. **Clone the project to a folder on your system :**
```
git clone https://github.com/antoniogbn/tprog.git
```

2. **Install required libraries :**
```
pip install -r requirements.txt
```

## Howto

The steps below will guide how to use the TPROG 

1. **Create tha YANG model file :**

The YANG model must be based on equipment API format honouring the data hiehierarchy, once that´s created the [Pyang](https://github.com/mbj4668/pyang) is used to convert the model into python objects that will be later used on TPROG workflow.
 
The data modeled on the YANG file will refer strictly to that  data that will be applied on equipment using the follow YANG structure as reference :

```
module [modulename] {

    yang-version "1";

    namespace "https://[yournamespaceurl]/";

    prefix "[]";

    typedef data {
        type string;
    }
    
    container [containername]___{
        leaf [fieldname1]___ {
            type data;
        }
        leaf [fieldname2]___ {
            type data;
        }
        .
        .
        .
        leaf [fieldname3]___ {
            type data;
        }

    }
```

**Notes** : *- The module information inside of YANG model must be the same as the YANG file name also* 
           

2. **Generate the python object from YANG model**

Once the YANG file is created,  command line below should be used to generate the python object class that later will ve used on TPROG workflow :

```
python tprog.cyang.py [yangfilename]
```



3. **Prepare the YAML file with tasks data :**

The YAML file should have the tasks that will be performed when the TPROG is executed, it can contain one more multiple tasks entries that must follow the YAML format rules. The YAML file is read using library [Ruamel](https://pypi.org/project/ruamel.yaml/)

The service task file should have the below presented structure :

```
task1:
    type : 
    action : 
    csv : 
    uri : 
    username : 
    password : 
    version : 
    data :
    .
    .
    .

task2:
    type : 
    action : 
    csv : 
    uri : 
    username : 
    password : 
    version : 
    data :
    .
    .
    .
```
In the table below is showed the tags supported on YAML file also their description and if it´s mandatory accordinly with access technologies 


| Tag        | Description                                                                       | REST | SOAP | SSH |
|------------| ----------------------------------------------------------------------------------|------|------|-----|
|task        | Unique task idenfier                                                              |  Y   |  Y   |  Y  | 
|type        | Equipment access method type. currently supported  : restjson, soapaxl e ioscli   |  Y   |  Y   |  Y  | 
|action      | Action to be called during the process, must match with object class (YANG Model) |  Y   |  Y   |  Y  | 
|uri         | Logical address for webservices protocols                                         |  Y   |  Y   |  N  |   
|ip_address  | Logical address for IP protocols                                                  |  N   |  N   |  Y  | 
|version     | Equipment version                                                                 |  N   |  Y   |  N  |                                     
|device_type | Equipment type                                                                    |  N   |  N   |  Y  |                                        
|username    | Username access                                                                   |  N   |  Y   |  Y  |                                            
|password    | Password access                                                                   |  N   |  Y   |  Y  |                                               
|csv         | CSV sub-file for batch execution                                                  |  N   |  N   |  N  |          
|data        | Data that will submited in the equipment                                          |  Y   |  Y   |  Y  |                            
|return      | Task return variable                                                              |  N   |  N   |  N  | 


4. **Run TPROG in order to get tasks completed :**


```
python tprog.py tasks.yaml
```


## About

The TPROG tool is the result of a MSc study currently in course with [Universidade Federal Fluminense](http://mesc.sites.uff.br/)

Authors :

Antonio Garcia Brandão Neto - antoniogbn@id.uff.br (mastering)

Carlos Bazilio - carlosbazilio@id.uff.br (advisor)
