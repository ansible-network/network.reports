# Generate HTML Reports from Network Facts

Convert collected facts into HTML web reports using Jinja2 templates.
Run a lightweight web server to visualize the reports.

## Task example:

```
- name: Generate Network HTML Report
  hosts: network_devices
  gather_facts: false
  tasks:
    - name: Generate Network Report
      ansible.builtin.include_role:
        name: network.reports.generate_web_report
```
