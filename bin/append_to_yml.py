#!/usr/bin/env python3

import getenv

server_list = getenv.XMLParser()
targets = []

for i in server_list.IPs():
    targets.append(i+':9100')

new_environment = """
  - job_name: '%s'

    static_configs:
     - targets: %s""" % (getenv.environment_name(), targets)

with open('../prometheus.yml', 'a+') as prometheus_file:
    prometheus_file.write(new_environment)
