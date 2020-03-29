# TPROG - Telecomunications programming tool

TPROG is a tool developed using the Python scripting language for automation of telecommunications processes on heterogenous enviroments. 
It uses equipment´s management interfaces to interact with them, the currently versions supports follow integration technologies :

* RESTful
* SOAP
* Terminal access


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

1. Clone the project to a folder on your system :
```
git clone https://github.com/antoniogbn/tprog.git
```

2. Install required libraries :
```
pip install -r requirements.txt
```

## Howto

1. Create YANG model file :


2. Prepare de YAML file with tasks data :


3. Run TPROG in order to get tasks completed :

```
python tprog.py cisco_vg.yaml
```




