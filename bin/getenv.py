#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import paramiko
import getpass

xml_remote = '/etc/HPCCSystems/environment.xml'
xml_local = '/tmp/environment.xml'
user = 'root'

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
    host.connect(username=user, password=authentication())
    sftp = paramiko.SFTPClient.from_transport(host)
    sftp.get(xml_remote, xml_local)
    return xml_local

class XMLParser:
    def __init__(self):
        self.parsing = self

    def IPs(self):
        parsexml = ET.parse(getxml())
        doc_root = parsexml.getroot()
        ip_addresses = []
        for i in doc_root.findall('.//DafilesrvProcess/Instance'):
            ip = i.attrib['netAddress']
            ip_addresses.append(ip)
        return ip_addresses
