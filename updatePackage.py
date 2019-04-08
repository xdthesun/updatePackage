from pip._internal.utils.misc import get_installed_distributions
from subprocess import call
import sys


def updatePackage(args):
    for dist in get_installed_distributions():
        if dist.project_name not in args:
            call("pip install --upgrade " + dist.project_name, shell=True)


if __name__ == "__main__":
    updatePackage(sys.argv[1:])
