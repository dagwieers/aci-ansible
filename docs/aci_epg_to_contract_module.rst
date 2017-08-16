.. _aci_epg_to_contract:


aci_epg_to_contract - Bind EPGs to Contracts on Cisco ACI fabrics (fv:RsCons and fvRsProv)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Bind EPGs to Contracts on Cisco ACI fabrics.
* More information from the internal APIC classes *fv:RsCons* at https://developer.cisco.com/media/mim-ref/MO-fvRsCons.html and *fv:RsProv* at https://developer.cisco.com/media/mim-ref/MO-fvRsProv.html.


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
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of an existing application network profile, that will contain the EPGs.</div></br>
    <div style="font-size: small;">aliases: app_profile_name<div>        </td></tr>
                <tr><td>contract<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the contract.</div></br>
    <div style="font-size: small;">aliases: contract_name<div>        </td></tr>
                <tr><td>contract_type<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul><li>consumer</li><li>proivder</li></ul></td>
        <td><div>Determines if the EPG should Provide or Consume the Contract.</div>        </td></tr>
                <tr><td>epg<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the end point group.</div></br>
    <div style="font-size: small;">aliases: epg_name<div>        </td></tr>
                <tr><td>hostname<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>IP Address or hostname of APIC resolvable by Ansible control host.</div></br>
    <div style="font-size: small;">aliases: host<div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password to use for authentication.</div>        </td></tr>
                <tr><td>priority<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>unspecified</td>
        <td><ul><li>level1</li><li>level2</li><li>level3</li><li>unspecified</li></ul></td>
        <td><div>QoS class.</div><div>The APIC defaults new EPG to Contract bindings to unspecified.</div>        </td></tr>
                <tr><td>provider_match<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>at_least_one</td>
        <td><ul><li>all</li><li>at_least_one</li><li>at_most_one</li><li>none</li></ul></td>
        <td><div>The matching algorithm for Provided Contracts.</div><div>The APIC defaults new EPG to Provided Contracts to at_least_one.</div>        </td></tr>
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
    - The ``tenant``, ``app_profile``, ``EPG``, and ``Contract`` used must exist before using this module in your playbook. The :ref:`aci_tenant <aci_tenant>`, :ref:`aci_ap <aci_ap>`, :ref:`aci_epg <aci_epg>`, and :ref:`aci_contract <aci_contract>` modules can be used for this.
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
