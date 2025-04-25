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
        resources:
          - "bgp_global"
          - "bgp_address_family"
```

Example Output
When the playbook is executed successfully, the output will display the all_gathered_resources for the specified resources.
- Yaml Output
```yaml
TASK [network.reports.gather : Debug combined facts] ****************************************************************************************************
ok: [ansible-4] => 
  all_gathered_resources:
    ansible_network_os: cisco.iosxr.iosxr
    bgp_address_family:
      address_family:
      - advertise_best_external: true
        afi: ipv4
        allocate_label:
          all: true
        bgp:
          attribute_download: true
          scan_time: 20
        safi: unicast
      - afi: vpnv4
        safi: unicast
      - afi: ipv4
        dynamic_med: 9
        redistribute:
        - metric: 10
          protocol: connected
        safi: unicast
        vrf: vrf1
      as_number: '65001'
    bgp_global:
      as_number: '65001'
      bgp:
        router_id: 192.0.1.1
      neighbors:
      - neighbor_address: 192.0.2.1
        remote_as: 65002
      timers:
        holdtime: 90
        keepalive_time: 30
      vrfs:
      - rd:
          auto: true
        vrf: vrf1
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
    interfaces:
    - enabled: true
      name: Loopback0
    - enabled: true
      name: MgmtEth0/RP0/CPU0/0
    - enabled: true
      name: GigabitEthernet0/0/0/0
    - enabled: true
      name: GigabitEthernet0/0/0/1
    l2_interfaces:
    - name: Loopback0
    - name: MgmtEth0/RP0/CPU0/0
    - name: GigabitEthernet0/0/0/0
    - name: GigabitEthernet0/0/0/1
    l3_interfaces:
    - name: Loopback0
    - ipv4:
      - address: dhcp
      name: MgmtEth0/RP0/CPU0/0
    - ipv4:
      - address: 10.1.1.1/29
      name: GigabitEthernet0/0/0/0
    - ipv4:
      - address: 10.0.0.1/24
      name: GigabitEthernet0/0/0/1
    license:
      count: 1
      export_status: NOT RESTRICTED
      name: IOS-XRv-9000-vRouter-VM
      status: EVAL MODE
      version: 1.0
    memory:
      free_mb: 3560M
      total_mb: 6144M
    memory_summary:
      image_size: 4M
    os_type: IOS XR
    ospf_interfaces:
    - address_family:
      - afi: ipv4
        cost: 50
        processes:
        - area:
            area_id: '0'
          process_id: MYOSPF
      name: GigabitEthernet0/0/0/0
      type: gigabitethernet
    ospfv2:
      processes:
      - process_id: LAB3
        router_id: 1.1.1.1
      - process_id: MYOSPF
    ospfv3:
      processes:
      - areas:
        - area_id: '11'
          cost: 11
          default_cost: 5
        - area_id: '22'
          default_cost: 6
        process_id: '10'
        router_id: 1.1.1.1
      - authentication:
          disable: true
        process_id: '26'
      - areas:
        - area_id: '10'
          hello_interval: 2
        process_id: '27'
    uptime:
      days: 3
      hours: 4
      minutes: 52
      weeks: 2
    version: 7.7.1
