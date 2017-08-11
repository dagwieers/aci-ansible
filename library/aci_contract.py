#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
module: aci_contract
short_description: Manages initial contracts
description:
- Manages contract resources, but does not include subjects although
  subjects can be removed using this module.
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
- Jacob McGill (@jmcgill298)
requirements:
- ACI Fabric 1.0(3f)+
notes:
- The tenant used must exist before using this module in your playbook. The M(aci_tenant) module can be used for this.
options:
  contract:
    description:
    - Contract Name
    required: yes
    aliases: [ contract_name, name ]
  description:
    description:
    - Description for the filter.
    aliases: [ descr ]
  tenant:
    description:
    - The name of the tenant.
    required: yes
    aliases: [ tenant_name ]
  scope:
    description:
    - The scope of a service contract.
    choices: [ application-profile, context, global, tenant ]
    default: 'context'
  priority:
    description:
    - The desired QoS class to be used.
    default: unspecified
    choices: [ level1, level2, level3, unspecified ]
  target:
    description:
    - Target DSCP (FIXME!)
    default: unspecified
extends_documentation_fragment: aci
'''

EXAMPLES = r'''
- aci_contract:
    action: "{{ action }}"
    contract_name: "{{ contract_name }}"
    tenant_name: "{{ tenant_name }}"
    priority: "{{ priority }}"
    scope: "{{ scope }}"
    target: "{{ target }}"
    descr: "{{ descr }}"
    host: "{{ inventory_hostname }}"
    username: "{{ user }}"
    password: "{{ pass }}"
    protocol: "{{ protocol }}"
'''

RETURN = r'''
status:
  description: status code of the http request
  returned: always
  type: int
  sample: 200
response:
  description: response text returned by APIC
  returned: when a HTTP request has been made to APIC
  type: string
  sample: '{"totalCount":"0","imdata":[]}'
'''

from ansible.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = aci_argument_spec
    argument_spec.update(
        contract=dict(type='str', required=False, aliases=['contract_name', 'name']),  # Not required for querying all contracts
        tenant=dict(type='str', required=True, aliases=['tenant_name']),
        description=dict(type='str', aliases=['descr']),
        scope=dict(type='str', default='context', choices=['application-profile', 'context', 'global', 'tenant']),
        priority=dict(type='str', choices=['level1', 'level2', 'level3', 'unspecified']),  # No default provided on purpose
        target=dict(type='str'),  # No default provided on purpose
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        method=dict(type='str', choices=['delete', 'get', 'post'], aliases=['action'], removed_in_version='2.6'),  # Deprecated starting from v2.6
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    contract = module.params['contract']
    tenant = module.params['tenant']
    description = module.params['description']
    scope=module.params['scope']
    priority=module.params['priority']
    target=module.params['target']
    state = module.params['state']

    aci = ACIModule(module)

    if contract is not None:
        # Work with a specific contract
        path = 'api/mo/uni/tn-%(tenant)s/brc-%(contract)s.json' % module.params
    elif state == 'query':
        # Query all contracts
        path = 'api/node/class/vzBrCP.json'
    else:
        module.fail_json(msg="Parameter 'contract' is required for state 'absent' or 'present'")

    aci.result['url'] = '%(protocol)s://%(hostname)s/' % aci.params + path

    aci.get_existing()

    if state == 'present':
        # Filter out module parameters with null values
        aci.payload(aci_class='vzBrCP', class_config=dict(name=contract, descr=description, scope=scope, prio=priority, targetDscp=target))

        # Generate config diff which will be used as POST request body
        aci.get_diff(aci_class='vzBrCP')

        # Submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
