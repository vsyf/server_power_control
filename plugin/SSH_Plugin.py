#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 youfa <vsyfar@gmail.com>
#
# Distributed under terms of the GPLv2 license.

"""

"""

from worker import PluginBase
import paramiko

class SSH_Plugin(PluginBase):
    def __init__(self, server_ip, ssh_port, ssh_username, sudo_password, password=None, ssh_key_file=None):
        self.server_ip = server_ip
        self.ssh_port = ssh_port
        self.ssh_username = ssh_username
        self.sudo_password = sudo_password
        self.password= password
        self.ssh_key_file = ssh_key_file

    def connect(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if self.password:
                self.ssh_client.connect(self.server_ip, port=self.ssh_port, username=self.ssh_username, password=self.password)
            elif self.ssh_key_file:
                self.ssh_client.connect(self.server_ip, port=self.ssh_port, username=self.ssh_username, key_filename=self.ssh_key_file)
            else:
                raise ValueError("SSH key or key file must be provided.")
            return True
        except Exception as e:
            print(f"SSH connection error: {str(e)}")
            return False

    def is_online(self):
        if not self.connect():
            print("SSH connection failed")
            return False
        print("SSH connection online")
        self.ssh_client.close()
        return True

    # not support
    def restart(self):
        return "hard restart not support for ssh"

    # not support
    def power_on(self):
        return "power on not support for ssh"

    def sleep(self):
        if not self.connect():
            return "SSH connection error: Unable to perform soft shutdown."
        try:
            command = "echo " + self.sudo_password + " | sudo -S systemctl suspend"    
            output = self.execute_command(command)
            self.close()
            return f"Soft shutdown initiated: {output}"
        except Exception as e:
            self.close()
            return f"Error performing soft shutdown: {str(e)}"

    # not support
    def shutdown(self):
        return "hard shutdown not support for ssh"

    def soft_shutdown(self):
        if not self.connect():
            return "SSH connection error: Unable to perform soft shutdown."
        try:
            command = "shutdown -h now"  
            output = self.execute_command(command)
            self.close()
            return f"Soft shutdown initiated: {output}"
        except Exception as e:
            self.close()
            return f"Error performing soft shutdown: {str(e)}"


    def soft_restart(self):
        if not self.connect():
            return "SSH connection error: Unable to perform soft restart."
        try:
            command = "shutdown -r now"  
            output = self.execute_command(command)
            self.close()
            return f"Soft restart initiated: {output}"
        except Exception as e:
            self.close()
            return f"Error performing soft restart: {str(e)}"
