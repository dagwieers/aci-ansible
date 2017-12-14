#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Dag Wieers <dag@wieers.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: aci_aep_to_domain
short_description: Bind AEP to Physical or Virtual Domain on Cisco ACI fabrics (infra:RsDomP)
description:
- Bind AEP to Physical or Virtual Domain on Cisco ACI fabrics.
- More information from the internal APIC class
  I(infra:RsDomP) at U(https://developer.cisco.com/site/aci/docs/apis/apic-mim-ref/).
author:
- Dag Wieers (@dagwieers)
version_added: '2.4'
notes:
- The C(aep) and C(domain) parameters should exist before using this module.
  The M(aci_aep) and M(aci_vmm_domain) or M(aci_physical_domain) can be used for these.
options:
  aep:
    description:
    - The name of the Attachable Access Entity Profile.
    required: yes
    aliases: [ aep_name ]
  domain:
    description:
    - The name of the Physical Domain or Virtual Domain.
    required: yes
    aliases: [ domain_name ]
  state:
    description:
    - Use C(present) or C(absent) for adding or removing.
    - Use C(query) for listing an object or multiple objects.
    choices: [ absent, present, query ]
    default: present
'''

EXAMPLES = r''' # '''

RETURN = ''' # '''

from ansible.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule


#  - name: Link AEPs to domains
#    aci_rest:
#      <<: *aci_login
#      path: /api/node/mo/uni/infra/attentp-{{ item.access_policy_aep_name }}.json
#      method: post
#      content:
#        infraRsDomP:
#          attributes:
#            childAction: ''
#            dn: uni/infra/attentp-{{ item.access_policy_aep_name }}/rsdomP-[uni/{{ item.access_policy_aep_domain_name }}]
#            tDn: uni/{{ item.access_policy_aep_domain_name }}

def main():
    argument_spec = aci_argument_spec
    argument_spec.update(
        aep=dict(type='str', aliases=['aep_name']),
        domain=dict(type='str', aliases=['domain_name']),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ['state', 'absent', ['aep', 'domain']],
            ['state', 'present', ['aep', 'domain']],
        ],
    )

    aep = module.params['aep']
    domain = module.params['domain']
    state = module.params['state']

    aci = ACIModule(module)
    aci.construct_url(
        root_class=dict(
            aci_class='infraAttEntityP',
            aci_rn='infra/attentp-{}'.format(aep),
            filter_target='eq(infraRsDomP.name, "{}")'.format(aep),
            module_object=aep,
        ),
        subclass_1=dict(
            aci_class='rsDomP',
            aci_rn='rsdomP-[uni/{}]'.format(domain),
            filter_target='eq(infraRsDomP.name, "{}")'.format(domain),
            module_object=domain,
        ),
    )

    aci.get_existing()

    if state == 'present':
        # Filter out module params with null values
        aci.payload(
            aci_class='infraRsDomP',
            class_config=dict(tDn='uni/' + domain),
        )

        # Generate config diff which will be used as POST request body
        aci.get_diff(aci_class='infraRsDomP')

        # Submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
