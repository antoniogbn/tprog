import json
import requests
import xmltodict
from abc import ABC, abstractmethod

from netmiko import ConnectHandler

requests.packages.urllib3.disable_warnings()





#### ABSTRACT CLASS ####

class interface(ABC):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    @abstractmethod
    def execute(self):
        pass

#### MAIN CLASSES ####

class webservice_client(interface):

    def __init__(self, username, password, uri, header):
       self.uri = uri
       self.header = header
       super().__init__(username, password)

    def call_request_post(self, data):
        r = requests.post(self.uri, data, self.header, verify = False, auth=(self.username,self.password)) 
        return r

    def execute(self, data, debug=False):
        if debug:
            print('\n\nSENT >>>')
            print(data)      
        r = self.call_request_post(data)
        if debug:
            print('\n\nRECEIVED >>>')
            print(r.json())
        return r.json()
   
class ssh_client(interface):

    def __init__(self, username, password, ip_address):
        self.ip_address  = ip_address
        super().__init__(username, password)        

    def send_cmd(self, cmd_list, device_type):
        connection = ConnectHandler(device_type=device_type, ip=self.ip_address, username=self.username, password=self.password)
        connection.enable()
        r = connection.send_config_set(cmd_list)
        connection.disconnect()
        return r

    def execute(self, cmd_list, device_type):
        r = send_cmd(self, cmd_list, device_type)
        return r


#### CHILD CLASSES ####

# CLI IOS #
class cliios(ssh_client):

    def __init__(self, task_p, object):
        device_type = task_p.get("device_type")
        super().__init__(task_p.get("username",""), task_p.get("password",""), task_p.get("device_type",""), task_p.get("ip_address",""))
        self.process = object
        
    def execute(self):
        data = self.process.get_data() 
        super().execute(data, self.device_type)
        return True

# REST_JSON #
class restjson(webservice_client):

    def __init__(self, task_p, object):
        super().__init__(task_p.get("username",""), task_p.get("password",""), task_p.get("uri",""),"")
        self.process = object

    def __format_message__(self):
        data_dict = self.process.get_data()
        for i in data_dict:
            data_dict[i] = json.dumps(data_dict.get(i))
        return data_dict

    def execute(self, debug=False):
        data = self.__format_message__()
        r = super().execute(data, debug)            
        return r 

# SOAP_AXL #
class soapaxl(webservice_client):

    def __init__(self, task_p, object):
        self.header = "{'Content-type':'text/xml', 'SOAPAction':'CUCM:DB ver=%s %s'}" % (task_p.get("version",""))
        super().__init__(task_p.get("username",""), task_p.get("password",""), task_p.get("uri",""),self.header)
        self.process = object
        self.task_p = task_p

    def __format_message__(self):
        json_string = json.dumps(self.process.get_data())
        print(json_string)
        json_string = json_string.replace("___",'')
        xml_string = xmltodict.unparse(json.loads(json_string), pretty=False)
        xml_string = xml_string.replace('<?xml version="1.0" encoding="utf-8"?>','')
        xml_header = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/%s"><soapenv:Header/><soapenv:Body><ns:%s>%s</ns:%s></soapenv:Body></soapenv:Envelope>' % (self.task_p.get("version"), self.task_p.get("action"), xml_string, self.task_p.get("action"))              
        return xml_header

    def execute(self, debug=False):
        data = self.__format_message__()
        r = super().execute(data,debug)            
        res = r.content
        return res
