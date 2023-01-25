#!/usr/bin/python3
""" fabfile that deletes out of date files in servers"""

import os
from fabric.api import *

env.hosts = ["54.82.178.149", "54.160.78.46"]


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number: if 0 or 1, keeps the most recent file
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
