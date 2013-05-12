#!/usr/bin/python
# encoding: utf-8
"""
ipchecker.py

Created by Lou Mauget on 2013-05-11.
MIT License
Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com
"""
import time
import props
import emailer
import resolver
import tracker

def main(p):
	
	do_run = True
	while do_run:
		ipaddr = resolver.get_ip_address(p)
		print "Current IP '" + ipaddr + "'"
		
		old_ipaddr = tracker.get_tracker_value(p, ipaddr)
		print "Cached IP '" + old_ipaddr + "'"

		if old_ipaddr != ipaddr or p.always_notify:
			emailer.send(p, ipaddr, old_ipaddr)

		do_run = p.do_run
		time.sleep(p.interval)
		
main(props)
