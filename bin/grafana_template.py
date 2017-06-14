#!/usr/bin/env python

from __future__ import print_function

import getenv
import fileinput

name = getenv.environment_name()

with fileinput.FileInput('../grafana-template.json', inplace=True, backup='.backup') as template:
    for line in template:
        if 'cluster-template' in line:
            print(line.replace('cluster-template', name), end='')
        else:
            print(line, end='')