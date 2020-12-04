import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 's3cmd'
PACKAGE_BINARY = '/usr/local/bin/s3cmd'


def test_s3cmd_binary_exists(host):
    """
    Tests if s3cmd binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_s3cmd_binary_file(host):
    """
    Tests if s3cmd binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_s3cmd_binary_which(host):
    """
    Tests the output to confirm s3cmd's binary location.
    """
    assert host.check_output('which s3cmd') == PACKAGE_BINARY
