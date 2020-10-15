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

def process(p, dns_nm):
	ipaddr = resolver.get_ip_address(dns_nm)
	print(dns_nm + "current IP '" + ipaddr + "'")
	
	tracker_fn = p.tracker_file % tuple([dns_nm])
	old_ipaddr = tracker.get_tracker_value(tracker_fn, ipaddr)
	print(dns_nm + "cached IP '" + old_ipaddr + "'")
	
	logging.info('Resolved "%s". Current IP "%s". Cached IP "%s"', dns_nm, ipaddr, old_ipaddr)

	if old_ipaddr != ipaddr or p.always_notify:
		emailer.send(p, dns_nm, ipaddr, old_ipaddr)

def main(p):
	logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p', filename=p.logging_file, level=p.logging_level)
	logging.info('ipchecker started')
	
	do_run = True
	while do_run:
		
		for dns_nm in p.dns_name:
			process(p, dns_nm)

		do_run = p.do_run
		time.sleep(p.interval)
		logging.info('Awakened')
		
main(props)
