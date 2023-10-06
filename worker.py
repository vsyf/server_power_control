#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 youfa <vsyfar@gmail.com>
#
# Distributed under terms of the GPLv2 license.

"""

"""

class PluginBase:
    def is_online(self):
        raise NotImplementedError

    def restart(self):
        raise NotImplementedError

    def power_on(self):
        raise NotImplementedError

    def sleep(self):
        raise NotImplementedError

    def shutdown(self):
        raise NotImplementedError

    def soft_shutdown(self):
        raise NotImplementedError

    def soft_restart(self):
        raise NotImplementedError

class Worker:
    def __init__(self):
        self.plugins = {}  # 插件字典，用于存储插件名称和实例

    # 注册插件
    def register_plugin(self, plugin_name, plugin_instance):
        self.plugins[plugin_name] = plugin_instance

    # 动态绑定核心接口到插件的特定函数
    def bind_online_func(self, plugin):
        self.bind_core_interface_to_plugin("is_online", plugin)

    def bind_restart_func(self, plugin):
        self.bind_core_interface_to_plugin("restart", plugin)

    def bind_power_on_func(self, plugin):
        self.bind_core_interface_to_plugin("power_on", plugin)

    def bind_sleep_func(self, plugin):
        self.bind_core_interface_to_plugin("sleep", plugin)

    def bind_shutdown_func(self, plugin):
        self.bind_core_interface_to_plugin("shutdown", plugin)

    def bind_soft_shutdown_func(self, plugin):
        self.bind_core_interface_to_plugin("soft_shutdown", plugin)

    def bind_soft_restart_func(self, plugin):
        self.bind_core_interface_to_plugin("soft_restart", plugin)

    # 动态绑定核心接口到插件的指定函数
    def bind_core_interface_to_plugin(self, interface, plugin):
        if plugin not in self.plugins.values():
            raise ValueError(f"Plugin not registered.")

        if hasattr(plugin, interface):
            setattr(self, interface, getattr(plugin, interface))
        else:
            raise ValueError(f"Plugin does not implement the '{interface}' method.")

    def is_online(self):
        return "is_online not implemented."

    def restart(self):
        return "restart not implemented."

    def power_on(self):
        return "power_on not implemented."

    def sleep(self):
        return " sleep not implemented."

    def shutdown(self):
        return "shutdown not implemented."

    def soft_shutdown(self):
        return "soft_shutdown not implemented."

    def soft_restart(self):
        return "soft_restart not implemented."
