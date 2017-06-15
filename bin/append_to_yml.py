#!/usr/bin/env python3

import gethpcc

server_list = gethpcc.XMLParser()
job_name = gethpcc.environment_name()
roxie_cluster = server_list.Roxie()
thor_cluster = server_list.ThorSlave()

if thor_cluster:
    for cluster_name in thor_cluster:
        targets = []
        for server in thor_cluster[cluster_name]:
            targets.append(server+':9100')
        new_environment = """\n
  - job_name: '%s'

    static_configs:
     - targets: %s""" % (job_name + ' ' + cluster_name, targets)
        with open('../prometheus.yml', 'a+') as prometheus_file:
            prometheus_file.write(new_environment)

if roxie_cluster:
    for cluster_name in roxie_cluster:
        targets = []
        for server in roxie_cluster[cluster_name]:
            targets.append(server + ':9100')
        new_environment = """\n
     - job_name: '%s'

       static_configs:
        - targets: %s""" % (job_name + ' ' + cluster_name, targets)
        with open('../prometheus.yml', 'a+') as prometheus_file:
            prometheus_file.write(new_environment)
