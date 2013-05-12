#!/usr/bin/python
# encoding: utf-8
"""
props.py

Created by Lou Mauget on 2013-05-11.
MIT License
Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com

Rename file to props.py and set values for your environment
"""
# Target DNS
dns_name = 'DNS name to be monitored'

# Interval in seconds; loop continuation is do_run value; Forever is True
interval = 60*30
do_run = False

# Notify even if IP didn't change
always_notify = False

# SMTP properties
smtp_server = 'your smtp server address'
smtp_port = 587
smtp_user = 'smtp user name'
smtp_password = 'smtp password here'
smtp_debug_level = 1;  # 1 or 0 works

# Email properties
sender = 'mauget@mindspring.com'
#receivers = ['mauget@mindspring.com', 'mauget@gmail.com']
receivers = ['mauget@mindspring.com']

message_template = """From: %s
To: Somebody <sombody@someorg.org>
MIME-Version: 1.0
Content-type: text/html
Subject: DNS IP Tracking

<table>
<tr><th>DNS name</th><td>%s</td></tr>
<tr><th>IP Change</th><td>%s</td></tr>
<tr><th>Current IP</th><td>%s</td></tr>
<tr><th>Cached IP</th><td>%s</td></tr>
</table>
<p>
From DNS IP Tracker
</p>
"""
# Tracking file
tracker_file = 'tracker_file.txt'
