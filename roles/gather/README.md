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
          - "bgp_global"
          - "bgp_address_family"
```

Example Output
When the playbook is executed successfully, the output will display the all_gathered_resources for the specified resources.
- Yaml Output
```yaml
   all_gathered_resources:
        bgp_address_family:
            address_family:
            -   afi: ipv4
                networks:
                -   prefix: 10.0.0.0/24
                -   prefix: 172.16.0.0/16
                safi: unicast
            -   afi: ipv6
                networks:
                -   prefix: 2001:db8::/32
                -   prefix: 2001:db8:abcd::/48
                safi: unicast
            as_number: '65001'
        bgp_global:
            as_number: '65001'
            neighbors:
            -   neighbor_address: 192.168.1.2
                remote_as: '65002'
                update_source: loopback0
            -   neighbor_address: 192.168.2.1
                remote_as: '65002'
            -   neighbor_address: 2001:db8::2
                remote_as: '65003'
            router_id: 1.1.1.1
            timers:
                bgp:
                    holdtime: 90
                    keepalive: 30
    device_info:
        ansible_network_os: cisco.nxos.nxos
        bootflash: 4495360
        device_name: aayushNXOS
        hardware:
            model: Nexus9000 C9300v
            serial_number: 9GT0HF5KR3M
        last_reset_reason: Unknown
        license:
            count: 1
            description: LAN license for Nexus 9300-XF
            enforcement_type: NOT ENFORCED
            license_type: Generic
            name: LAN_ENTERPRISE_SERVICES_PKG
            status: IN USE
            version: 1.0
        memory:
            free_mb: 1377.3515625
            total_mb: 7945.015625
            used_mb: 6567.6640625
        nxos_compile_time: 11/30/2023 12:00:00 [12/14/2023 05:25:50]
        nxos_image_file: bootflash:///nxos64-cs.10.4.2.F.bin
        os_type: NX-OS
        processes:
            running: 1
            total: 925
        processor:
            memory: 8135696
            type: Intel(R) Xeon(R) Platinum 8275CL CPU @ 3.00GHz
        release_type: Feature Release
        uptime:
            days: 119
            hours: 22
            minutes: 4
            seconds: 46
        version: 10.4(2)
```
- Json output
```json
TASK [network.reports.gather : Display gathered facts as pretty JSON] *********************************************************************************************************************************************************
task path: /home/aaanand/ansible-dev-workspace/collections/ansible_collections/network/reports/roles/gather/tasks/main.yaml:21
ok: [ansible-2] => 
  msg: |-
    {
        "all_gathered_resources": {
            "bgp_address_family": {
                "address_family": [
                    {
                        "afi": "ipv4",
                        "networks": [
                            {
                                "prefix": "10.0.0.0/24"
                            },
                            {
                                "prefix": "172.16.0.0/16"
                            }
                        ],
                        "safi": "unicast"
                    },
                    {
                        "afi": "ipv6",
                        "networks": [
                            {
                                "prefix": "2001:db8::/32"
                            },
                            {
                                "prefix": "2001:db8:abcd::/48"
                            }
                        ],
                        "safi": "unicast"
                    }
                ],
                "as_number": "65001"
            },
            "bgp_global": {
                "as_number": "65001",
                "neighbors": [
                    {
                        "neighbor_address": "192.168.1.2",
                        "remote_as": "65002",
                        "update_source": "loopback0"
                    },
                    {
                        "neighbor_address": "192.168.2.1",
                        "remote_as": "65002"
                    },
                    {
                        "neighbor_address": "2001:db8::2",
                        "remote_as": "65003"
                    }
                ],
                "router_id": "1.1.1.1",
                "timers": {
                    "bgp": {
                        "holdtime": 90,
                        "keepalive": 30
                    }
                }
            }
        },
        "device_info": {
            "ansible_network_os": "cisco.nxos.nxos",
            "bootflash": 4495360,
            "device_name": "aayushNXOS",
            "hardware": {
                "model": "Nexus9000 C9300v",
                "serial_number": "9GT0HF5KR3M"
            },
            "last_reset_reason": "Unknown",
            "license": {
                "count": 1,
                "description": "LAN license for Nexus 9300-XF",
                "enforcement_type": "NOT ENFORCED",
                "license_type": "Generic",
                "name": "LAN_ENTERPRISE_SERVICES_PKG",
                "status": "IN USE",
                "version": 1.0
            },
            "memory": {
                "free_mb": 1493.84765625,
                "total_mb": 7945.015625,
                "used_mb": 6451.16796875
            },
            "nxos_compile_time": "11/30/2023 12:00:00 [12/14/2023 05:25:50]",
            "nxos_image_file": "bootflash:///nxos64-cs.10.4.2.F.bin",
            "os_type": "NX-OS",
            "processes": {
                "running": 1,
                "total": 904
            },
            "processor": {
                "memory": 8135696,
                "type": "Intel(R) Xeon(R) Platinum 8275CL CPU @ 3.00GHz"
            },
            "release_type": "Feature Release",
            "uptime": {
                "days": 119,
                "hours": 21,
                "minutes": 56,
                "seconds": 31
            },
            "version": "10.4(2)"
        }
    }
