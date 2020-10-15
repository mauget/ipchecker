#!/usr/bin/python3
# encoding: utf-8
"""
emailer.py

Created by Lou Mauget on 2013-05-11.
MIT License
Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com
"""

import logging
import smtplib


def send(p, dns_nm, cur_ipaddr, old_ipaddr):
    is_changed = cur_ipaddr != old_ipaddr
    txt_msg = p.message_template_txt % tuple([p.sender, dns_nm, dns_nm, is_changed, cur_ipaddr, old_ipaddr])
    print(txt_msg)

    # htmlMsg = p.message_template % tuple([p.sender, dns_nm, dns_nm, is_changed, cur_ipaddr, old_ipaddr])

    # smtpObj = smtplib.SMTP(p.smtp_server, p.smtp_port)
    # smtpObj.set_debuglevel(p.smtp_debug_level)
    # smtpObj.login(p.smtp_user, p.smtp_password)
    # smtpObj.sendmail(p.sender, p.receivers, htmlMsg)

    print("TURNED OFF: Emailed IP information about " + dns_nm)
    logging.info("TURNED OFF: Emailed IP information about " + dns_nm)
