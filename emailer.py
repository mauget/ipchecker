#!/usr/bin/python
# encoding: utf-8
"""
emailer.py

Created by Lou Mauget on 2013-05-11.
MIT License
Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com
"""

import logging

import smtplib
	
def send(p, cur_ipaddr, old_ipaddr):
	is_changed = cur_ipaddr != old_ipaddr
	msg = p.message_template % tuple([p.sender, p.dns_name, is_changed, cur_ipaddr, old_ipaddr])
	
	smtpObj = smtplib.SMTP(p.smtp_server, p.smtp_port)
	smtpObj.set_debuglevel(p.smtp_debug_level)
	smtpObj.login(p.smtp_user, p.smtp_password)
	smtpObj.sendmail(p.sender, p.receivers, msg) 
       
	print "Successfully sent email"
	logging.info("Successfully sent email")
	
