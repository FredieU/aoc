#! /usr/bin/python3
import sys, datetime, re

def get_ts(line):
	regexp = r'\[\d+-\d+-\d+ \d+:\d+\]'
	match_obj = re.match(regexp, line)

	try:
		date_str = match_obj[0].strip('[]')
		ts = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')
		return ts
	except TypeError:
		return None

def get_guard_id(line):
	regexp = r'Guard'
	print(regexp, line)
	match_obj = re.match(regexp, line)

	try:
		ID = match_obj[0].strip('#')
		return ID
	except TypeError:
		return None


for line in sys.stdin:
	ID = get_guard_id(line)
	ts = get_ts(line)
	print(ts,ID)