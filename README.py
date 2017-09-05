#!/usr/bin/python

with open('README.md', 'w') as README:
    with open('docs/list_of__modules.rst', 'r') as index:

        README.write('''
# Cisco ACI modules for Ansible

This project is working on upstreaming Cisco ACI support within the Ansible project.
We currently have 30+ modules available, and many more are being added.


## News
Ansible v2.4 will ship with **aci_rest** and tens of ACI modules ! We are working hard
with the Ansible Network Working Group to add more modules to ship with Ansible v2.5.

You can find more information related to this project at:
https://github.com/ansible/community/wiki/Network:-ACI

People interested in contributing to this project are welcome to join.


## Modules

''')

        for line in index.readlines():
            items = line.split()
            if not items:
                continue
            module = items[0]
            if module.startswith('aci_'):
                description = ' '.join(items[2:-1])
                README.write('- [%(mod)s](https://github.com/datacenter/aci-ansible/blob/master/docs/%(mod)s_module.rst) -\n' % dict(mod=module))
                README.write('  %(desc)s\n' % dict(desc=description))

    index.closed

README.closed
