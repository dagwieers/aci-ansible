.. _aci_bd_to_l3out:


aci_bd_to_l3out - Manage Bridge Domain to L3 Out Bindings on Cisco ACI fabrics [fv:RsBDToOut]
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage Bridge Domain to L3 Out Bindings on Cisco ACI fabrics.
* More information from the internal APIC class ``fv:RsBDToOut`` at https://developer.cisco.com/media/mim-ref/MO-fvRsBDToOut.html.


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
                <tr><td>bd<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the Bridge Domain.</div></br>
    <div style="font-size: small;">aliases: bd_name, bridge_domain<div>        </td></tr>
                <tr><td>l3out<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the l3out to associate with th Bridge Domain.</div>        </td></tr>
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
        </table>
    </br>



Examples
--------

 ::

     # 


Notes
-----

.. note::
    - The ``bd`` and ``l3out`` parameters should exist before using this module. The :ref:`aci_bd <aci_bd>` and :ref:`aci_l3out <aci_l3out>` can be used for these.



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support Level
~~~~~~~~~~~~~

This module is maintained by The Ansible Community

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
