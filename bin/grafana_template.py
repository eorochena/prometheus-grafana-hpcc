#!/usr/bin/env python3

import gethpcc
import os

name = gethpcc.environment_name()
json_file = name + '.json'
file_location = os.path.abspath("../json_files/" + json_file)
new_json =open(file_location, 'w+')
template_name = 'cluster-template'

with open('../grafana-template.json', 'r+') as template:
    for line in template:
        if line.find('cluster-template') >= 0:
            new_line = line.replace('cluster-template', name).replace('\n', '')
            new_json.write(new_line)
        else:
            new_json.write(line)
new_json.close()