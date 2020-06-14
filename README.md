[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-s3cmd.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-s3cmd) ![Ansible Role](https://img.shields.io/ansible/role/47495?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47495?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47495?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-s3cmd&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-s3cmd) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-s3cmd?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-s3cmd?color=orange&style=flat-square)

# Ansible Role: s3cmd

Role to install (_by default_) [s3cmd](https://github.com/gos3cmdio/s3cmd) on **Debian/Ubuntu** and **EL** systems. s3cmd is a popular s3 client.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
s3cmd_debian_pre_reqs:
  - python3
  - python3-pip
s3cmd_debian_pre_reqs_desired_state: present
s3cmd_pip_executable: pip3
s3cmd_app_debian_package: s3cmd
s3cmd_desired_state: present
```

### Variables table:

Variable                            | Value (default)      | Description
----------------------------------- | -------------------- | -----------------------------------------------------------------------------------------------------------------
s3cmd_debian_pre_reqs               | python3, python3-pip | Packages required to install **s3cmd** on Debian based systems. Using python3 as python2.x is EOL by end of 2020.
s3cmd_debian_pre_reqs_desired_state | present              | Desired state for **s3cmd** pre-requisite apps on Debian systems.
pip_executable                      | pip3                 | The executable to utilize for installing **pip** package of `s3cmd`.
s3cmd_app_debian_package            | s3cmd                | Name of s3cmd application package require to be installed i.e. `s3cmd` on Debian based systems.
s3cmd_desired_state                 | present              | Desired state for **s3cmd**.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **s3cmd**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.s3cmd
```

For customizing behavior of role (i.e. specifying the desired **s3cmd** state to uninstall) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.s3cmd
  vars:
    s3cmd_desired_state: absent
```

For customizing behavior of role (i.e. specifying the desired **s3cmd** state to install/upgrade to latest version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.s3cmd
  vars:
    s3cmd_bin_path: latest
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-s3cmd/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
