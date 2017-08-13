#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: aci_contract_subjects
short_description: Manage initial contract subjects on Cisco ACI fabrics
description:
- Manage initial contract subjects on Cisco ACI fabrics.
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
- Jacob McGill (@jmcgill298)
version_added: '2.4'
requirements:
    - ACI Fabric 1.0(3f)+
notes: Tenant must be exist prior to using this module
options:
   action:
        description:
            - post, get, delete
        required: true
        choices: ['post','get','delete']
   tenant_name:
        description:
            - Tenant Name
        required: true
   subject_name:
        description:
            - Subject Name
        required: true
   contract_name:
        description:
            - Contract Name
        required: true
   reverse_filter:
        description:
            - Select or De-select reverse filter port option
        default: 'no'
        choices: ['yes','no']
   priority:
        description:
            - Qos class
        default: unspecified
        choices: [ 'unspecified','level1','level2','level3']
   target:
        description:
            - Target DSCP
        default: unspecified
   filter_name:
        description:
            - Filter Name
   directive:
        description:
            - Directive for filter  (can be none or log)
   descr:
        description:
            - Description for the AEP
   host:
        description:
            - IP Address or hostname of APIC resolvable by Ansible control host
        required: true
   username:
        description:
            - Username used to login to the switch
        required: true
        default: 'admin'
   password:
        description:
            - Password used to login to the switch
        required: true
   protocol:
        description:
            - Dictates connection protocol to use
        default: https
        choices: ['http', 'https']
'''

EXAMPLES = '''
- aci_contract_subjects:
    action: "{{ action }}"
    subject_name: "{{ subject_name }}"
    contract_name: "{{ contract_name }}"
    tenant_name: "{{ tenant_name }}"
    priority: "{{ priority }}"
    reverse_filter: "{{ reverse_filter }}"
    filter_name: "{{ filter_name }}"
    directive: "{{ directive }}"
    target: "{{ target }}"
    descr: "{{ descr }}"
    host: "{{ inventory_hostname }}"
    username: "{{ user }}"
    password: "{{ pass }}"
    protocol: "{{ protocol }}"
'''

import socket
import json
import requests


def main():

    ''' Ansible module to take all the parameter values from the playbook '''
    module = AnsibleModule(
        argument_spec=dict(
            action=dict(choices=['post', 'get', 'delete']),
            host=dict(required=True),
            username=dict(type='str', default='admin'),
            password=dict(type='str'),
            protocol=dict(choices=['http', 'https'], default='https'),
            contract_name=dict(type="str"),
            subject_name=dict(type="str", required=False),
            tenant_name=dict(type="str", required=False),
            priority=dict(choices=['unspecified', 'level1', 'level2', 'level3'], default='unspecified', required=False),
            reverse_filter=dict(choices=['yes', 'no'], required=False, default='yes'),
            target=dict(type="str", required=False, default='unspecified'),
            descr=dict(type="str", required=False),
            filter_name=dict(type="str", required=False),
            directive=dict(type="str", required=False, default='none'),
        ),
        supports_check_mode=False,
    )

    subject_name = module.params['subject_name']
    tenant_name = module.params['tenant_name']
    priority = module.params['priority']
    reverse_filter = module.params['reverse_filter']
    target = module.params['target']
    descr = module.params['descr']
    contract_name = module.params['contract_name']
    username = module.params['username']
    password = module.params['password']
    protocol = module.params['protocol']
    filter_name = module.params['filter_name']
    directive = module.params['directive']
    host = socket.gethostbyname(module.params['host'])
    action = module.params['action']

    if directive == "none":
        directive = ""
    elif directive == "log":
        directive = "log"
    else:
        print("Please error either none or log as the directive value")

    post_uri = 'api/mo/uni/tn-' + tenant_name + '/brc-' + contract_name + '/subj-' + subject_name + '.json'
    get_uri = 'api/node/class/vzSubj.json'

    ''' Config payload to enable the physical interface '''
    config_data = {
        "vzSubj": {
            "attributes": {
                "name": subject_name,
                "prio": priority,
                "revFltPorts": reverse_filter,
                "targetDscp": target,
                "descr": descr,
            }, "children": [{
                "vzRsSubjFiltAtt": {
                    "attributes": {
                        "directives": directive,
                        "tnVzFilterName": filter_name,
                    }
                }
            }]
        }
    }
    payload_data = json.dumps(config_data)

    ''' authentication || || Throw an error otherwise'''
    apic = '{0}://{1}/'.format(protocol, host)
    auth = dict(aaaUser=dict(attributes=dict(name=username, pwd=password)))
    url = apic + 'api/aaaLogin.json'
    authenticate = requests.post(url, data=json.dumps(auth), timeout=2, verify=False)

    if authenticate.status_code != 200:
        module.fail_json(msg='could not authenticate to apic', status=authenticate.status_code, response=authenticate.text)

    ''' Sending the request to APIC '''
    if post_uri.startswith('/'):
        post_uri = post_uri[1:]
    post_url = apic + post_uri

    if get_uri.startswith('/'):
        get_uri = get_uri[1:]
    get_url = apic + get_uri

    if action == 'post':
        req = requests.post(post_url, cookies=authenticate.cookies, data=payload_data, verify=False)
    elif action == 'delete':
        req = requests.delete(post_url, cookies=authenticate.cookies, data=payload_data, verify=False)
    elif action == 'get':
        req = requests.get(get_url, cookies=authenticate.cookies, data=payload_data, verify=False)

    ''' Check response status and parse it for status || Throw an error otherwise '''
    response = req.text
    status = req.status_code
    changed = False

    if req.status_code == 200:
        if action == 'post':
            changed = True
        else:
            changed = False

    else:
        module.fail_json(msg='error issuing api request', response=response, status=status)

    results = {}
    results['status'] = status
    results['response'] = response
    results['changed'] = changed
    module.exit_json(**results)

from ansible.module_utils.basic import *
if __name__ == "__main__":
    main()
