#!/usr/bin/python3
# encoding: utf-8
"""
resolver.py

Created by Lou Mauget on 2013-05-11.
MIT License
Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com
"""

import socket


# Resolve DNS name to IP address
def get_ip_address(dns_nm):
    ipaddr = socket.gethostbyname(dns_nm)
    return ipaddr
