import json
import requests
import xmltodict
import abc

from netmiko import ConnectHandler

requests.packages.urllib3.disable_warnings()

#### MAIN CLASSES ####

class webservice_client():
    def __init__(self, uri="",username="",password="",header=""):
        self.uri = uri
        self.username = username
        self.password = password
        self.header = header

    def call_request_post(self, data):
        return requests.post(self.uri, data, self.header, verify = False, auth=(self.username,self.password))       

class ssh_client():
    def __init__(self, ip_address="",username="",password="",device_type=""):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.device_type = device_type

    def run_cmd(self,cmd_list,debug=False):
        connection = ConnectHandler(device_type=self.device_type, ip=self.ip_address, username=self.username, password=self.password)
        connection.enable()
        output = connection.send_config_set(cmd_list)
        connection.disconnect()
        return output

#### CHILD CLASSES ####

# IOS_CLI #
class ioscli(ssh_client):
    def __init__(self, jobparams, object):
        super().__init__(jobparams.get("ip_address",""), jobparams.get("username",""),jobparams.get("password",""),jobparams.get("device_type",""))
        self.process = object
        
    def execute(self, debug=False):
        data = self.process.get_data() 
        if debug:
           print("\n\n>>>>>>>>> SENT >>>>>>>>> ")
           print(data)
        data = eval(data['cmd_list'])
        r = super().run_cmd(data, debug)            
        if debug:
           print("\n<<<<<<<<< RECEIVED <<<<<<<<< ")
           print(r)     
        return r

# REST_JSON #
class restjson(webservice_client):

    def __init__(self, jobparams, object):
        super().__init__(jobparams.get("uri",""))
        self.process = object

    def __format_message__(self):
        data_dict = self.process.get_data()
        for i in data_dict:
            data_dict[i] = json.dumps(data_dict.get(i))
        return data_dict

    def execute(self, debug=False):
        data = self.__format_message__()
        if debug:
           print("\n\n>>>>>>>>> SENT >>>>>>>>> ")
           print(data)
        r = super().call_request_post(data)            
        if r:
            res = r.json()
        else:
            res = {}
        if debug:
           print("\n<<<<<<<<< RECEIVED <<<<<<<<< ")
           print(r.content)
        return res

# SOAP_AXL #
class soapaxl(webservice_client):

    def __init__(self, jobparams, object):
        super().__init__(jobparams.get("uri",""), jobparams.get("username",""), jobparams.get("password",""), "{'Content-type':'text/xml', 'SOAPAction':'CUCM:DB ver=%s %s'}"%(jobparams.get("version",""), jobparams.get("action","")))
        self.process = object
        self.jobdata = jobparams

    def __format_message__(self):
        json_string = json.dumps(self.process.get_data())
        print(json_string)
        json_string = json_string.replace("___",'')
        xml_string = xmltodict.unparse(json.loads(json_string), pretty=False)
        xml_string = xml_string.replace('<?xml version="1.0" encoding="utf-8"?>','')
        xml_header = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/%s"><soapenv:Header/><soapenv:Body><ns:%s>%s</ns:%s></soapenv:Body></soapenv:Envelope>' % (self.jobdata.get("version"), self.jobdata.get("action"), xml_string, self.jobdata.get("action"))              
        return xml_header

    def execute(self, debug=False):
        data = self.__format_message__()
        if debug:
            print("\n\n>>>>>>>>> SENT >>>>>>>>> ")
            print(data)
        r = super().call_request_post(data)            
        res = r.content
        if debug:
           print("\n<<<<<<<<< RECEIVED <<<<<<<<< ")            
           print(res)
        return res
