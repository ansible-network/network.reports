# Ansible Network Reports

[![CI](https://github.com/redhat-cop/network.reports/actions/workflows/tests.yml/badge.svg?event=schedule)](https://github.com/redhat-cop/network.reports/actions/workflows/tests.yml)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7661/badge)](https://bestpractices.coreinfrastructure.org/projects/7661)


## About

- The **Ansible Network Reports Collection** provides a platform-agnostic way to gather, generate, persist, and visualize network resource reports. 
  This collection enables users to collect network facts, convert them into structured formats (YAML, JSON), and visualize them as HTML reports using Jinja2 templates.
  
- This collection includes the following roles:

- **`gather`**: Collect comprehensive network device facts for specified resources, including hardware details, using native parsers.
- **`generate_report`**: Generate structured HTML reports from previously gathered network facts for visualization and analysis.
- **`persist`**: Store gathered network facts in YAML format to local directories or remote SCM repositories, establishing a source of truth (SOT).

- This collection can be used by **network administrators**, **system operators**, and **IT professionals** looking to monitor and manage their network infrastructure through automated reporting.

![Screenshot from 2025-02-11 17-30-19](https://github.com/user-attachments/assets/8f822ffd-519b-4cf8-915b-9c73351d46a5)

## Included content

Click on the name of a role to view its documentation:

<!--start collection content-->
### Roles

Name                                                 | Description
---------------------------------------------------- | -----------
[network.reports.gather](roles/gather/README.md)     | Collect comprehensive network device facts using native parsers.
[network.reports.generate_report](roles/generate_report/README.md) | Generate structured HTML reports from gathered network facts.
[network.reports.persist](roles/persist/README.md)       | Store gathered network facts to local or remote repositories (SCM).

<!--end collection content-->



## Requirements
- [Requires Ansible](https://github.com/redhat-cop/network.reports/blob/main/meta/runtime.yml)
- [Requires Content Collections](https://github.com/redhat-cop/network.reports/blob/main/galaxy.yml)
- [Testing Requirements](https://github.com/redhat-cop/network.reports/blob/main/test-requirements.txt)
- Users also need to include platform collections as per their requirements. The supported platform collections are:
  - [arista.eos](https://github.com/ansible-collections/arista.eos) >= v11.0.0  
  - [cisco.ios](https://github.com/ansible-collections/cisco.ios) >= v10.0.0    
  - [cisco.iosxr](https://github.com/ansible-collections/cisco.iosxr) >= v11.0.0 
  - [cisco.nxos](https://github.com/ansible-collections/cisco.nxos) >= v10.0.0

## Installation
To consume this Validated Content from Automation Hub, the following needs to be added to `ansible.cfg`:

```
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://console.redhat.com/api/automation-hub/content/validated/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<SuperSecretToken>
```

Utilize the current Token, and if the token has expired, obtain the necessary
token from the [Automation Hub Web UI](https://console.redhat.com/ansible/automation-hub/token).

With this configured, simply run the following commands:

```
ansible-galaxy collection install network.base
ansible-galaxy collection install network.reports
```

## Use Cases

This collection enables users to perform the following reporting tasks:

`Gather Network Resource Reports`
- The `gather` role enables users to collect comprehensive network device facts for specified resources (like interfaces, BGP configurations, etc.), including hardware details, using native parsers. These facts form the basis for reports and persisted data.

```yaml
- name: Gather Network Reports for specific resources
  hosts: network_devices
  gather_facts: false
  tasks:
    - name: Invoke gather role for interfaces and BGP
      ansible.builtin.include_role:
        name: network.reports.gather
      vars:
        resources:
          - interfaces
          - l2_interfaces
          - bgp_global
```
Example Output
When the playbook is executed successfully, the output will display the all_gathered_facts for the specified resources.


`Generate HTML Reports from Network Facts`
- The `generate_report` role allows users to convert previously gathered network facts into structured HTML reports using Jinja2 templates, providing a visual representation of the network state.

```yaml
- name: Generate Network HTML Report
  hosts: localhost
  gather_facts: false
  # Assumes facts were gathered previously (e.g., by the gather role)
  tasks:
    - name: Generate Report from gathered facts
      ansible.builtin.include_role:
        name: network.reports.generate_report
```
Example Output

- This task collects information from the network devices about all the resources of that device.

- After the facts have been gathered, the next task is to generate the web report. This task runs locally on the localhost. The output of the network.reports.generate_report task will produce an HTML file summarizing the gathered facts.

`Persist Network Data as Source of Truth (SOT)`
- The `persist` role enables users to store gathered network facts (not just reports) in YAML format to local directories or remote SCM (like GitHub/GitLab) repositories. This establishes a version-controlled source of truth for network configuration data, useful for backup, audit, or driving configuration deployment.

```yaml
- name: Persist Gathered Facts to SCM
  hosts: network_devices # Target your network devices group
  gather_facts: false
  # Assumes facts were gathered previously (e.g., by the gather role)
  tasks:
    - name: Persist Facts to GitHub Repository
      ansible.builtin.include_role:
        name: network.reports.persist
      vars:
        data_store:
          scm:
            parent_directory: "/tmp/network_reports_repo" 
            origin:
              url: "{{ github_repo_url }}" 
              token: "{{ github_access_token }}"
              user:
                name: "{{ git_user_name }}"
                email: "{{ git_user_email }}"
```
Example Output When the playbook is executed, the persisted facts will be saved in the specified data store in a structured YAML format.

## Testing

The project uses **tox** to run `ansible-lint` and `ansible-test sanity`. Assuming this repository is checked out in the proper structure, e.g., `collections_root/ansible_collections/network/reports`, run:

```shell
  tox -e ansible-lint
  tox -e py39-sanity
```

To run integration tests, ensure that your inventory has a `network_reports` group.

```ini
[network_devices]
ios
junos

[ios:vars]
< enter inventory details for IOS devices >

[junos:vars]
< enter inventory details for Junos devices >
```

```shell
  ansible-test network-integration -i /path/to/inventory --python 3.9 [target]
```

## Contributing

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against this repository.

Don't know how to start? Refer to the [Ansible community guide](https://docs.ansible.com/ansible/devel/community/index.html)!

Want to submit code changes? Take a look at the [Quick-start development guide](https://docs.ansible.com/ansible/devel/community/create_pr_quick_start.html).

We also use the following guidelines:

* [Collection review checklist](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_reviewing.html)
* [Ansible development guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
* [Ansible collection development guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections)

### Code of Conduct
This collection follows the Ansible project's [Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html). Please read and familiarize yourself with this document.

## Release Notes

Release notes are available [here](https://github.com/redhat-cop/network.reports/blob/main/CHANGELOG.rst).

## Related Information

- [Developing network resource modules](https://github.com/ansible-network/networking-docs/blob/main/rm_dev_guide.md)
- [Ansible Networking docs](https://github.com/ansible-network/networking-docs)
- [Ansible Collection Overview](https://github.com/ansible-collections/overview)
- [Ansible Roles overview](https://docs.ansible.com/ansible/2.9/user_guide/playbooks_reuse_roles.html)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community Code of Conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
