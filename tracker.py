#!/usr/bin/python
# encoding: utf-8
"""
tracker.py

Created by Lou Mauget on 2013-05-11.
MIT License
Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com
"""

def is_exist_tracker(p):
	try:
		with open(p.tracker_file): pass
		return True
	except IOError:
		return False
		
def write_to_tracker(p, value):
	try:
		fo = open(p.tracker_file, "w")
		fo.write(value)
		fo.close();
	except IOError:
		print "IOError writing tracker file"
		
def read_from_tracker(p):
	value = ""
	try:
		fo = open(p.tracker_file, "r")
		value = fo.read()
		fo.close();
	except IOError:
		print "IOError writing tracker file"
	return value
	
def get_tracker_value(p, cur_ipaddr):
	old_ipaddr = ''
	if is_exist_tracker(p):
		old_ipaddr = read_from_tracker(p)
	else:
		print "tracker not found"
		write_to_tracker(p, cur_ipaddr)
	return old_ipaddr
	