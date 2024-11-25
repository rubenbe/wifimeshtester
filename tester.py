#!/usr/bin/env python3

import subprocess
from time import sleep

import nmcli
from termcolor import cprint
import yaml

data_loaded = {}
with open("apnames.yaml") as stream:
    try:
        data_loaded = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        pass

mac_lookup = {}
max_ap_name_length = len("unknown")
for ap, macs in data_loaded.items():
    max_ap_name_length = max(max_ap_name_length, len(ap))
    for mac in macs:
        mac_lookup[mac] = ap


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Building the command. Ex: "ping -c 1 google.com"
    command = ["ping", "-W", "1", "-c", "1", host]

    return (
        subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        == 0
    )


def getnamestr(bssid):
    return mac_lookup.get(bssid, "unknown").ljust(max_ap_name_length)


nmcli.disable_use_sudo()
print("bssid", "freq", "signal", "rate")
while True:
    for x in [x for x in nmcli.device.wifi() if x.in_use]:
        print(
            x.bssid, getnamestr(x.bssid), x.freq, x.signal, x.rate, x.security, end=" "
        )
        if ping("8.8.8.8"):
            cprint(" OK ", "green")
            sleep(1)
        else:
            cprint("FAIL", "red")
