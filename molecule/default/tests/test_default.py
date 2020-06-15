import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_s3cmd_binary_exists(host):
    assert host.file('/usr/local/bin/s3cmd').exists


def test_s3cmd_binary_file(host):
    assert host.file('/usr/local/bin/s3cmd').is_file


def test_s3cmd_binary_which(host):
    assert host.check_output('which s3cmd') == '/usr/local/bin/s3cmd'
