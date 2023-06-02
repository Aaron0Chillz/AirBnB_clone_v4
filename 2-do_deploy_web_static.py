#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""


from fabric.api import local
from datetime import datetime

from fabric.decorators import runs_once


@runs_once
def do_pack():
    '''generates .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return None
    return path

