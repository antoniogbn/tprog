# TPROG 

TPROG is a tool developed using the Python scripting language for automation of telecommunications processes on heterogenous enviroments. 
It uses equipment´s interfaces to interact with them in order to acomplish configuration tasks, the currently version supports the follow integration technologies :

* [REST](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
* [SOAP](https://www.w3.org/TR/soap/) 
* [SSH](https://tools.ietf.org/html/rfc4253)


## Requirements :

### Python :
```
Python 3.6.8 or higher
```

### Libraries :
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
           

2. **Generate the python object from YANG model :**

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

In the table below is listed the tags that are supported on YAML file also their description and mandatory rule accordinly with access technologies. 


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

## Examples :

1. **Using TPROG with REST API :**

This example shows how to use TPROG to add customer and accounts information using REST API in a [PortaOne Softswitch](https://www.portaone.com/products/portaswitch) server.

The both YANG files were created to serve as model to both API methods that will be called based on service API sctructure :

- [add_customer](https://github.com/antoniogbn/tprog/blob/master/mdl/add_customer.yang)
- [add_accounts](https://github.com/antoniogbn/tprog/blob/master/mdl/add_account.yang)

Then the object classes were created from their respectively YANG models using the follow commands:

```
(tprog) user@localhost:/dev/tprog$ python tprog.cyang.py add_customer
pyang -f tree mdl/add_customer.yang
module: add_customer
  +--rw auth_info___
  |  +--rw login___?      data
  |  +--rw password___?   data
  +--rw params___
     +--rw customer_info___
        +--rw name___?                data
        +--rw iso_4217___?            data
        +--rw i_traffic_profile___?   data
        +--rw email___?               data
pyang --plugindir $PYBINDPLUGIN -f pybind mdl/add_customer.yang > obj/add_customer.py

(tprog) user@localhost:/dev/tprog$ python tprog.cyang.py add_customer
pyang -f tree mdl/add_customer.yang
module: add_customer
  +--rw auth_info___
  |  +--rw login___?      data
  |  +--rw password___?   data
  +--rw params___
     +--rw customer_info___
        +--rw name___?                data
        +--rw iso_4217___?            data
        +--rw i_traffic_profile___?   data
        +--rw email___?               data
pyang --plugindir $PYBINDPLUGIN -f pybind mdl/add_customer.yang > obj/add_customer.py

```

And the object classes files were generated inside **obj** folder, then once that is completed, the next step will be to create the task YAML file, the example below shows the file with 2 tasks :

```
---
task1:
    type : restjson
    action : add_customer
    uri : https://apiserver/rest/Customer/add_customer
    data :
        auth_info :
            login : "username"
            password : "password" 
        params :
            customer_info:
                name : "Telecom International"
                iso_4217 : "USD"
    return : i_customer
  
task2:
    type : restjson
    action : add_account
    uri : https://apiserver/rest/Account/add_account
    data :
        auth_info :
            login : "username"
            password : "password" 
        params :
            account_info:
                id: 552137525665
                billing_model: 1
                i_product: 1676                 
                i_customer: $i_customer         
                h323_password: 123456           
                batch_name: telecomint_accounts 
```

The task1 will call the method **add_customer** to add customer information on the server and the task2 will call the method **add_account** to add the accounts posteriorly . The entry **return** present on the task1 refers to the variable returned from method called with customer key that was generated during the process and will avaiable on the task2 be used adding accounts for that recently added customer.

Once YAML is complete call tprog main script to execute the tasks file with below line :

```
python tprog.py demo1.yaml
```

The obteined output should be like presented below :

```
SENT >>>
{'auth_info': '{"login": "UsernameDemo", "password": "PasswordDemo"}', 'params': '{"customer_info": {"name": "Telecom International", "iso_4217": "USD", "i_traffic_profile": "", "email": ""}}'}


RECEIVED >>>
{'i_customer': 6736}


SENT >>>
{'auth_info': '{"login": "UsernameDemo", "password": "PasswordDemo"}', 'params': '{"account_info": {"id": "552137525665", "billing_model": "1", "i_product": "1676", "i_customer": "6736", "h323_password": "abc12356", "batch_name": "telecomint_accounts"}}'}


RECEIVED >>>
{'i_account': 570170}

--- 3.52347 seconds ---
```


2. **Using TPROG with SOAP API :**

This example shows how to use TPROG to add Phones and Numbers  information using SOAP AXL API in a [Cisco CUCM](https://www.cisco.com/c/en/us/products/unified-communications/unified-communications-manager-callmanager/index.html) server.

...


3. **Using TPROG with SSH :**

This example shows how to use TPROG to add dial-peer configuration using SSH command line instructions to a [Cisco Voice Gateway](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/srnd/design/guide/cmesrnd/gatewy.html) .

...

## About :

The TPROG tool is the result of a MSc. study currently in course with [Universidade Federal Fluminense](http://mesc.sites.uff.br/)

Authors :

Antonio Garcia Brandão Neto - antoniogbn@id.uff.br (mastering)

Carlos Bazilio - carlosbazilio@id.uff.br (advisor)
