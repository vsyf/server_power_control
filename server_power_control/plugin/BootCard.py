#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 youfa <vsyfar@gmail.com>
#
# Distributed under terms of the GPLv2 license.

"""

"""

from server_power_control.worker import PluginBase
import requests
import json

cmd_boot = 1
cmd_shutdown_long = 2
cmd_shutdown_short = 3
cmd_restart = 4
cmd_current_status = 11

class BootCard(PluginBase):
    def __init__(self, server_ip):
        self.server_ip = server_ip

    # post http://ip/perform {"cmd:": action}
    def perform(self, action):
        url = "http://%s/perform" % (self.server_ip)
        message = {"cmd": action}
        print (message)
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url, headers=headers, data=json.dumps(message))
        print (res.text)
        return res

    def is_online(self):
        res = self.perform(cmd_current_status)
        if res.status_code == 200 and res.json()["errCode"] == 0:
                return True
        return False

    def restart(self):
        res = self.perform(cmd_restart)
        if res.status_code == 200 and res.json()["errCode"] == 0:
                return "restart success"
        return "restart failed"

    # not support
    def power_on(self):
        res = self.perform(cmd_boot)
        if res.status_code == 200 and res.json()["errCode"] == 0:
            return "power on success"
        return "power on failed"

    def sleep(self):
        return "BootCard not support sleep"

    # not support
    def shutdown(self):
        res = self.perform(cmd_shutdown_long)
        if res.status_code == 200 and res.json()["errCode"] == 0:
            return "shutdown success"
        return "shutdown failed"

    def soft_shutdown(self):
        return "soft shutdown not support for BootCard"

    def soft_restart(self):
        return "soft restart not support for BootCard"
