#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: anzhang28@163.com
# FileName: ping_check.py
# Function: 检查 host 网络是否连通
# Date: 2018/04/04

import threading
import os
import sys
import re
#from multiprocessing import Process

_PLAT = sys.platform
ping_command = None
lpattern = None
if _PLAT == 'win32':
    ping_command = 'ping -n 4 -w 1 '
    lpattern = re.compile('(?:丢失|lost) = (\d+) ')
elif _PLAT == 'linux2':
    ping_command = 'ping -c 4 -i 0 '
    lpattern = re.compile('(\d+)% packet loss')


def ping(host):
    global ping_command
    if ping_command:
        command = ping_command + str(host)
        return os.popen(command).read()
    else:
        return None


def check_ping(host):
    res = ping(host)
    global lpattern
    if lpattern:
        lost = re.search(lpattern, res).group(1)
        if lost is '0':
            print('%s UP' % host)
            return True
        else:
            print('%s DOWN' % host)
            return False
    else:
        return None


if __name__ == '__main__':
    with open('host.txt') as f:
        for h in f.readlines():
            # p = Process(target=check_ping, args=(h.strip(),))
            # p.start()
            # p.join()
            t = threading.Thread(target=check_ping, args=(h.strip(),))
            t.start()
            # t.join()
