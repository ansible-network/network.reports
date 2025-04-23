# Ansible Network Reports

[![CI](https://github.com/redhat-cop/network.reports/actions/workflows/tests.yml/badge.svg?event=schedule)](https://github.com/redhat-cop/network.reports/actions/workflows/tests.yml)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7661/badge)](https://bestpractices.coreinfrastructure.org/projects/7661)


## About

- The **Ansible Network Reports Collection** provides a platform-agnostic way to gather, generate, persist, and visualize network resource reports. 
  This collection enables users to collect network facts, convert them into structured formats (YAML, JSON), and visualize them as HTML reports using Jinja2 templates.

- This collection can be used by **network administrators**, **system operators**, and **IT professionals** looking to monitor and manage their network infrastructure through automated reporting.

![Screenshot from 2025-02-11 17-30-19](https://github.com/user-attachments/assets/8f822ffd-519b-4cf8-915b-9c73351d46a5)

These playbooks demonstrate how to use the three roles you requested:

- gather: Collects network facts and configuration from devices and also allows you to specify which resource modules to gather

- persist:Saves gathered network facts and configurations to various storage backends and also supports local filesystem and Git repositories.

- generate_web_report:Creates interactive web reports from gathered network data


## Requirements
- [Requires Ansible](https://github.com/redhat-cop/network.reports/blob/main/meta/runtime.yml)
- [Requires Content Collections](https://github.com/redhat-cop/network.reports/blob/main/galaxy.yml)
- [Testing Requirements](https://github.com/redhat-cop/network.reports/blob/main/test-requirements.txt)
- Users also need to include platform collections as per their requirements. The supported platform collections are:
  - [arista.eos](https://github.com/ansible-collections/arista.eos)
  - [cisco.ios](https://github.com/ansible-collections/cisco.ios)
  - [cisco.iosxr](https://github.com/ansible-collections/cisco.iosxr)
  - [cisco.nxos](https://github.com/ansible-collections/cisco.nxos)
  - [junipernetworks.junos](https://github.com/ansible-collections/junipernetworks.junos)

## Included content

Click on the name of a role to view its documentation:

<!--start collection content-->
### Roles
Name | Description
--- | ---
[network.reports.gather](https://github.com/ansible-network/network.reports/tree/main/roles/gather) | For collecting structured facts and configurations.
[network.reports.generate_web_report](roles/configure/README.md) | For creating web-based reports from the data.
[network.reports.persist](https://github.com/AAYUSH2091/network.reports/blob/patch-1/roles/persist/README.md) | For saving and versioning the collected data
<!--end collection content-->

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

### 1. Gather Network Resource Reports
- Collect network resource facts like interfaces, BGP configurations, OSPF settings, etc.
- Convert these facts into **YAML**, **JSON**, or **HTML** formats.

```yaml
- name: Gather Network Reports
  hosts: network_devices
  gather_facts: false
  tasks:
    - name: Network Resource Manager
      ansible.builtin.include_role:
        name: network.reports.gather
      vars:
        resources:
          - interfaces
          - l2_interfaces
          - bgp_global
```
#### Example playbook for using network.reports.gather role
```yaml
- name: Gather network resources 
  hosts: network_devices
  gather_facts: false
  tasks:
    - name: Collect network resource facts
      ansible.builtin.include_role:
        name: network.reports.gather
      vars:
        resources:
          - interfaces
          - bgp_global
          - l2_interfaces
```
This playbook:

- Runs the gather role against network_devices
- Collects facts for interfaces, BGP global configuration, and L2 interfaces
- Outputs the data in both YAML and JSON formats
- Displays the gathered interface and BGP information for verification

### 2. Generate HTML Reports from Network Facts
- Convert collected facts into **HTML web reports** using Jinja2 templates.
- Run a lightweight **web server** to visualize the reports.

```yaml
- name: Generate Network HTML Report
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Generate Network Report
      ansible.builtin.include_role:
        name: network.reports.generate_web_report
```
#### Example playbook for using network.reports.generate_web_report
```yaml
- name: generate web network reports
  hosts: localhost
  become: true
  vars:
    all_gathered_facts: "{{ hostvars['ansible-1'] | default({}) }}"
  tasks:
   - name: Generate Network Report
      ansible.builtin.include_role:
        name: network.reports.generate_web_report
```
This playbook:

- Runs on localhost (since it's generating the report locally)
- Uses become: true to ensure proper permissions for file operations
- Pulls the network facts from a previous gather operation stored in hostvars
- Customizes the report location and web port
- Displays the gathered facts for verification before generating the report
- Calls the generate_web_report role with custom title, description, and sections
  
### 3. Persist Network Reports to SCM (GitHub/GitLab)
- Persist generated reports into **GitHub** or **GitLab** repositories for version control and audit.

```yaml
- name: Persist Reports to GitHub
  hosts: network_devices
  gather_facts: false
  tasks:
    - name: Persist Reports to GitHub Repository
      ansible.builtin.include_role:
        name: network.reports.persist
      vars:
        scm:
          origin:
            url: "{{ github_repo_url }}"
            token: "{{ github_access_token }}"
            user:
              name: "{{ git_user_name }}"
              email: "{{ git_user_email }}"
```
#### Example playbook for using network.reports.persist
```yaml
- name: persist
  hosts: ansible-1
  become: true
  tasks:
    - name: Persist report
      ansible.builtin.include_role:
        name: network.reports.persist
```
This playbook:
  - First gathers the network resources using the gather role
  - Then persists the gathered information using the persist role
  - Specifies both local file storage and SCM repository details

## Testing

The project uses **tox** to run `ansible-lint` and `ansible-test sanity`. Assuming this repository is checked out in the proper structure, e.g., `collections_root/ansible_collections/network/reports`, run:

```shell
  tox -e ansible-lint
  tox -e py39-sanity
```

To run integration tests, ensure that your inventory has a `network_reports` group.

```shell
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

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
