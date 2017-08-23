.. _aci_bd_subnet:


aci_bd_subnet - Manage Subnets on Cisco ACI fabrics (fv:Subnet)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage Subnets on Cisco ACI fabrics.
* More information from the internal APIC class *fv:Subnet* at https://developer.cisco.com/media/mim-ref/MO-fvSubnet.html.


Requirements (on host that executes module)
-------------------------------------------

  * ACI Fabric 1.0(3f)+


Options
-------

.. raw:: html

    <table border=1 cellpadding=4>

    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>

    <tr>
    <td>bd<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the Bridge Domain.</div>
    </td>
    </tr>

    <tr>
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The description for the Subnet.</div>
    </td>
    </tr>

    <tr>
    <td>enable_vip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>False</li><li>True</li></ul></td>
    <td>
        <div>Determines if the Subnet should be treated as a VIP; used when the BD is extended to multiple sites.</div>
        <div>The APIC defaults new Subnets to &quot;no&quot;.</div>
    </td>
    </tr>

    <tr>
    <td>gateway<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The IPv4 or IPv6 gateway address for the Subnet.</div>
        </br><div style="font-size: small;">aliases: gateway_ip</div>
    </td>
    </tr>

    <tr>
    <td>mask<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>Any 0 to 32 for IPv4 Addresses</li><li>0-128 for IPv6 Addresses</li></ul></td>
    <td>
        <div>The subnet mask for the Subnet.</div>
        <div>This is the number assocated with CIDR notation.</div>
        </br><div style="font-size: small;">aliases: subnet_mask</div>
    </td>
    </tr>

    <tr>
    <td>nd_prefix_policy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The IPv6 Neighbor Discovery Prefix Policy to associate with the Subnet.</div>
    </td>
    </tr>

    <tr>
    <td>preferred<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>False</li><li>True</li></ul></td>
    <td>
        <div>Determines if the Subnet is preferred over all available Subnets. Only one Subnet per Address Family (IPv4/IPv6). can be preferred in the Bridge Domain.</div>
        <div>The APIC defaults new Subnets to &quot;no&quot;.</div>
    </td>
    </tr>

    <tr>
    <td>route_profile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The Route Profile to the associate with the Subnet.</div>
    </td>
    </tr>

    <tr>
    <td>route_profile_l3_out<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The L3 Out that contains the assocated Route Profile.</div>
    </td>
    </tr>

    <tr>
    <td>scope<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>private</td>
    <td><ul><li>private</li><li>public</li><li>shared</li></ul></td>
    <td>
        <div>Determines if scope of the Subnet.</div>
        <div>The private option only allows communication with hosts in the same VRF.</div>
        <div>The public option allows the Subnet to be advertised outside of the ACI Fabric, and allows communication with hosts in other VRFs.</div>
        <div>The shared option limits communication to hosts in either the same VRF or the shared VRF.</div>
        <div>The APIC defaults new Subnets to &quot;private&quot;.</div>
    </td>
    </tr>

    <tr>
    <td>subnet_control<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>nd_ra</td>
    <td><ul><li>nd_ra</li><li>no_gw</li><li>querier_ip</li><li>unspecified</li></ul></td>
    <td>
        <div>Determines the Subnet's Control State.</div>
        <div>The querier_ip option is used to treat the gateway_ip as an IGMP querier source IP.</div>
        <div>The nd_ra option is used to treate the gateway_ip address as a Neighbor Discovery Router Advertisement Prefix.</div>
        <div>The no_gw option is used to remove default gateway functionality from the gateway address.</div>
        <div>The APIC defaults new Subnets to &quot;nd_ra&quot;.</div>
    </td>
    </tr>

    <tr>
    <td>subnet_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the Subnet.</div>
        </br><div style="font-size: small;">aliases: name</div>
    </td>
    </tr>

    <tr>
    <td>tenant<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the Tenant.</div>
        </br><div style="font-size: small;">aliases: tenant_name</div>
    </td>
    </tr>

    </table>
    </br>



Examples
--------

 ::

     # 


Notes
-----

.. note::
    - The ``gateway`` parameter is the root key used to access the Subnet (not name), so the ``gateway`` is required when the state is ``absent`` or ``present``.
    - The ``tenant`` and ``bd`` used must exist before using this module in your playbook. The :ref:`aci_tenant <aci_tenant>` module and :ref:`aci_bd <aci_bd>` can be used for these.



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support Level
~~~~~~~~~~~~~

This module is maintained by The Ansible Community

For more information on what this means please read :doc:`modules_support`.


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
