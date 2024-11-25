#!/usr/bin/env python3

import nmcli
import subprocess
from time import sleep
from termcolor import colored, cprint

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', "-c", '1', host]

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0

nmcli.disable_use_sudo()
print("bssid", "freq", "signal", "rate")
while True:
    for x in [x for x in nmcli.device.wifi() if x.in_use]:
        print(x.bssid, x.freq, x.signal, x.rate, x.security, end=" ")
        cprint(" OK ", "green") if ping("8.8.8.8") else cprint("FAIL", "red")
        sleep(1)
