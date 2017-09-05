.. _aci_config_rollback:


aci_config_rollback - Provides rollback and rollback preview functionality for Cisco ACI fabrics (config:ImportP)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Provides rollback and rollback preview functionality for Cisco ACI fabric.
* Config Rollbacks are done using snapshots ``aci_snapshot`` with the configImportP class.
* More information from the internal APIC class *config:ImportP* at https://developer.cisco.com/media/mim-ref/MO-configImportP.html.


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
    <td>compare_export_policy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The export policy that the <code>compare_snapshot</code> is associated to.</div>
    </td>
    </tr>

    <tr>
    <td>compare_snapshot<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the snapshot to compare with <code>snapshot</code>.</div>
    </td>
    </tr>

    <tr>
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The description for the Import Policy.</div>
        </br><div style="font-size: small;">aliases: descr</div>
    </td>
    </tr>

    <tr>
    <td>export_policy<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>The export policy that the <code>snapshot</code> is associated to.</div>
    </td>
    </tr>

    <tr>
    <td>fail_on_decrypt<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Determines if the APIC should fail the rollback if unable to decrypt secured data.</div>
        <div>The APIC defaults new Import Policies to <code>true</code>.</div>
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
    <td>import_mode<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>atomic</td>
    <td><ul><li>atomic</li><li>best-effort</li></ul></td>
    <td>
        <div>Determines how the import should be handled by the APIC.</div>
        <div>The APIC defaults new Import Policies to <code>atomic</code>.</div>
    </td>
    </tr>

    <tr>
    <td>import_policy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the Import Policy to use for config rollback.</div>
    </td>
    </tr>

    <tr>
    <td>import_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>replace</td>
    <td><ul><li>merge</li><li>replace</li></ul></td>
    <td>
        <div>Determines how the current and snapshot configuration should be compared for replacement.</div>
        <div>The APIC defaults new Import Policies to <code>replace</code>.</div>
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
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the snapshot to rollback to, or the base snapshot to use for comparison.</div>
        <div>The <code>aci_snapshot</code> module can be used to query the list of available snapshots.</div>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>rollback</td>
    <td><ul><li>preview</li><li>rollback</li></ul></td>
    <td>
        <div>Use <code>preview</code> for previewing the diff between two snapshots.</div>
        <div>Use <code>rollback</code> for reverting the configuration to a previous snapshot.</div>
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
    
    -name: Query Existing Snapshots
      aci_config_snapshot:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        state: query
        export_policy: config_backup
    
    - name: Compare Snapshot Files
      aci_config_rollback:
        hostname: apic
        username: admin
        password: SomeSecretPassword
        state: preview
        export_policy: config_backup
        snapshot: 'run-2017-08-28T06-24-01'
        compare_export_policy: config_backup
        compare_snapshot: 'run-2017-08-27T23-43-56'
    
    - name: Rollback Configuration
      aci_config_rollback
        hostname: apic
        username: admin
        password: SomeSecretPassword
        state: rollback
        import_policy: rollback_config
        export_policy: config_backup
        snapshot: 'run-2017-08-28T06-24-01'
    
    - name: Rollback Configuration
      aci_config_rollback
        hostname: apic
        username: admin
        password: SomeSecretPassword
        state: rollback
        import_policy: rollback_config
        export_policy: config_backup
        snapshot: 'run-2017-08-28T06-24-01'
        description: 'Rollback 8-27 changes"
        import_mode: atomic
        import_type: replace
        fail_on_decrypt: 'yes'


Notes
-----

.. note::
    - By default, if an environment variable ``<protocol>_proxy`` is set on the target host, requests will be sent through that proxy. This behaviour can be overridden by setting a variable for this task (see `setting the environment <http://docs.ansible.com/playbooks_environment.html>`_), or by using the ``use_proxy`` option.
    - HTTP redirects can redirect from HTTP to HTTPS so you should be sure that your proxy environment for both protocols is correct.



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.

For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
