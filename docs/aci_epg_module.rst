.. _aci_epg:


aci_epg - Manage End Point Groups (EPG) on Cisco ACI fabrics (fv:AEPg)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage End Point Groups (EPG) on Cisco ACI fabrics.
* More information from the internal APIC class *fv:AEPg* at https://developer.cisco.com/media/mim-ref/MO-fvAEPg.html.


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
                <tr><td>app_profile<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Name of an existing application network profile, that will contain the EPGs.</div></br>
    <div style="font-size: small;">aliases: app_profile_name<div>        </td></tr>
                <tr><td>bridge_domain<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Name of the bridge domain being associated with the EPG.</div></br>
    <div style="font-size: small;">aliases: bd_name<div>        </td></tr>
                <tr><td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Description for the EPG.</div></br>
    <div style="font-size: small;">aliases: descr<div>        </td></tr>
                <tr><td>epg<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Name of the end point group.</div></br>
    <div style="font-size: small;">aliases: name, epg_name<div>        </td></tr>
                <tr><td>fwd_control<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>none</td>
        <td><ul><li>none</li><li>proxy-arp</li></ul></td>
        <td><div>The forwarding control used by the EPG.</div><div>The APIC defaults new EPGs to none.</div>        </td></tr>
                <tr><td>hostname<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>IP Address or hostname of APIC resolvable by Ansible control host.</div></br>
    <div style="font-size: small;">aliases: host<div>        </td></tr>
                <tr><td>intra_epg_isolation<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>unenforced</td>
        <td><ul><li>enforced</li><li>unenforced</li></ul></td>
        <td><div>Intra EPG Isolation.</div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password to use for authentication.</div>        </td></tr>
                <tr><td>priority<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>unspecified</td>
        <td><ul><li>level1</li><li>level2</li><li>level3</li><li>unspecified</li></ul></td>
        <td><div>QoS class.</div>        </td></tr>
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

    
    - name: Add a new EPG
      aci_epg:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        tenant: production
        app_profile: default
        epg: app_epg
        description: application EPG
        bridge_domain: vlan_bd
        priority: unspecified
        intra_epg_isolation: unenforced
        state: present
    
    - name: Remove an EPG
      aci_epg:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        tenant: production
        app_profile: default
        epg: app_epg
        state: absent
    
    - name: Query an EPG
      aci_epg:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        tenant: production
        app_profile: default
        epg: app_epg
        state: query
    
    - name: Query all EPgs
      aci_epg:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        state: query


Notes
-----

.. note::
    - The ``tenant`` and ``app_profile`` used must exist before using this module in your playbook. The :ref:`aci_tenant <aci_tenant>` and :ref:`aci_ap <aci_ap>` modules can be used for this.
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
