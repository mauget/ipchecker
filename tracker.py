#!/usr/bin/python
# encoding: utf-8
"""
tracker.py

Created by Lou Mauget on 2013-05-11.
MIT License
Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com
"""

import logging

def is_exist_tracker(fn):
	try:
		with open(fn): pass
		return True
	except IOError:
		return False
		
def write_to_tracker(fn, value):
	try:
		fo = open(fn, "w")
		fo.write(value)
		fo.close();
	except IOError:
		print("IOError writing tracker file " + fn)
		logging.error("IOError writing tracker file " + fn)
		
def read_from_tracker(fn):
	value = ""
	try:
		fo = open(fn, "r")
		value = fo.read()
		fo.close();
	except IOError:
		print("IOError reading tracker file " + fn)
		logging.error("IOError reading tracker file " + fn)
	return value
	
def get_tracker_value(fn, cur_ipaddr):
	old_ipaddr = ''
	
	if is_exist_tracker(fn):
		old_ipaddr = read_from_tracker(fn)
	else:
		print("Tracker file not found " + fn)
		logging.info("Tracker file not found " + fn)
		
	write_to_tracker(fn, cur_ipaddr)
	return old_ipaddr
	