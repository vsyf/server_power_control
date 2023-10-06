#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 youfa <vsyfar@gmail.com>
#
# Distributed under terms of the GPLv2 license.

"""

"""

from flask import Flask, jsonify, request, render_template
import time
from worker import Worker
from plugin.SSH_Plugin import SSH_Plugin
from plugin.BootCard import BootCard

app = Flask(__name__)
worker = Worker()
ssh = SSH_Plugin("192.168.253.149", 22,"root","sudo_password", "ssh_password")
bootcard = BootCard("192.168.253.107")
worker.register_plugin("ssh",ssh)
worker.register_plugin("bootcard",bootcard)

worker.bind_online_func(ssh)
worker.bind_soft_restart_func(ssh)
worker.bind_soft_shutdown_func(ssh)
worker.bind_sleep_func(ssh)
worker.bind_power_on_func(bootcard)
worker.bind_restart_func(bootcard)
worker.bind_shutdown_func(bootcard)

online = False

@app.route('/')
def index():
    return render_template('index.html', online=online)

@app.route('/is_online', methods=['GET'])
def is_online():
    online = worker.is_online()
    return jsonify({'online': online})

@app.route('/restart', methods=['POST'])
def restart():
    ret = worker.restart()
    return jsonify({'message': '重启命令已发送'})

@app.route('/power_on', methods=['POST'])
def power_on():
    ret = worker.power_on()
    return jsonify({'message': '开机命令已发送'})

@app.route('/sleep', methods=['POST'])
def sleep():
    ret = worker.sleep()
    return jsonify({'message': '睡眠命令已发送'})

@app.route('/shutdown', methods=['POST'])
def shutdown():
    ret = worker.shutdown()
    return jsonify({'message': '关机命令已发送'})

@app.route('/soft_shutdown', methods=['POST'])
def soft_shutdown():
    ret = worker.soft_shutdown()
    return jsonify({'message': '软关机命令已发送'})

@app.route('/soft_restart', methods=['POST'])
def soft_restart():
    ret = worker.soft_restart()
    return jsonify({'message': '软重启命令已发送'})

if __name__ == '__main__':
    app.run(debug=True)

