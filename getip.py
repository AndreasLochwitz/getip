#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

__author__ = "Andreas Lochwitz"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "andreas_lochwitz(at)live.de"

# This Python Script runs the following command to obtain the ip Addresses of a computer:
#
# ifconfig | grep "inet " | awk '{ORS=" "; if ($2 != "127.0.0.1") print $2}'
#
# and return the result as an array
#
# See https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline for more information
#

awkProgram = '{ORS=" "; if ($2 != "127.0.0.1") print $2 }'

def getIPs():
    ifconfigProcess = Popen(['ifconfig'], stdout=PIPE)
    grepProcess = Popen(["grep", "inet "], stdin=ifconfigProcess.stdout, stdout=PIPE)
    awkProcess = Popen(["awk", awkProgram], stdin=grepProcess.stdout, stdout=PIPE)
    output = awkProcess.communicate()[0]
    output = output.decode('utf8')
    return output.strip().split(" ")

if __name__ == "__main__":
    print(getIPs())
