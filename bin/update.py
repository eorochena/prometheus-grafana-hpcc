#!/usr/bin/env python3

import gethpcc
import append_to_yml
import grafana_template

server_list = gethpcc.XMLParser()
job_name = gethpcc.environment_name()
roxie_cluster = server_list.Roxie()
thor_cluster = server_list.ThorSlave()

for thor in append_to_yml.prometheus_yml_thor(job_name, thor_cluster):
    dashboard_name = job_name + ' ' + thor
    grafana_template.grafana_json(dashboard_name)
for roxie in append_to_yml.prometheus_yml_roxie(job_name, roxie_cluster):
    dashboard_name = job_name + ' ' + roxie
    grafana_template.grafana_json(dashboard_name)

