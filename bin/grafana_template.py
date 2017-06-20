#!/usr/bin/env python3

import os
import requests
import json

def grafana_json(dashboard_name):
    json_file = dashboard_name.replace(' ', '_') + '.json'
    file_location = os.path.abspath("../json_files/" + json_file)
    new_json =open(file_location, 'w+')
    template_name = 'cluster-template'
    admin_user = 'admin'
    admin_password = 'lamepassword'

    with open('../grafana-template.json', 'r+') as template:
        for line in template:
            if line.find(template_name) >= 0:
                new_line = line.replace(template_name, dashboard_name).replace('\n', '')
                new_json.write(new_line)
            else:
                new_json.write(line)
    new_json.close()

    with open(file_location) as data_file:
        payload = json.load(data_file)
    headers = {"Content-Type":"application/json", 'Accept': 'application/json'}
    r = requests.post('http://10.239.227.60:3000/api/dashboards/db',
                  data=json.dumps(payload), auth=(admin_user, admin_password))
    return r.json()