```
- Json output
```json
{"bgp_address_family": {"as_number": "65001", "address_family": [{"afi": "ipv4", "safi": "unicast", "bgp": {"scan_time": 20, "attribute_download": true}, "advertise_best_external": true, "allocate_label": {"all": true}}, {"afi": "vpnv4", "safi": "unicast"}, {"afi": "ipv4", "safi": "unicast", "vrf": "vrf1", "dynamic_med": 9, "redistribute": [{"protocol": "connected", "metric": 10}]}]}, "bgp_global": {"as_number": "65001", "vrfs": [{"vrf": "vrf1", "rd": {"auto": true}}], "timers": {"keepalive_time": 30, "holdtime": 90}, "bgp": {"router_id": "192.0.1.1"}, "neighbors": [{"neighbor_address": "192.0.2.1", "remote_as": 65002}]}, "interfaces": [{"name": "Loopback0", "enabled": true}, {"name": "MgmtEth0/RP0/CPU0/0", "enabled": true}, {"name": "GigabitEthernet0/0/0/0", "enabled": true}, {"name": "GigabitEthernet0/0/0/1", "enabled": true}], "l2_interfaces": [{"name": "Loopback0"}, {"name": "MgmtEth0/RP0/CPU0/0"}, {"name": "GigabitEthernet0/0/0/0"}, {"name": "GigabitEthernet0/0/0/1"}], "l3_interfaces":
    [{"name": "Loopback0"}, {"name": "MgmtEth0/RP0/CPU0/0", "ipv4": [{"address": "dhcp"}]}, {"name": "GigabitEthernet0/0/0/0", "ipv4": [{"address": "10.1.1.1/29"}]}, {"name": "GigabitEthernet0/0/0/1", "ipv4": [{"address": "10.0.0.1/24"}]}], "ospf_interfaces": [{"name": "GigabitEthernet0/0/0/0", "type": "gigabitethernet", "address_family": [{"afi": "ipv4", "processes": [{"process_id": "MYOSPF", "area": {"area_id": "0"}}], "cost": 50}]}], "ospfv2": {"processes": [{"process_id": "LAB3", "router_id": "1.1.1.1"}, {"process_id": "MYOSPF"}]}, "ospfv3": {"processes": [{"process_id": "10", "router_id": "1.1.1.1", "areas": [{"area_id": "11", "cost": 11, "default_cost": 5}, {"area_id": "22", "default_cost": 6}]}, {"process_id": "26", "authentication": {"disable": true}}, {"process_id": "27", "areas": [{"area_id": "10", "hello_interval": 2}]}]}, "version": "7.7.1", "os_type": "IOS XR", "build_info": {"built_by": "ingunawa", "built_on": "Mon Jul 25 02:41:45 PDT 2022", "built_host": "iox-ucs-067", "workspace":
    "/auto/srcarchive12/prod/7.7.1/xrv9k/ws", "location": "/opt/cisco/XR/packages/", "label": "7.7.1-0"}, "hardware": {"model": "cisco IOS-XRv 9000", "serial_number": "3B5CEE0EED4"}, "uptime": {"weeks": 2, "days": 3, "hours": 4, "minutes": 52}, "memory": {"total_mb": "6144M", "free_mb": "3560M"}, "memory_summary": {"image_size": "4M"}, "device_name": "iosxr", "license": {"status": "EVAL MODE", "name": "IOS-XRv-9000-vRouter-VM", "count": 1, "version": 1.0, "export_status": "NOT RESTRICTED"}, "ansible_network_os": "cisco.iosxr.iosxr"}'
