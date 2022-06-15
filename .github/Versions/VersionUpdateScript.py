import os
import re

import fire

version_filepath = os.path.join('.', 'VersionFile.txt')
default_sanpshot_str="SNAPSHOT"
version_pattern = re.compile(fr'^\d+.\d+.\d+(-(DEV|RC|RELEASE|{default_sanpshot_str}))')


def get():
    with open(version_filepath, 'r') as version_file:
        version_lines = version_file.readlines()
        assert len(version_lines) == 1, 'Version file is malformed'
        version = version_lines[0]
        assert version_pattern.match(version), 'Version string is malformed'
        return version

def write_version_file(major: int, minor: int, patch: int,snapshot:str):
    version = f'{major}.{minor}.{patch}-{snapshot}'
    with open(version_filepath, 'w') as version_file:
        version_file.write(version)


def inc_patch():
    version = get()
    version_with_out_snapshot,version_snapshot=version.split('-')
    major, minor, patch = version_with_out_snapshot.split('.')
    write_version_file(major, minor, int(patch) + 1,snapshot=version_snapshot)


def inc_minor():
    version = get()
    version_with_out_snapshot, snapshot = version.split('-')
    major, minor, patch = version_with_out_snapshot.split('.')
    write_version_file(major, int(minor) + 1, patch,snapshot=version_snapshot)


def inc_major():
    version = get()
    version_with_out_snapshot, version_snapshot = version.split('-')
    major, minor, patch = version_with_out_snapshot.split('.')
    write_version_file(int(major) + 1, minor, patch,snapshot=version_snapshot)


def set_snapshot(snapshot:str):
    version = get()
    version_with_out_snapshot, version_snapshot = version.split('-')
    major, minor, patch = version_with_out_snapshot.split('.')
    write_version_file(major, minor, patch,snapshot=snapshot)

def set_snapshot_dev():
    set_snapshot(snapshot='DEV')
def set_snapshot_release():
    set_snapshot(snapshot='RELEASE')
def set_snapshot_rc():
    set_snapshot(snapshot='RC')
def set_snapshot_snapshot():
    set_snapshot(snapshot='SNAPSHOT')

if __name__ == "__main__":
    fire.Fire({
        'get': get,
        'inc-patch': inc_patch,
        'inc-minor': inc_minor,
        'inc-major': inc_major,
        'set_snapshot_dev': set_snapshot_dev,
        'set_snapshot_release': set_snapshot_release,
        'set_snapshot_snapshot': set_snapshot_snapshot,
        'set_snapshot_rc': set_snapshot_rc,
    })