#! /usr/bin/python3

import sys

def check_id(id, check, dup):
	''' Check duplicate letters for checksum.
	Params:
		id (string) = Current ID string from input.
		check (object) = Current cumulative count of each duplicate for all IDs.
		dup [list] = Duplicates already counted for the current ID.
	Returns:
		check (object) = Current cumulative count of each duplicate for all IDs.
	'''
	for letter in id:
		letter_count = id.count(letter)
		count_key = str(letter_count)
		if count_key not in dup and letter_count > 1:
			# Create a key of the letter count or +1 if exists
			try:
				check[count_key] += 1
			except KeyError:
				check[count_key] = 1
			dup.append(count_key)
	return check

def common_letters(id_list, current_id):
	''' Find similar pair of IDs (differ by 1 character). Output the common
	letters between these.
	Params:
		id_list (list) = List of checked IDs so far from input.
		current_id (string) = Current ID from input to check against id_list.
	Returns:
		common_letters (string) = Common letters between the 2 similar IDs.
	'''
	current_id = current_id.replace('\n', '')
	# print(f'\nCurrent ID: {current_id}\nID List: {id_list}')

	for n in range(len(id_list)):
		common_letters = ''
		concat = id_list[n] + current_id

		for letter in concat:
			if concat.count(letter) == 2:
				common_letters = common_letters + letter
				concat = concat.replace(letter, '')
		if len(concat) == 2:
			print(f'Correct IDs: {id_list[n]} and {current_id}')
			id_list.append(current_id)
			return common_letters

	id_list.append(current_id)


if __name__ == "__main__":
	check = {}
	id_list = []
	
	for id in sys.stdin:
		dup = []
		count_duplicates = check_id(id, check, dup)
		letters = common_letters(id_list, id)
		if letters:
			correct_letters = letters

	print(f'\nTotal duplicates: {count_duplicates}')

	try:
		checksum = count_duplicates['2'] * count_duplicates['3']
		print(f'Checksum for \'2\' and \'3\': {checksum}')
		print(f'Common letters for correct IDs: {correct_letters}')
	except KeyError:
		print('No two/three of any letter.')
	except NameError:
		print('Correct box IDs not found.')