```
- Xml output 
```xml
<?xml version="1.0" encoding="UTF-8" ?><facts><bgp_address_family type="dict"><as_number type="str">65001</as_number><address_family type="list"><item type="dict"><afi type="str">ipv4</afi><safi type="str">unicast</safi><bgp type="dict"><scan_time type="int">20</scan_time><attribute_download type="bool">true</attribute_download></bgp><advertise_best_external type="bool">true</advertise_best_external><allocate_label type="dict"><all type="bool">true</all></allocate_label></item><item type="dict"><afi type="str">vpnv4</afi><safi type="str">unicast</safi></item><item type="dict"><afi type="str">ipv4</afi><safi type="str">unicast</safi><vrf type="str">vrf1</vrf><dynamic_med type="int">9</dynamic_med><redistribute type="list"><item type="dict"><protocol type="str">connected</protocol><metric type="int">10</metric></item></redistribute></item></address_family></bgp_address_family><bgp_global type="dict"><as_number type="str">65001</as_number><vrfs type="list"><item type="dict"><vrf type="str">vrf1</vrf><rd
    type="dict"><auto type="bool">true</auto></rd></item></vrfs><timers type="dict"><keepalive_time type="int">30</keepalive_time><holdtime type="int">90</holdtime></timers><bgp type="dict"><router_id type="str">192.0.1.1</router_id></bgp><neighbors type="list"><item type="dict"><neighbor_address type="str">192.0.2.1</neighbor_address><remote_as type="int">65002</remote_as></item></neighbors></bgp_global><interfaces type="list"><item type="dict"><name type="str">Loopback0</name><enabled type="bool">true</enabled></item><item type="dict"><name type="str">MgmtEth0/RP0/CPU0/0</name><enabled type="bool">true</enabled></item><item type="dict"><name type="str">GigabitEthernet0/0/0/0</name><enabled type="bool">true</enabled></item><item type="dict"><name type="str">GigabitEthernet0/0/0/1</name><enabled type="bool">true</enabled></item></interfaces><l2_interfaces type="list"><item type="dict"><name type="str">Loopback0</name></item><item type="dict"><name type="str">MgmtEth0/RP0/CPU0/0</name></item><item
    type="dict"><name type="str">GigabitEthernet0/0/0/0</name></item><item type="dict"><name type="str">GigabitEthernet0/0/0/1</name></item></l2_interfaces><l3_interfaces type="list"><item type="dict"><name type="str">Loopback0</name></item><item type="dict"><name type="str">MgmtEth0/RP0/CPU0/0</name><ipv4 type="list"><item type="dict"><address type="str">dhcp</address></item></ipv4></item><item type="dict"><name type="str">GigabitEthernet0/0/0/0</name><ipv4 type="list"><item type="dict"><address type="str">10.1.1.1/29</address></item></ipv4></item><item type="dict"><name type="str">GigabitEthernet0/0/0/1</name><ipv4 type="list"><item type="dict"><address type="str">10.0.0.1/24</address></item></ipv4></item></l3_interfaces><ospf_interfaces type="list"><item type="dict"><name type="str">GigabitEthernet0/0/0/0</name><type type="str">gigabitethernet</type><address_family type="list"><item type="dict"><afi type="str">ipv4</afi><processes type="list"><item type="dict"><process_id type="str">MYOSPF</process_id><area
    type="dict"><area_id type="str">0</area_id></area></item></processes><cost type="int">50</cost></item></address_family></item></ospf_interfaces><ospfv2 type="dict"><processes type="list"><item type="dict"><process_id type="str">LAB3</process_id><router_id type="str">1.1.1.1</router_id></item><item type="dict"><process_id type="str">MYOSPF</process_id></item></processes></ospfv2><ospfv3 type="dict"><processes type="list"><item type="dict"><process_id type="str">10</process_id><router_id type="str">1.1.1.1</router_id><areas type="list"><item type="dict"><area_id type="str">11</area_id><cost type="int">11</cost><default_cost type="int">5</default_cost></item><item type="dict"><area_id type="str">22</area_id><default_cost type="int">6</default_cost></item></areas></item><item type="dict"><process_id type="str">26</process_id><authentication type="dict"><disable type="bool">true</disable></authentication></item><item type="dict"><process_id type="str">27</process_id><areas type="list"><item
    type="dict"><area_id type="str">10</area_id><hello_interval type="int">2</hello_interval></item></areas></item></processes></ospfv3><version type="str">7.7.1</version><os_type type="str">IOS XR</os_type><build_info type="dict"><built_by type="str">ingunawa</built_by><built_on type="str">Mon Jul 25 02:41:45 PDT 2022</built_on><built_host type="str">iox-ucs-067</built_host><workspace type="str">/auto/srcarchive12/prod/7.7.1/xrv9k/ws</workspace><location type="str">/opt/cisco/XR/packages/</location><label type="str">7.7.1-0</label></build_info><hardware type="dict"><model type="str">cisco IOS-XRv 9000</model><serial_number type="str">3B5CEE0EED4</serial_number></hardware><uptime type="dict"><weeks type="int">2</weeks><days type="int">3</days><hours type="int">4</hours><minutes type="int">52</minutes></uptime><memory type="dict"><total_mb type="str">6144M</total_mb><free_mb type="str">3560M</free_mb></memory><memory_summary type="dict"><image_size type="str">4M</image_size></memory_summary><device_name
    type="str">iosxr</device_name><license type="dict"><status type="str">EVAL MODE</status><name type="str">IOS-XRv-9000-vRouter-VM</name><count type="int">1</count><version type="float">1.0</version><export_status type="str">NOT RESTRICTED</export_status></license><ansible_network_os type="str">cisco.iosxr.iosxr</ansible_network_os></facts>
```
## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information

- Ansible Network Content Team
