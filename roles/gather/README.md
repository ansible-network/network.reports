# gather

## Overview

The `gather` role collects comprehensive network device facts, including hardware details using native parsers.

## Features

- Retrieve structured facts for specified network resources.
- Gathers detailed hardware information from network devices using native parsers
- Support for various network resources like `bgp_global`, `interfaces`, `vlans`, etc.
- Provides data in both YAML and XML formats for easy consumption and analysis.

## Variables

| Variable Name        | Default Value | Required | Type | Description                                            |                Example                 |
| :------------------- | :-----------: | :------: | :--: | :----------------------------------------------------- | :------------------------------------: |
| `ansible_network_os` |     `""`      |    no    | str  | Network OS to be used during gather.                   |           `"cisco.ios.ios"`            |
| `resources`          |    `[all]`    |    no    | list | List of resources for which facts need to be gathered. | `['bgp_global', 'bgp_address_family']` |

## Usage

Below is an example playbook demonstrating how to use the `gather` role, where we will retrieve facts for the specified network resources:

```yaml
---
- name: Gather structured facts for network resources
  hosts: all
  gather_facts: false
  tasks:
    - name: Invoke gather role
      ansible.builtin.include_role:
        name: network.reports.gather
      vars:
        format: json
        resources:
          - "interfaces"
          - "l2_interfaces"
          - "l3_interfaces"
```

