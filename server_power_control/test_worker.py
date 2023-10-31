#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 youfa <vsyfar@gmail.com>
#
# Distributed under terms of the GPLv2 license.

"""

"""

from worker import Worker
from plugin.SSH_Plugin import SSH_Plugin

if __name__ == "__main__":
    worker = Worker()

    ssh = SSH_Plugin("192.168.253.149", 22,"root", "sudo_password", "password")
    worker.register_plugin("ssh",ssh)

    worker.bind_online_func(ssh)

    print(worker.is_online())
    print(worker.restart())
    print(worker.power_on())
    print(worker.sleep())
    print(worker.shutdown())
    print(worker.soft_shutdown())
    print(worker.soft_restart())
