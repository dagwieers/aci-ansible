.. _aci_epg_to_domain:


aci_epg_to_domain - Manage EPG to Domain bindings on Cisco ACI fabrics [fv:RsDomAtt]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage EPG to Physical and Virtual Domains on Cisco ACI fabrics.
* More information from the internal APIC class ``fv:RsDomAtt`` at https://developer.cisco.com/media/mim-ref/MO-fvRsDomAtt.html.


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
                <tr><td>allow_useg<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>encap</td>
        <td><ul><li>encap</li><li>useg</li></ul></td>
        <td><div>Allows micro-segmentation.</div><div>The APIC defaults new EPG to Domain bindings to use encap</div>        </td></tr>
                <tr><td>app_profile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of an existing application network profile, that will contain the EPGs.</div></br>
    <div style="font-size: small;">aliases: app_profile_name<div>        </td></tr>
                <tr><td>deploy_immediacy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>lazy</td>
        <td><ul><li>immediate</li><li>lazy</li></ul></td>
        <td><div>Determines when the policy is pushed to hardware Policy CAM.</div><div>The APIC defaults new EPG to Domain bindings to lazy.</div>        </td></tr>
                <tr><td>domain_profile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the physical or virtual domain being associated with the EPG.</div></br>
    <div style="font-size: small;">aliases: domain_name<div>        </td></tr>
                <tr><td>domain_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>phys</li><li>vmm</li></ul></td>
        <td><div>Determines if the Domain is physical (phys) or virtual (vmm).</div></br>
    <div style="font-size: small;">aliases: domain<div>        </td></tr>
                <tr><td>encap<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>range from 1 to 4096</li></ul></td>
        <td><div>The VLAN encapsulation for the EPG when binding a VMM Domain with static encap_mode.</div><div>This acts as the secondary encap when using useg.</div>        </td></tr>
                <tr><td>encap_mode<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>auto</td>
        <td><ul><li>auto</li><li>vlan</li><li>vxlan</li></ul></td>
        <td><div>The ecapsulataion method to be used.</div><div>The APIC defaults new EPG to Domain bindings to be auto.</div>        </td></tr>
                <tr><td>epg<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the end point group.</div></br>
    <div style="font-size: small;">aliases: epg_name<div>        </td></tr>
                <tr><td>hostname<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>IP Address or hostname of APIC resolvable by Ansible control host.</div></br>
    <div style="font-size: small;">aliases: host<div>        </td></tr>
                <tr><td>netflow<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>disabled</td>
        <td><ul><li>disabled</li><li>enabled</li></ul></td>
        <td><div>Determines if netflow should be enabled.</div><div>The APIC defaults new EPG to Domain binings to be disabled.</div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password to use for authentication.</div>        </td></tr>
                <tr><td>primary_encap<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>range from 1 to 4096</li></ul></td>
        <td><div>Determines the primary VLAN ID when using useg.</div>        </td></tr>
                <tr><td>resolution_immediacy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>lazy</td>
        <td><ul><li>immediate</li><li>lazy</li><li>pre-provision</li></ul></td>
        <td><div>Determines when the policies should be resolved and available.</div><div>The APIC defaults new EPG to Domain bindings to lazy.</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>absent</li><li>present</li><li>query</li></ul></td>
        <td><div>Use <code>present</code> or <code>absent</code> for adding or removing.</div><div>Use <code>query</code> for listing an object or multiple objects.</div>        </td></tr>
                <tr><td>tenant<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of an existing tenant.</div></br>
    <div style="font-size: small;">aliases: tenant_name<div>        </td></tr>
                <tr><td>timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>30</td>
        <td></td>
        <td><div>The socket level timeout in seconds.</div>        </td></tr>
                <tr><td>use_proxy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If <code>no</code>, it will not use a proxy, even if one is defined in an environment variable on the target hosts.</div>        </td></tr>
                <tr><td>use_ssl<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If <code>no</code>, an HTTP connection will be used instead of the default HTTPS connection.</div>        </td></tr>
                <tr><td>username<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>admin</td>
        <td></td>
        <td><div>The username to use for authentication.</div></br>
    <div style="font-size: small;">aliases: user<div>        </td></tr>
                <tr><td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If <code>no</code>, SSL certificates will not be validated.</div><div>This should only set to <code>no</code> used on personally controlled sites using self-signed certificates.</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

     # 


Notes
-----

.. note::
    - The ``tenant``, ``app_profile``, ``epg``, and ``domain`` used must exist before using this module in your playbook. The :ref:`aci_tenant <aci_tenant>` :ref:`aci_ap <aci_ap>`, :ref:`aci_epg <aci_epg>` :ref:`aci_domain <aci_domain>` modules can be used for this.
    - By default, if an environment variable ``<protocol>_proxy`` is set on the target host, requests will be sent through that proxy. This behaviour can be overridden by setting a variable for this task (see `setting the environment <http://docs.ansible.com/playbooks_environment.html>`_), or by using the ``use_proxy`` option.
    - HTTP redirects can redirect from HTTP to HTTPS so you should be sure that your proxy environment for both protocols is correct.



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support Level
~~~~~~~~~~~~~

This module is maintained by The Ansible Community

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
