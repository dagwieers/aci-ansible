.. _aci_intf_policy_lldp:


aci_intf_policy_lldp - Manage LLDP interface policies on Cisco ACI fabrics (lldp:IfPol)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage LLDP interface policies on Cisco ACI fabrics.
* More information from the internal APIC class *lldp:IfPol* at https://developer.cisco.com/media/mim-ref/MO-lldpIfPol.html.


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
                <tr><td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The description for the LLDP interface policy name.</div></br>
    <div style="font-size: small;">aliases: descr<div>        </td></tr>
                <tr><td>lldp_policy<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The LLDP interface policy name.</div></br>
    <div style="font-size: small;">aliases: name<div>        </td></tr>
                <tr><td>receive_state<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>enabled</td>
        <td><ul><li>disabled</li><li>enabled</li></ul></td>
        <td><div>Enable or disable Receive state (FIXME!)</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>absent</li><li>present</li><li>query</li></ul></td>
        <td><div>Use <code>present</code> or <code>absent</code> for adding or removing.</div><div>Use <code>query</code> for listing an object or multiple objects.</div>        </td></tr>
                <tr><td>transmit_state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>enabled</td>
        <td><ul><li>disabled</li><li>enabled</li></ul></td>
        <td><div>Enable or Disable Transmit state (FIXME!)</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    - aci_intf_policy_lldp:
        hostname: '{{ hostname }}'
        username: '{{ username }}'
        password: '{{ password }}'
        lldp_policy: '{{ lldp_policy }}'
        description: '{{ description }}'
        receive_state: '{{ receive_state }}'
        transmit_state: '{{ transmit_state }}'





Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support Level
~~~~~~~~~~~~~

This module is maintained by The Ansible Community

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
