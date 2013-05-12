#!/usr/bin/python
# encoding: utf-8
"""
resolver.py

Created by Lou Mauget on 2013-05-11.
MIT License
Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com
"""

import socket

# Resolve DNS name to IP address
def get_ip_address(p):
	ipaddr = socket.gethostbyname(p.dns_name) 
	return ipaddr
