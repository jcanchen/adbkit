#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 打包成exe时M2Crypto需要这几个模块，所以在这里引入
import Cookie
import SocketServer
import M2Crypto
import platform
from os import path

from adb import adb_commands, sign_m2crypto


class CommandExe(object):
    def __init__(self):
        if 'Linux' in platform.system():
            rsa_path = path.expanduser('~/.android/adbkey')
        else:
            rsa_path = path.expanduser('~\\.android\\adbkey')
        signer = sign_m2crypto.M2CryptoSigner(rsa_path)
        device = adb_commands.AdbCommands()
        device.ConnectDevice(rsa_keys=[signer])
        self.device = device

    def shell(self, command):
        self.device.Shell(command)
