[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-s3cmd.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-s3cmd) ![Ansible Role](https://img.shields.io/ansible/role/47495?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47495?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47495?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-s3cmd&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-s3cmd) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-s3cmd?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-s3cmd?color=orange&style=flat-square)

# Ansible Role: s3cmd

Role to install (_by default_) [s3cmd](https://github.com/gos3cmdio/s3cmd) on **Debian/Ubuntu** and **EL** systems. s3cmd is a popular s3 client.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
s3cmd_app: s3cmd
s3cmd_version: 2.1.0
s3cmd_dl_url: https://github.com/s3tools/{{ s3cmd_app }}/releases/download/v{{ s3cmd_version }}/{{ s3cmd_app }}-{{ s3cmd_version }}.tar.gz
s3cmd_bin_path: /usr/local/bin
```

### Variables table:

Variable       | Value (default)                                                                                                                | Description
-------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------
s3cmd_app      | s3cmd                                                                                                                          | Defines the app to install i.e. **s3cmd**
s3cmd_version  | 2.1.0                                                                                                                          | Defined to dynamically fetch the desired version to install. Defaults to: **0.72.0**
s3cmd_dl_url   | <https://github.com/s3tools/{{> s3cmd_app }}/releases/download/v{{ s3cmd_version }}/{{ s3cmd_app }}-{{ s3cmd_version }}.tar.gz | Defines URL to download the s3cmd binary from.
s3cmd_bin_path | /usr/local/bin                                                                                                                 | Defined to dynamically set the appropriate path to store s3cmd binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **s3cmd**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.s3cmd
```

For customizing behavior of role (i.e. specifying the desired **s3cmd** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.s3cmd
  vars:
    s3cmd_version: 2.0.2
```

For customizing behavior of role (i.e. placing binary of **s3cmd** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.s3cmd
  vars:
    s3cmd_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-s3cmd/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
