#! /usr/bin/python3

import sys, json, time

def parse_fabric(claim):
	''' Parse the claim string containing details about the rectangle section 
			of fabric.
	Params:
		claim (string) = String in the format of "#ID @ X,Y: WxH".
	Returns:
		fabric_specs (object) = Object containing fabric info and dimensions:
		- 'id': ID of the claim
		- 'x': Offset from the left edge of the fabric in inches.
		- 'y': Offset from the top edge of the fabric in inches.
		- 'w': Width of the rectangle in inches.
		- 'h': Height of the rectangle in inches.
	'''
	# Strip new line chars from stdin.
	claim = claim.replace('\n', '')
	# Split string by whitespace for the relevant parts
	parts = claim.split(' ')
	# Init empty dict
	fabric_specs = {}

	# ID
	fabric_specs['id'] = int(parts[0].replace('#', ''))

	# Offsets
	offset = parts[2].split(',')
	fabric_specs['x_offset'] = int(offset[0])
	fabric_specs['y_offset'] = int(offset[1].replace(':', ''))

	# Dimensions
	dimensions = parts[3].split('x')
	fabric_specs['width'] = int(dimensions[0])
	fabric_specs['height'] = int(dimensions[1])

	return fabric_specs

def blank_fabric(total_width, total_height):
	fabric = []

	for h in range(total_height):
		fabric.append([])
		for w in range(total_width):
			fabric[h].append('.')

	return fabric

def draw_fabric(fabric, fabric_specs):
	id_list = []
	for spec in fabric_specs:
		id = str(spec['id'])
		id_list.append(id)
		x = spec['x_offset']
		y = spec['y_offset']
		w = spec['width']
		h = spec['height']
	
		for height in range(y + h):
			height += 1
			for width in range(x + w):
				width += 1
				if height > y and y <= height and width > x and x <= width:
					if fabric[height-1][width-1] == '.':
						fabric[height-1][width-1] = id
					else:
						if id in id_list:
							id_list.remove(id)
						if fabric[height-1][width-1] in id_list:
							id_list.remove(fabric[height-1][width-1])
						fabric[height-1][width-1] = 'X'

	overlap_count = 0
	for row in fabric:
		# print(''.join(row))
		if 'X' in row:
			overlap_width = row.count('X')
			overlap_count += overlap_width
	return overlap_count, id_list



if __name__ == "__main__":
	width = 0
	height = 0
	all_specs = []
	for claim in sys.stdin:
		specs = parse_fabric(claim)
		if specs['x_offset'] + specs['width'] > width:
			width = specs['x_offset'] + specs['width']
		if specs['y_offset'] + specs['height'] > height:
			height = specs['y_offset'] + specs['height']
		all_specs.append(parse_fabric(claim))

	fabric = blank_fabric(
		total_width = width,
		total_height = height)

	sq_in_overlap = draw_fabric(fabric, all_specs)
	print(sq_in_overlap)