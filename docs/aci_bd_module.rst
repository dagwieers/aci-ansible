.. _aci_bd:


aci_bd - Manage Bridge Domains (BD) on Cisco ACI Fabrics (fv:BD)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manages Bridge Domains (BD) on Cisco ACI Fabrics.
* More information from the internal APIC class *fv:BD* at https://developer.cisco.com/media/mim-ref/MO-fvBD.html.


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
                <tr><td>arp_flooding<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>False</li><li>True</li></ul></td>
        <td><div>Determines if the Bridge Domain should flood ARP traffic.</div><div>The APIC defaults new Bridge Domains to &quot;no&quot;.</div>        </td></tr>
                <tr><td>bd<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the Bridge Domain.</div></br>
    <div style="font-size: small;">aliases: bd_name, name<div>        </td></tr>
                <tr><td>bd_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ethernet</li><li>fc</li></ul></td>
        <td><div>The type of traffic on the Bridge Domain.</div><div>The APIC defaults new Bridge Domains to Ethernet.</div>        </td></tr>
                <tr><td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Description for the Bridge Domain.</div>        </td></tr>
                <tr><td>enable_multicast<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>False</li><li>True</li></ul></td>
        <td><div>Determines if PIM is enabled</div><div>The APIC defaults new Bridge Domains to disabled.</div>        </td></tr>
                <tr><td>enable_routing<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>False</li><li>True</li></ul></td>
        <td><div>Determines if IP forwarding should be allowed.</div><div>The APIC defaults new Bridge Domains to IP forwarding enabled.</div>        </td></tr>
                <tr><td>endpoint_clear<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>False</li><li>True</li></ul></td>
        <td><div>Clears all End Points in all Leaves when enabled.</div><div>The APIC defaults new Bridge Domains to disabled.</div><div>The value is not reset to disabled once End Points have been cleared; that requires a second task.</div>        </td></tr>
                <tr><td>endpoint_move_detect<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>default</li><li>garp</li></ul></td>
        <td><div>Determines if GARP should be enabled to detect when End Points move.</div><div>The APIC defaults new Bridge Domains to not use GARP.</div>        </td></tr>
                <tr><td>endpoint_retention_action<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Determines if the Bridge Domain should inherit or resolve the End Point Retention Policy.</div><div>The APIC defaults new Bridge Domain to End Point Retention Policies to resolve the policy.</div>        </td></tr>
                <tr><td>endpoint_retention_policy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>inherit</li><li>resolve</li></ul></td>
        <td><div>The name of the End Point Retention Policy the Bridge Domain should use when overriding the default End Point Retention Policy.</div>        </td></tr>
                <tr><td>igmp_snoop_policy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the IGMP Snooping Policy the Bridge Domain should use when overriding the default IGMP Snooping Policy.</div>        </td></tr>
                <tr><td>ip_learning<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>False</li><li>True</li></ul></td>
        <td><div>Determines if the Bridge Domain should learn End Point IPs.</div><div>The APIC defaults new Bridge Domains to enable IP learning.</div>        </td></tr>
                <tr><td>ipv6_nd_policy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the IPv6 Neighbor Discovery Policy the Bridge Domain should use when overridding teh default IPV6 ND Policy.</div>        </td></tr>
                <tr><td>l2_unknown_unicast<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>proxy</li><li>flood</li></ul></td>
        <td><div>Determines what forwarding method to use for unknown l2 destinations.</div><div>The APIC defaults new Bridge domains to use Hardware Proxy.</div>        </td></tr>
                <tr><td>l3_unknown_multicast<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>flood</li><li>opt-flood</li></ul></td>
        <td><div>Determines the forwarding method to use for unknown multicast destinations.</div><div>The APCI defaults new Bridge Domains to use normal flooding.</div>        </td></tr>
                <tr><td>limit_ip_learn<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>False</li><li>True</li></ul></td>
        <td><div>Determines if the BD should limit IP learning to only subnets owned by the Bridge Domain.</div><div>The APIC defaults new Bridge Domains to learn all IP addresses.</div>        </td></tr>
                <tr><td>multi_dest<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>bd-flood</li><li>drop</li><li>encap-flood</li></ul></td>
        <td><div>Determines the forwarding method for L2 multicast, broadcast, and link layer traffic.</div><div>The APIC defaults new Bridge Domains to use bd-flood.</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>absent</li><li>present</li><li>query</li></ul></td>
        <td><div>Use <code>present</code> or <code>absent</code> for adding or removing.</div><div>Use <code>query</code> for listing an object or multiple objects.</div>        </td></tr>
                <tr><td>tenant<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the Tenant.</div></br>
    <div style="font-size: small;">aliases: tenant_name<div>        </td></tr>
                <tr><td>vrf<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the VRF.</div></br>
    <div style="font-size: small;">aliases: vrf_name<div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    - name: Add Bridge Domain
      aci_bd:
        action: "{{ action }}"
        tenant: "{{ tenant }}"
        bd: "{{ bd }}"
        vrf: "{{ vrf }}"
        arp_flooding: "{{ arp_flooding }}"
        l2_unknown_unicast: "{{ l2_unknown_unicast }}"
        l3_unknown_multicast: "{{ l3_unknown_multicast }}"
        multi_dest: "{{ multi_dest }}"
        gateway_ip: "{{ gateway_ip }}"
        subnet_mask: "{{ subnet_mask }}"
        scope: "{{ scope }}"
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        protocol: "{{ protocol }}"


Notes
-----

.. note::
    - The ``tenant`` used must exist before using this module in your playbook. The :ref:`aci_tenant <aci_tenant>` module can be used for this.



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support Level
~~~~~~~~~~~~~

This module is maintained by The Ansible Community

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
