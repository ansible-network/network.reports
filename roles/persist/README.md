# persist

## Overview

The `persist` role enables users to fetch facts for specified network resources and store them in a YAML-formatted structure. These host variables can be saved either locally or in a remote data store, acting as a single source of truth (SOT) for network configurations.

## Features

- Fetch structured facts for specified resources.
- Persist gathered facts to local directories or remote SCM repositories.
- Enable centralized and version-controlled storage for network configuration data.

## Variables

| Variable Name        | Default Value | Required | Type | Description                                             |            Example             |
| :------------------- | :-----------: | :------: | :--: | :------------------------------------------------------ | :----------------------------: |
| `ansible_network_os` |     `""`      |    no    | str  | Network OS for which the facts are being gathered.      |       `"cisco.ios.ios"`        |
| `resources`          |    `[all]`    |    no    | list | List of resources for which facts need to be persisted. | `['interfaces', 'bgp_global']` |
| `data_store`         |     `""`      |   yes    | dict | Specifies the storage configuration (local or SCM).     |      See examples below.       |

## Usage

Below are examples demonstrating how to use the `persist` role:

### Example 1: Persist to Local Data Store

In this example, gathered facts are stored in a local directory:

```yaml
- name: persist
  hosts: all
  become: true
  tasks:
    - name: Persist report
      ansible.builtin.include_role:
        name: network.reports.persist
      vars:
        format: json
        resources:
          - "bgp_global"
          - "bgp_address_family"
        data_store:
          local: "~/data/network"
```

Example Output
When the playbook is executed, the persisted facts will be saved in the specified data store in a structured YAML format.

### Example 2: Persist to SCM repository

In this example, gathered facts are stored in a remote Git repository:

```yaml
- name: Persist network facts to SCM repository
  hosts: all
  gather_facts: true
  tasks:
    - name: Invoke persist role
      ansible.builtin.include_role:
        name: network.reports.persist
      vars:
        format: json
        data_store:
          scm:
            parent_directory: "/home/rhel"
            origin:
              url: "{{ gh_scm_url }}"
              token: "{{ gh_token }}"
              user:
                name: "{{ gh_username }}"
                email: "{{ gh_email }}"
```

Example Output
When the playbook is executed, the persisted facts will be saved in the specified data store in a structured YAML format.

- Json Output
```json
 ✝  ⚛ core_3.12.5  ~/ansible-dev-workspace  sudo cat /root/data/network/host_vars/ansible-2.yaml
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
    "device_info": [
        {
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
                "free_mb": 1510.2734375,
                "total_mb": 7945.015625,
                "used_mb": 6434.7421875
            },
            "nxos_compile_time": "11/30/2023 12:00:00 [12/14/2023 05:25:50]",
            "nxos_image_file": "bootflash:///nxos64-cs.10.4.2.F.bin",
            "os_type": "NX-OS",
            "processes": {
                "running": 2,
                "total": 898
            },
            "processor": {
                "memory": 8135696,
                "type": "Intel(R) Xeon(R) Platinum 8275CL CPU @ 3.00GHz"
            },
            "release_type": "Feature Release",
            "uptime": {
                "days": 119,
                "hours": 21,
                "minutes": 47,
                "seconds": 6
            },
            "version": "10.4(2)"
        }
    ]
}
```
## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information

- Ansible Network Content Team
