.. _aci_config_snapshot:


aci_config_snapshot - Manage Config Snapshots on Cisco ACI fabrics (config:Snapshot, config:ExportP)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage Config Snapshots on Cisco ACI fabrics.
* Creating new Snapshots is done using the configExportP class.
* Removing Snapshots is done using the configSnapshot class.
* More information from the internal APIC classes *config:Snapshot* at https://developer.cisco.com/media/mim-ref/MO-configSnapshot.html and *config:ExportP* at https://developer.cisco.com/media/mim-ref/MO-configExportP.html.


Requirements (on host that executes module)
-------------------------------------------

  * Tested with ACI Fabric 1.0(3f)+


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
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The description for the Config Export Policy.</div>
        </br><div style="font-size: small;">aliases: descr</div>
    </td>
    </tr>

    <tr>
    <td>export_policy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the Export Policy to use for Config Snapshots.</div>
        </br><div style="font-size: small;">aliases: name</div>
    </td>
    </tr>

    <tr>
    <td>format<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>json</td>
    <td><ul><li>json</li><li>xml</li></ul></td>
    <td>
        <div>Sets the config backup to be formatted in JSON or XML.</div>
        <div>The APIC defaults new Export Policies to <code>json</code></div>
    </td>
    </tr>

    <tr>
    <td>hostname<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>IP Address or hostname of APIC resolvable by Ansible control host.</div>
        </br><div style="font-size: small;">aliases: host</div>
    </td>
    </tr>

    <tr>
    <td>include_secure<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>False</li><li>True</li></ul></td>
    <td>
        <div>Determines if secure information should be included in the backup.</div>
        <div>The APIC defaults new Export Policies to <code>yes</code>.</div>
    </td>
    </tr>

    <tr>
    <td>max_count<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>3</td>
    <td><ul><li>range between 1 and 10</li></ul></td>
    <td>
        <div>Determines how many snapshots can exist for the Export Policy before the APIC starts to rollover.</div>
        <div>The APIC defaults new Export Policies to <code>3</code>.</div>
    </td>
    </tr>

    <tr>
    <td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>The password to use for authentication.</div>
    </td>
    </tr>

    <tr>
    <td>snapshot<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the snapshot to delete.</div>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>absent</li><li>present</li><li>query</li></ul></td>
    <td>
        <div>Use <code>present</code> or <code>absent</code> for adding or removing.</div>
        <div>Use <code>query</code> for listing an object or multiple objects.</div>
    </td>
    </tr>

    <tr>
    <td>timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>30</td>
    <td></td>
    <td>
        <div>The socket level timeout in seconds.</div>
    </td>
    </tr>

    <tr>
    <td>use_proxy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>If <code>no</code>, it will not use a proxy, even if one is defined in an environment variable on the target hosts.</div>
    </td>
    </tr>

    <tr>
    <td>use_ssl<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>If <code>no</code>, an HTTP connection will be used instead of the default HTTPS connection.</div>
    </td>
    </tr>

    <tr>
    <td>username<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>admin</td>
    <td></td>
    <td>
        <div>The username to use for authentication.</div>
        </br><div style="font-size: small;">aliases: user</div>
    </td>
    </tr>

    <tr>
    <td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>If <code>no</code>, SSL certificates will not be validated.</div>
        <div>This should only set to <code>no</code> used on personally controlled sites using self-signed certificates.</div>
    </td>
    </tr>

    </table>
    </br>



Examples
--------

 ::

    
    - name: Create a Snapshot
      aci_config_snapshot:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        state: present
        export_policy: config_backup
        max_count: 10
        description: Backups taken before new configs are applied.
    
    - name: Query all Snapshots
      aci_config_snapshot:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        state: query
    
    - name: Query Snapshots associated with a particular Export Policy
      aci_config_snapshot:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        state: query
        export_policy: config_backup
    
    - name: Delete a Snapshot
      aci_config_snapshot:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        state: absent
        export_policy: config_backup
        snapshot: run-2017-08-24T17-20-05


Notes
-----

.. note::
    - The APIC does not provide a mechanism for naming the snapshots.
    - Snapshot files use the following naming structure: ce_<config export policy name>-<yyyy>-<mm>-<dd>T<hh>:<mm>:<ss>.<mss>+<hh>:<mm>.
    - Snapshot objects use the following naming structure: run-<yyyy>-<mm>-<dd>T<hh>-<mm>-<ss>.
    - By default, if an environment variable ``<protocol>_proxy`` is set on the target host, requests will be sent through that proxy. This behaviour can be overridden by setting a variable for this task (see `setting the environment <http://docs.ansible.com/playbooks_environment.html>`_), or by using the ``use_proxy`` option.
    - HTTP redirects can redirect from HTTP to HTTPS so you should be sure that your proxy environment for both protocols is correct.



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.

For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
