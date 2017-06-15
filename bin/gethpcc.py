#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import paramiko
import getpass

xml_remote = '/etc/HPCCSystems/environment.xml'
xml_local = '/tmp/environment.xml'

def username():
    user = input('Enter username > ')
    return user

def ip_address():
    address = input('Enter IP of remote environment > ')
    return address

def authentication():
    xxx = getpass.getpass()
    return xxx

def environment_name():
    env_name = input('Enter environment name > ')
    return env_name

def getxml():
    host = paramiko.Transport((ip_address(), 22))
    host.connect(username=username(), password=authentication())
    sftp = paramiko.SFTPClient.from_transport(host)
    sftp.get(xml_remote, xml_local)
    return xml_local

class XMLParser:
    def __init__(self):
        self.parsing = self

    getxml()

    def IPs(self):
        parsexml = ET.parse(xml_local)
        doc_root = parsexml.getroot()
        ip_addresses = []
        for i in doc_root.findall('.//DafilesrvProcess/Instance'):
            ip = i.attrib['netAddress']
            ip_addresses.append(ip)
        return ip_addresses

    def dali(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        for i in doc_root.findall('.//DaliServerProcess/Instance'):
            DaliIP = i.attrib['netAddress']
        return DaliIP

    def eclccservers(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        eclservers = []
        for i in doc_root.findall('.//EclCCServerProcess/Instance'):
            ECLIP = i.attrib['netAddress']
            eclservers.append(ECLIP)
        return eclservers

    def eclservers(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        eclservers = []
        for i in doc_root.findall('.//EclServerProcess/Instance'):
            ECLIP = i.attrib['netAddress']
            eclservers.append(ECLIP)
        return eclservers

    def eclagent(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        agents = []
        for i in doc_root.findall('.//EclAgentProcess/Instance'):
            AgentIP = i.attrib['netAddress']
            agents.append(AgentIP)
        return agents

    def dfuserver(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        dfuserver = []
        for i in doc_root.findall('.//DfuServerProcess/Instance'):
            DfuServer = i.attrib['netAddress']
            dfuserver.append(DfuServer)
        return dfuserver


    def ESP(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        ESP = []
        for i in doc_root.findall('.//EspProcess/Instance'):
            EspServer = i.attrib['netAddress']
            ESP.append(EspServer)
        return ESP


    def EclScheduler(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        eclscheduler = []
        for i in doc_root.findall('.//EclSchedulerProcess/Instance'):
            scheduler = i.attrib['netAddress']
            eclscheduler.append(scheduler)
        return eclscheduler

    def Roxie(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        RoxieCluster = {}
        for i in doc_root.findall('.//RoxieCluster'):
            try:
                roxie_attributes = i.attrib
                for i in roxie_attributes:
                    if i == 'name':
                        roxie_name = roxie_attributes[i]
                print(roxie_name)
                sisters = []
                for roxie_server in doc_root.findall(".//*[@name='%s']/RoxieServerProcess" % roxie_name):
                    bad_name = roxie_server.attrib['computer']
                    for hardware in doc_root.findall(".//Hardware/Computer"):
                        if bad_name == hardware.attrib['name']:
                            sisters.append(hardware.attrib['netAddress'])
                RoxieCluster[roxie_name] = sisters
            except:
                # Me no care
                pass
        return RoxieCluster

    def sasha(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        for i in doc_root.findall('.//SashaServerProcess/Instance'):
            Sasha = i.attrib['netAddress']
        return Sasha


    def ThorMaster(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        Thors = []
        for i in doc_root.findall('.//ThorMasterProcess'):
            Thor = i.attrib['computer']
            Thors.append(Thor)
        d = {}
        for i in doc_root.findall('.//Hardware/Computer'):
            Machine = i.attrib['name']
            IP = i.attrib['netAddress']
            d[Machine] = IP
        ThorMasters = []
        for i in d:
            if i not in Thors:
                continue
            elif i in Thors:
                ThorMasters.append(d[i])
        return ThorMasters


    def ThorSlave(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        ThorCluster = {}
        for i in doc_root.findall('.//ThorCluster'):
            try:
                Master = i.attrib['name']
                Slaves = []
                for i in doc_root.findall(".//*[@name='%s']/ThorSlaveProcess" % Master):
                    bad_name = i.attrib['computer']
                    for i in doc_root.findall(".//Hardware/Computer"):
                        if bad_name == i.attrib['name']:
                            Slaves.append(i.attrib['netAddress'])
                ThorCluster[Master] = Slaves
            except:
                # Because I don't give a fuck
                pass
        return ThorCluster

print(XMLParser().Roxie())
print(XMLParser().ThorSlave())