# Generate HTML Reports from Network Facts

## Overview

The `generate_report` role allows users to generate HTML reports based on collected network device facts. This role parses the gathered facts and presents them in a visually structured HTML format.

## Features

- Collects and formats network facts into an HTML report.
- Supports various network operating systems like Cisco, Arista, and more.
- Ensures network devices remain compliant with the intended configuration.

## Variables

| Variable Name        | Default Value | Required | Type | Description                                       |          Example          |
| :------------------- | :-----------: | :------: | :--: | :------------------------------------------------ | :-----------------------: |
| `ansible_network_os` |     `""`      |    no    | str  | Network OS to be used when generating the report. |     `"cisco.ios.ios"`     |
| `resources`          |    `[all]`    |    no    | list | List of resources to generate report.             | `['interfaces', 'vlans']` |

## Usage

Below are examples demonstrating how to use the `generate_web` role:

### Example 1: Generate Network Web Report

- Gathering Structured Facts for Network Resources:

This part runs on the network group of hosts and gathers structured facts specifically for bgp_address_family resources.

The include_role task uses the network.reports.gather role to gather these facts.

- Generating a Web Report:

This part runs locally on the localhost and generates the web report using the network.reports.generate_report role.

The become: true ensures that necessary privileges are granted if required on the local machine when generating the report.

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
          - "all"

- name: generate WEB report
  hosts: localhost
  become: true
  tasks:
    - name: Generate report
      ansible.builtin.include_role:
        name: network.reports.generate_report
```

Example Output

- This task collects information from the network devices about all the resources of that device.

- After the facts have been gathered, the next task is to generate the web report. This task runs locally on the localhost. The output of the network.reports.generate_report task will produce an HTML file summarizing the gathered facts.

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information

- Ansible Network Content Team
