#!/usr/bin/python3
# encoding: utf-8
"""
props.py

Created by Lou Mauget on 2013-05-17.
MIT License
Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com

Rename file to props.py and set values for your environment
"""

import logging

# Target DNS
dns_name = ['DNS name to be monitored', 'somedns.org', 'somedns.com']

# Interval in seconds; loop continuation is do_run value; Forever is True
interval = 60*30
do_run = True

# Notify even if IP didn't change
always_notify = True

# SMTP properties
smtp_server = 'your smtp server address'
smtp_port = 587
smtp_user = 'smtp user name'
smtp_password = 'smtp password'
smtp_debug_level = 1  # 1 or 0 works

# Email properties
sender = 'user@email.net'
receivers = ['sombody@someorg.org', 'somebodyelse@otherplace.com']

message_template = """From: DNS Tracker<%s>
To: Lou Mauget<mauget@mindspring.com>
MIME-Version: 1.0
Content-type: text/html
Subject: %s IP tracking

<table>
<tr><th>DNS name</th><td>%s</td></tr>
<tr><th>IP Change</th><td>%s</td></tr>
<tr><th>Current IP</th><td>%s</td></tr>
<tr><th>Cached IP</th><td>%s</td></tr>
</table>
<p>
From DNS IP Checker
</p>
"""

message_template_txt = """
From: DNS Tracker %s
Subject: %s IP tracking
DNS name: %s
IP change: %s
Current IP: %s
Cached IP: %s
"""

# Tracking file name and location
tracker_file = 'tracker_file_%s.txt'

# Logging parameters

# logging_level = logging.WARN
# logging_level = logging.INFO
# logging_level = logging.DEBUG
# logging_level = logging.ERROR
# logging_level = logging.CRITICAL
logging_level = logging.INFO

logging_file = 'ipchecker.log'

