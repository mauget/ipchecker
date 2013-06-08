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
import logging

def main(p):
	logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p', filename=p.logging_file, level=p.logging_level)
	logging.info('ipchecker started')
	
	do_run = True
	while do_run:
		ipaddr = resolver.get_ip_address(p)
		print("Current IP '" + ipaddr + "'")
		
		old_ipaddr = tracker.get_tracker_value(p, ipaddr)
		print("Cached IP '" + old_ipaddr + "'")
		
		logging.info('Resolved "%s". Current IP "%s". Cached IP "%s"', p.dns_name, ipaddr, old_ipaddr)

		if old_ipaddr != ipaddr or p.always_notify:
			emailer.send(p, ipaddr, old_ipaddr)
			print("Sent email")

		do_run = p.do_run
		time.sleep(p.interval)
		
		logging.info('Awakened')
		
main(props)