Example Output
When the playbook is executed successfully, the output will display the all_gathered_resources for the specified resources.
- Yaml Output
```yaml
     ansible_1:
        all_gathered_resources:
            device_info:
                ansible_network_os: cisco.ios.ios
                build_info:
                    compiled_by: sweickge
                    compiled_date: Tue 29-Sep-20 11:53
                config_register: 257
                device_name: S1
                hardware:
                    serial_number: 9LYOJDDPHUB
                last_reload_reason: Unknown reason
                memory:
                    free_mb: 538491.88671875
                    nvram: 256K
                    total_mb: 598207.84375
                reload_reason: reload
                system_image: flash0:/vios_l2-adventerprisek9-m
            interfaces:
            -   description: temp1
                enabled: true
                name: GigabitEthernet0/0
            -   enabled: true
                name: GigabitEthernet0/1
            -   enabled: true
                name: GigabitEthernet0/2
            -   enabled: true
                name: GigabitEthernet0/3
            -   enabled: true
                name: Vlan1
            l2_interfaces:
            -   mode: access
                name: GigabitEthernet0/0
            -   name: GigabitEthernet0/1
            -   name: GigabitEthernet0/2
            -   mode: access
                name: GigabitEthernet0/3
            -   name: Vlan1
            l3_interfaces:
            -   name: GigabitEthernet0/0
            -   name: GigabitEthernet0/1
            -   name: GigabitEthernet0/2
            -   name: GigabitEthernet0/3
            -   autostate: true
                ipv4:
                -   dhcp:
                        enable: true
                name: Vlan1
    ansible_4:
        all_gathered_resources:
            device_info:
                ansible_network_os: cisco.iosxr.iosxr
                build_info:
                    built_by: ingunawa
                    built_host: iox-ucs-067
                    built_on: Mon Jul 25 02:41:45 PDT 2022
                    label: 7.7.1-0
                    location: /opt/cisco/XR/packages/
                    workspace: /auto/srcarchive12/prod/7.7.1/xrv9k/ws
                device_name: iosxr
                hardware:
                    model: cisco IOS-XRv 9000
                    serial_number: 3B5CEE0EED4
                license:
                    count: 1
                    export_status: NOT RESTRICTED
                    name: IOS-XRv-9000-vRouter-VM
                    status: EVAL MODE
                    version: 1.0
                memory:
                    free_mb: 3525M
                    total_mb: 6144M
                memory_summary:
                    image_size: 4M
                os_type: IOS XR
                version: 7.7.1
            interfaces:
            -   enabled: true
                name: Loopback0
            -   enabled: true
                name: Loopback888
            -   enabled: true
                name: Loopback999
            -   enabled: true
                name: MgmtEth0/RP0/CPU0/0
            -   enabled: true
                name: GigabitEthernet1/1/1/1
                speed: 10
            l2_interfaces:
            -   name: Loopback0
            -   name: Loopback888
            -   name: Loopback999
            -   name: MgmtEth0/RP0/CPU0/0
            -   name: GigabitEthernet1/1/1/1
            l3_interfaces:
            -   name: Loopback0
            -   name: Loopback888
            -   name: Loopback999
            -   ipv4:
                -   address: dhcp
                name: MgmtEth0/RP0/CPU0/0
            -   name: GigabitEthernet1/1/1/1
    ansible_5:
        all_gathered_resources:
            device_info:
                account.smart_account: <none>
                account.virtual_account: <none>
                agent.version: 5.9.18_rel/75
                ansible_network_os: cisco.ios.ios
                build_info:
                    compiled_by: mcpre
                    compiled_date: Wed 13-Dec-23 21:43
                config_register: 8450
                data_privacy.hostname_privacy: DISABLED
                data_privacy.version_privacy: DISABLED
                detailed_info:
                    detailed_version: 17.13.1a
                    product: Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M)
                device_name: aayuIOS
                hardware:
                    model: ' Cisco C8000V'
                    processor: VXE
                    serial_number: 9CX13C870MC
                last_reload_reason: factory-reset
                license:
                    smart_licensing: Smart Licensing Using Policy
                    type: Perpetual
                license_conversion.enabled: true
                license_overall.status: NOT INSTALLED
                memory:
                    bootflash: 5234688K
                    free_mb: 1822106.91015625
                    nvram: 32768K
                    physical: 3960676K
                    total_mb: 2017116.1796875
                miscellaneous.custom_id: <empty>
                os_type: IOS XE
                policy.ack_required: yes (CISCO default)
                policy.in_use: Merged from multiple sources.
                product_info.pid: C8000V
                product_info.serial: 9CX13C870MC
                reload_reason: reload
                smart_licensing.status: ENABLED
                system_image: bootflash:packages.conf
                transport.type: cslu
                transport.vrf: <empty>
                version: 17.13.01a
            interfaces:
            -   description: Management interface do not change
                enabled: true
                name: GigabitEthernet1
            -   enabled: true
                name: GigabitEthernet2
                speed: '1000'
            -   enabled: true
                name: GigabitEthernet3
                speed: '1000'
            -   description: Auto_Cable_Testing_Ansible
                enabled: false
                name: GigabitEthernet4
            -   enabled: true
                name: Loopback888
            -   enabled: true
                name: Loopback999
            l2_interfaces:
            -   name: Loopback888
            -   name: Loopback999
            -   name: GigabitEthernet1
            -   name: GigabitEthernet2
            -   name: GigabitEthernet3
            -   name: GigabitEthernet4
            l3_interfaces:
            -   ipv4:
                -   dhcp:
                        enable: true
                name: GigabitEthernet1
            -   name: GigabitEthernet2
            -   name: GigabitEthernet3
            -   name: GigabitEthernet4
            -   name: Loopback888
            -   name: Loopback999
```
- Json output
```json
TASK [network.reports.gather : Display gathered facts as pretty JSON] *********************************************************************************************************************************************************
task path: /home/aaanand/ansible-dev-workspace/collections/ansible_collections/network/reports/roles/gather/tasks/main.yaml:21
ok: [ansible-2] => 
  msg: |-
    {
        "ansible_1": {
            "all_gathered_resources": {
                "device_info": {
                    "ansible_network_os": "cisco.ios.ios",
                    "build_info": {
                        "compiled_by": "sweickge",
                        "compiled_date": "Tue 29-Sep-20 11:53"
                    },
                    "config_register": 257,
                    "device_name": "S1",
                    "hardware": {
                        "serial_number": "9LYOJDDPHUB"
                    },
                    "last_reload_reason": "Unknown reason",
                    "memory": {
                        "free_mb": 538597.84765625,
                        "nvram": "256K",
                        "total_mb": 598207.84375
                    },
                    "reload_reason": "reload",
                    "system_image": "flash0:/vios_l2-adventerprisek9-m"
                },
                "interfaces": [
                    {
                        "description": "temp1",
                        "enabled": true,
                        "name": "GigabitEthernet0/0"
                    },
                    {
                        "enabled": true,
                        "name": "GigabitEthernet0/1"
                    },
                    {
                        "enabled": true,
                        "name": "GigabitEthernet0/2"
                    },
                    {
                        "enabled": true,
                        "name": "GigabitEthernet0/3"
                    },
                    {
                        "enabled": true,
                        "name": "Vlan1"
                    }
                ],
                "l2_interfaces": [
                    {
                        "mode": "access",
                        "name": "GigabitEthernet0/0"
                    },
                    {
                        "name": "GigabitEthernet0/1"
                    },
                    {
                        "name": "GigabitEthernet0/2"
                    },
                    {
                        "mode": "access",
                        "name": "GigabitEthernet0/3"
                    },
                    {
                        "name": "Vlan1"
                    }
                ],
                "l3_interfaces": [
                    {
                        "name": "GigabitEthernet0/0"
                    },
                    {
                        "name": "GigabitEthernet0/1"
                    },
                    {
                        "name": "GigabitEthernet0/2"
                    },
                    {
                        "name": "GigabitEthernet0/3"
                    },
                    {
                        "autostate": true,
                        "ipv4": [
                            {
                                "dhcp": {
                                    "enable": true
                                }
                            }
                        ],
                        "name": "Vlan1"
                    }
                ]
            }
        },
        "ansible_4": {
            "all_gathered_resources": {
                "device_info": {
                    "ansible_network_os": "cisco.iosxr.iosxr",
                    "build_info": {
                        "built_by": "ingunawa",
                        "built_host": "iox-ucs-067",
                        "built_on": "Mon Jul 25 02:41:45 PDT 2022",
                        "label": "7.7.1-0",
                        "location": "/opt/cisco/XR/packages/",
                        "workspace": "/auto/srcarchive12/prod/7.7.1/xrv9k/ws"
                    },
                    "device_name": "iosxr",
                    "hardware": {
                        "model": "cisco IOS-XRv 9000",
                        "serial_number": "3B5CEE0EED4"
                    },
                    "license": {
                        "count": 1,
                        "export_status": "NOT RESTRICTED",
                        "name": "IOS-XRv-9000-vRouter-VM",
                        "status": "EVAL MODE",
                        "version": 1.0
                    },
                    "memory": {
                        "free_mb": "3531M",
                        "total_mb": "6144M"
                    },
                    "memory_summary": {
                        "image_size": "4M"
                    },
                    "os_type": "IOS XR",
                    "version": "7.7.1"
                },
                "interfaces": [
                    {
                        "enabled": true,
                        "name": "Loopback0"
                    },
                    {
                        "enabled": true,
                        "name": "Loopback888"
                    },
                    {
                        "enabled": true,
                        "name": "Loopback999"
                    },
                    {
                        "enabled": true,
                        "name": "MgmtEth0/RP0/CPU0/0"
                    },
                    {
                        "enabled": true,
                        "name": "GigabitEthernet1/1/1/1",
                        "speed": 10
                    }
                ],
                "l2_interfaces": [
                    {
                        "name": "Loopback0"
                    },
                    {
                        "name": "Loopback888"
                    },
                    {
                        "name": "Loopback999"
                    },
                    {
                        "name": "MgmtEth0/RP0/CPU0/0"
                    },
                    {
                        "name": "GigabitEthernet1/1/1/1"
                    }
                ],
                "l3_interfaces": [
                    {
                        "name": "Loopback0"
                    },
                    {
                        "name": "Loopback888"
                    },
                    {
                        "name": "Loopback999"
                    },
                    {
                        "ipv4": [
                            {
                                "address": "dhcp"
                            }
                        ],
                        "name": "MgmtEth0/RP0/CPU0/0"
                    },
                    {
                        "name": "GigabitEthernet1/1/1/1"
                    }
                ]
            }
        },
        "ansible_5": {
            "all_gathered_resources": {
                "device_info": {
                    "account.smart_account": "<none>",
                    "account.virtual_account": "<none>",
                    "agent.version": "5.9.18_rel/75",
                    "ansible_network_os": "cisco.ios.ios",
                    "build_info": {
                        "compiled_by": "mcpre",
                        "compiled_date": "Wed 13-Dec-23 21:43"
                    },
                    "config_register": 8450,
                    "data_privacy.hostname_privacy": "DISABLED",
                    "data_privacy.version_privacy": "DISABLED",
                    "detailed_info": {
                        "detailed_version": "17.13.1a",
                        "product": "Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M)"
                    },
                    "device_name": "aayuIOS",
                    "hardware": {
                        "model": " Cisco C8000V",
                        "processor": "VXE",
                        "serial_number": "9CX13C870MC"
                    },
                    "last_reload_reason": "factory-reset",
                    "license": {
                        "smart_licensing": "Smart Licensing Using Policy",
                        "type": "Perpetual"
                    },
                    "license_conversion.enabled": true,
                    "license_overall.status": "NOT INSTALLED",
                    "memory": {
                        "bootflash": "5234688K",
                        "free_mb": 1822948.05859375,
                        "nvram": "32768K",
                        "physical": "3960676K",
                        "total_mb": 2017116.1796875
                    },
                    "miscellaneous.custom_id": "<empty>",
                    "os_type": "IOS XE",
                    "policy.ack_required": "yes (CISCO default)",
                    "policy.in_use": "Merged from multiple sources.",
                    "product_info.pid": "C8000V",
                    "product_info.serial": "9CX13C870MC",
                    "reload_reason": "reload",
                    "smart_licensing.status": "ENABLED",
                    "system_image": "bootflash:packages.conf",
                    "transport.type": "cslu",
                    "transport.vrf": "<empty>",
                    "version": "17.13.01a"
                },
                "interfaces": [
                    {
                        "description": "Management interface do not change",
                        "enabled": true,
                        "name": "GigabitEthernet1"
                    },
                    {
                        "enabled": true,
                        "name": "GigabitEthernet2",
                        "speed": "1000"
                    },
                    {
                        "enabled": true,
                        "name": "GigabitEthernet3",
                        "speed": "1000"
                    },
                    {
                        "description": "Auto_Cable_Testing_Ansible",
                        "enabled": false,
                        "name": "GigabitEthernet4"
                    },
                    {
                        "enabled": true,
                        "name": "Loopback888"
                    },
                    {
                        "enabled": true,
                        "name": "Loopback999"
                    }
                ],
                "l2_interfaces": [
                    {
                        "name": "Loopback888"
                    },
                    {
                        "name": "Loopback999"
                    },
                    {
                        "name": "GigabitEthernet1"
                    },
                    {
                        "name": "GigabitEthernet2"
                    },
                    {
                        "name": "GigabitEthernet3"
                    },
                    {
                        "name": "GigabitEthernet4"
                    }
                ],
                "l3_interfaces": [
                    {
                        "ipv4": [
                            {
                                "dhcp": {
                                    "enable": true
                                }
                            }
                        ],
                        "name": "GigabitEthernet1"
                    },
                    {
                        "name": "GigabitEthernet2"
                    },
                    {
                        "name": "GigabitEthernet3"
                    },
                    {
                        "name": "GigabitEthernet4"
                    },
                    {
                        "name": "Loopback888"
                    },
                    {
                        "name": "Loopback999"
                    }
                ]
            }
        }
    }
```
- Xml output 
```xml
  <?xml version="1.0" ?>
    <facts>
      <ansible_1 type="dict">
        <all_gathered_resources type="dict">
          <interfaces type="list">
            <item type="dict">
              <name type="str">GigabitEthernet0/0</name>
              <enabled type="bool">true</enabled>
              <description type="str">temp1</description>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet0/1</name>
              <enabled type="bool">true</enabled>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet0/2</name>
              <enabled type="bool">true</enabled>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet0/3</name>
              <enabled type="bool">true</enabled>
            </item>
            <item type="dict">
              <name type="str">Vlan1</name>
              <enabled type="bool">true</enabled>
            </item>
          </interfaces>
          <l2_interfaces type="list">
            <item type="dict">
              <name type="str">GigabitEthernet0/0</name>
              <mode type="str">access</mode>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet0/1</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet0/2</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet0/3</name>
              <mode type="str">access</mode>
            </item>
            <item type="dict">
              <name type="str">Vlan1</name>
            </item>
          </l2_interfaces>
          <l3_interfaces type="list">
            <item type="dict">
              <name type="str">GigabitEthernet0/0</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet0/1</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet0/2</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet0/3</name>
            </item>
            <item type="dict">
              <name type="str">Vlan1</name>
              <ipv4 type="list">
                <item type="dict">
                  <dhcp type="dict">
                    <enable type="bool">true</enable>
                  </dhcp>
                </item>
              </ipv4>
              <autostate type="bool">true</autostate>
            </item>
          </l3_interfaces>
          <device_info type="dict">
            <build_info type="dict">
              <compiled_by type="str">sweickge</compiled_by>
              <compiled_date type="str">Tue 29-Sep-20 11:53</compiled_date>
            </build_info>
            <reload_reason type="str">reload</reload_reason>
            <system_image type="str">flash0:/vios_l2-adventerprisek9-m</system_image>
            <last_reload_reason type="str">Unknown reason</last_reload_reason>
            <hardware type="dict">
              <serial_number type="str">9LYOJDDPHUB</serial_number>
            </hardware>
            <memory type="dict">
              <nvram type="str">256K</nvram>
              <total_mb type="float">598207.84375</total_mb>
              <free_mb type="float">538383.65234375</free_mb>
            </memory>
            <config_register type="int">257</config_register>
            <device_name type="str">S1</device_name>
            <ansible_network_os type="str">cisco.ios.ios</ansible_network_os>
          </device_info>
        </all_gathered_resources>
      </ansible_1>
      <ansible_4 type="dict">
        <all_gathered_resources type="dict">
          <interfaces type="list">
            <item type="dict">
              <name type="str">Loopback0</name>
              <enabled type="bool">true</enabled>
            </item>
            <item type="dict">
              <name type="str">Loopback888</name>
              <enabled type="bool">true</enabled>
            </item>
            <item type="dict">
              <name type="str">Loopback999</name>
              <enabled type="bool">true</enabled>
            </item>
            <item type="dict">
              <name type="str">MgmtEth0/RP0/CPU0/0</name>
              <enabled type="bool">true</enabled>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet1/1/1/1</name>
              <enabled type="bool">true</enabled>
              <speed type="int">10</speed>
            </item>
          </interfaces>
          <l2_interfaces type="list">
            <item type="dict">
              <name type="str">Loopback0</name>
            </item>
            <item type="dict">
              <name type="str">Loopback888</name>
            </item>
            <item type="dict">
              <name type="str">Loopback999</name>
            </item>
            <item type="dict">
              <name type="str">MgmtEth0/RP0/CPU0/0</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet1/1/1/1</name>
            </item>
          </l2_interfaces>
          <l3_interfaces type="list">
            <item type="dict">
              <name type="str">Loopback0</name>
            </item>
            <item type="dict">
              <name type="str">Loopback888</name>
            </item>
            <item type="dict">
              <name type="str">Loopback999</name>
            </item>
            <item type="dict">
              <name type="str">MgmtEth0/RP0/CPU0/0</name>
              <ipv4 type="list">
                <item type="dict">
                  <address type="str">dhcp</address>
                </item>
              </ipv4>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet1/1/1/1</name>
            </item>
          </l3_interfaces>
          <device_info type="dict">
            <version type="str">7.7.1</version>
            <os_type type="str">IOS XR</os_type>
            <build_info type="dict">
              <built_by type="str">ingunawa</built_by>
              <built_on type="str">Mon Jul 25 02:41:45 PDT 2022</built_on>
              <built_host type="str">iox-ucs-067</built_host>
              <workspace type="str">/auto/srcarchive12/prod/7.7.1/xrv9k/ws</workspace>
              <location type="str">/opt/cisco/XR/packages/</location>
              <label type="str">7.7.1-0</label>
            </build_info>
            <hardware type="dict">
              <model type="str">cisco IOS-XRv 9000</model>
              <serial_number type="str">3B5CEE0EED4</serial_number>
            </hardware>
            <memory type="dict">
              <total_mb type="str">6144M</total_mb>
              <free_mb type="str">3519M</free_mb>
            </memory>
            <memory_summary type="dict">
              <image_size type="str">4M</image_size>
            </memory_summary>
            <device_name type="str">iosxr</device_name>
            <license type="dict">
              <status type="str">EVAL MODE</status>
              <name type="str">IOS-XRv-9000-vRouter-VM</name>
              <count type="int">1</count>
              <version type="float">1.0</version>
              <export_status type="str">NOT RESTRICTED</export_status>
            </license>
            <ansible_network_os type="str">cisco.iosxr.iosxr</ansible_network_os>
          </device_info>
        </all_gathered_resources>
      </ansible_4>
      <ansible_5 type="dict">
        <all_gathered_resources type="dict">
          <interfaces type="list">
            <item type="dict">
              <name type="str">GigabitEthernet1</name>
              <enabled type="bool">true</enabled>
              <description type="str">Management interface do not change</description>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet2</name>
              <enabled type="bool">true</enabled>
              <speed type="str">1000</speed>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet3</name>
              <enabled type="bool">true</enabled>
              <speed type="str">1000</speed>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet4</name>
              <enabled type="bool">false</enabled>
              <description type="str">Auto_Cable_Testing_Ansible</description>
            </item>
            <item type="dict">
              <name type="str">Loopback888</name>
              <enabled type="bool">true</enabled>
            </item>
            <item type="dict">
              <name type="str">Loopback999</name>
              <enabled type="bool">true</enabled>
            </item>
          </interfaces>
          <l2_interfaces type="list">
            <item type="dict">
              <name type="str">Loopback888</name>
            </item>
            <item type="dict">
              <name type="str">Loopback999</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet1</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet2</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet3</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet4</name>
            </item>
          </l2_interfaces>
          <l3_interfaces type="list">
            <item type="dict">
              <name type="str">GigabitEthernet1</name>
              <ipv4 type="list">
                <item type="dict">
                  <dhcp type="dict">
                    <enable type="bool">true</enable>
                  </dhcp>
                </item>
              </ipv4>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet2</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet3</name>
            </item>
            <item type="dict">
              <name type="str">GigabitEthernet4</name>
            </item>
            <item type="dict">
              <name type="str">Loopback888</name>
            </item>
            <item type="dict">
              <name type="str">Loopback999</name>
            </item>
          </l3_interfaces>
          <device_info type="dict">
            <version type="str">17.13.01a</version>
            <os_type type="str">IOS XE</os_type>
            <detailed_info type="dict">
              <product type="str">Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M)</product>
              <detailed_version type="str">17.13.1a</detailed_version>
            </detailed_info>
            <build_info type="dict">
              <compiled_by type="str">mcpre</compiled_by>
              <compiled_date type="str">Wed 13-Dec-23 21:43</compiled_date>
            </build_info>
            <reload_reason type="str">reload</reload_reason>
            <system_image type="str">bootflash:packages.conf</system_image>
            <last_reload_reason type="str">factory-reset</last_reload_reason>
            <license type="dict">
              <type type="str">Perpetual</type>
              <smart_licensing type="str">Smart Licensing Using Policy</smart_licensing>
            </license>
            <memory type="dict">
              <total_mb type="float">2017116.1796875</total_mb>
              <nvram type="str">32768K</nvram>
              <physical type="str">3960676K</physical>
              <bootflash type="str">5234688K</bootflash>
              <free_mb type="float">1821261.6875</free_mb>
            </memory>
            <hardware type="dict">
              <model type="str"> Cisco C8000V</model>
              <processor type="str">VXE</processor>
              <serial_number type="str">9CX13C870MC</serial_number>
            </hardware>
            <config_register type="int">8450</config_register>
            <device_name type="str">aayuIOS</device_name>
            <smart_licensing.status type="str">ENABLED</smart_licensing.status>
            <license_conversion.enabled type="bool">true</license_conversion.enabled>
            <account.smart_account type="str">&lt;none&gt;</account.smart_account>
            <account.virtual_account type="str">&lt;none&gt;</account.virtual_account>
            <data_privacy.hostname_privacy type="str">DISABLED</data_privacy.hostname_privacy>
            <data_privacy.version_privacy type="str">DISABLED</data_privacy.version_privacy>
            <transport.type type="str">cslu</transport.type>
            <transport.vrf type="str">&lt;empty&gt;</transport.vrf>
            <miscellaneous.custom_id type="str">&lt;empty&gt;</miscellaneous.custom_id>
            <policy.in_use type="str">Merged from multiple sources.</policy.in_use>
            <policy.ack_required type="str">yes (CISCO default)</policy.ack_required>
            <product_info.pid type="str">C8000V</product_info.pid>
            <product_info.serial type="str">9CX13C870MC</product_info.serial>
            <agent.version type="str">5.9.18_rel/75</agent.version>
            <license_overall.status type="str">NOT INSTALLED</license_overall.status>
            <ansible_network_os type="str">cisco.ios.ios</ansible_network_os>
          </device_info>
        </all_gathered_resources>
      </ansible_5>
    </facts>

```
## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information

- Ansible Network Content Team
