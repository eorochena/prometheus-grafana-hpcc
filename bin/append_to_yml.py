#!/usr/bin/env python3

def prometheus_yml_thor(job_name, thor_cluster):
    if thor_cluster:
        # dealing with multiple clusters sharing same hardware
        unique_values = []
        keys_with_duplicate_values = []
        for key, value in thor_cluster.items():
            if value not in unique_values:
                unique_values.append(value)
            elif value in unique_values:
                keys_with_duplicate_values.append(key)
        for deletion in keys_with_duplicate_values:
            del thor_cluster[deletion]
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
    return thor_cluster

def prometheus_yml_roxie(job_name, roxie_cluster):
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
    return roxie_cluster