```
- Xml output 
```xml
  <?xml version="1.0" ?>
    <facts>
      <all_gathered_resources type="dict">
        <bgp_address_family type="dict">
          <as_number type="str">65001</as_number>
          <address_family type="list">
            <item type="dict">
              <afi type="str">ipv4</afi>
              <safi type="str">unicast</safi>
              <networks type="list">
                <item type="dict">
                  <prefix type="str">10.0.0.0/24</prefix>
                </item>
                <item type="dict">
                  <prefix type="str">172.16.0.0/16</prefix>
                </item>
              </networks>
            </item>
            <item type="dict">
              <afi type="str">ipv6</afi>
              <safi type="str">unicast</safi>
              <networks type="list">
                <item type="dict">
                  <prefix type="str">2001:db8::/32</prefix>
                </item>
                <item type="dict">
                  <prefix type="str">2001:db8:abcd::/48</prefix>
                </item>
              </networks>
            </item>
          </address_family>
        </bgp_address_family>
        <bgp_global type="dict">
          <as_number type="str">65001</as_number>
          <router_id type="str">1.1.1.1</router_id>
          <timers type="dict">
            <bgp type="dict">
              <keepalive type="int">30</keepalive>
              <holdtime type="int">90</holdtime>
            </bgp>
          </timers>
          <neighbors type="list">
            <item type="dict">
              <neighbor_address type="str">192.168.1.2</neighbor_address>
              <remote_as type="str">65002</remote_as>
              <update_source type="str">loopback0</update_source>
            </item>
            <item type="dict">
              <neighbor_address type="str">192.168.2.1</neighbor_address>
              <remote_as type="str">65002</remote_as>
            </item>
            <item type="dict">
              <neighbor_address type="str">2001:db8::2</neighbor_address>
              <remote_as type="str">65003</remote_as>
            </item>
          </neighbors>
        </bgp_global>
      </all_gathered_resources>
      <device_info type="dict">
        <os_type type="str">NX-OS</os_type>
        <release_type type="str">Feature Release</release_type>
        <version type="str">10.4(2)</version>
        <nxos_image_file type="str">bootflash:///nxos64-cs.10.4.2.F.bin</nxos_image_file>
        <nxos_compile_time type="str">11/30/2023 12:00:00 [12/14/2023 05:25:50]</nxos_compile_time>
        <hardware type="dict">
          <model type="str">Nexus9000 C9300v</model>
          <serial_number type="str">9GT0HF5KR3M</serial_number>
        </hardware>
        <processor type="dict">
          <type type="str">Intel(R) Xeon(R) Platinum 8275CL CPU @ 3.00GHz</type>
          <memory type="int">8135696</memory>
        </processor>
        <device_name type="str">aayushNXOS</device_name>
        <bootflash type="int">4495360</bootflash>
        <uptime type="dict">
          <days type="int">119</days>
          <hours type="int">22</hours>
          <minutes type="int">0</minutes>
          <seconds type="int">55</seconds>
        </uptime>
        <last_reset_reason type="str">Unknown</last_reset_reason>
        <processes type="dict">
          <total type="int">914</total>
          <running type="int">1</running>
        </processes>
        <memory type="dict">
          <total_mb type="float">7945.015625</total_mb>
          <free_mb type="float">1397.140625</free_mb>
          <used_mb type="float">6547.875</used_mb>
        </memory>
        <license type="dict">
          <status type="str">IN USE</status>
          <name type="str">LAN_ENTERPRISE_SERVICES_PKG</name>
          <description type="str">LAN license for Nexus 9300-XF</description>
          <count type="int">1</count>
          <version type="float">1.0</version>
          <enforcement_type type="str">NOT ENFORCED</enforcement_type>
          <license_type type="str">Generic</license_type>
        </license>
        <ansible_network_os type="str">cisco.nxos.nxos</ansible_network_os>
      </device_info>
    </facts>
```
## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information

- Ansible Network Content Team
