import os
import re
import fire
from typing import Tuple
DEV_TYPE='dev'
RC_TYPE='rc'



version_filepath = os.path.join(os.path.dirname(__file__), 'VersionFile.txt')
version_pattern = re.compile(fr'^\d+.\d+.(({DEV_TYPE}|.{RC_TYPE}))\d+')
version_split_snepshot_pattern=f".{DEV_TYPE}|{RC_TYPE}"

def get_version():
    with open(version_filepath, 'r') as version_file:
        version_lines = version_file.readlines()
        assert len(version_lines) == 1, 'Version file is malformed'
        version = version_lines[0]
        assert version_pattern.match(version), 'Version string is malformed'
        return version

def write_version_file(major: int, minor: int, patch: int,version_type:str):
    version = f'{major}.{minor}.{version_type}{patch}'
    with open(version_filepath, 'w') as version_file:
        version_file.write(version)



def inc_patch():
    parsed, major, minor, patch, version_type = split_version()
    if (parsed):
        write_version_file(major=major, minor=minor, patch=(int(patch) + 1),version_type=version_type)

def inc_minor():
    parsed, major, minor, patch, version_type = split_version()
    if (parsed):
        write_version_file(major=major, minor=(int(minor) + 1), patch=1, version_type=version_type)

def inc_major():
    parsed, major, minor, patch, version_type = split_version()
    if (parsed):
        write_version_file(major=(int(major) + 1), minor=0, patch=1, version_type=version_type)

def get_release_branch_name()->str:
    parsed, major, minor, patch, version_type = split_version()
    if (parsed):
        return  f"release/{major}.{minor}"
    return ""
def create_initial_version_for_release():
    parsed, major, minor, patch, version_type = split_version()
    if (parsed):
        write_version_file(major=major, minor=minor, patch=1, version_type=RC_TYPE)

def get_merge_rc_tag_name()->str:
    parsed,major, minor,patch,version_type =split_version()
    if(parsed):
        return f"{major}.{minor}.{patch}"
    return ""

def split_version()->Tuple[bool,int,int,int,str]:
    try:
        version = get_version()
        split_items = re.split(version_split_snepshot_pattern, version, maxsplit=2)
        patch = split_items[1]
        major, minor = split_items[0].split('.')
        version_type = re.findall(version_split_snepshot_pattern, version)[0].replace(".","")
        return (True,int(major),int(minor),int(patch),version_type)
    except Exception as ex:
        print(f"failed parse version with {ex}")
        return (False,0,0,0,"")


if __name__ == "__main__":
    fire.Fire({
        'get_version': get_version,
        'inc_patch': inc_patch,
        'inc-minor': inc_minor,
        'inc-major': inc_major,
        'get_release_branch_name': get_release_branch_name,
        'create_initial_version_for_release':create_initial_version_for_release,
        'get_merge_rc_tag_name': get_merge_rc_tag_name
    })
