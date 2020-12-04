import re

def read_input():
	list = []
	with open('04.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))
	
	return list

# Find the number of valid passports, those which have all the required info (cid is optional).
# Passports are separated by a blank newline.
def day04(input_list: list):
	n_valid = 0
	curr_fields = []

	for i, line in enumerate(input_list):
		if len(line) > 0:
			pairs = line.split()
			curr_fields += [pair.split(":")[0] for pair in pairs]
		
		if len(line) == 0 or i == len(input_list) - 1:
			if check_fields(curr_fields):
				n_valid += 1
			curr_fields = []

	print(n_valid)


def check_fields(curr_fields: list):
	req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

	for field in req_fields:
		if field not in curr_fields:
			return False

	return True


# Passports are now valid if they have all the required info, but all information need to be validated
def day04_2(input_list: list):
	n_valid = 0
	curr_fields = {}

	for i, line in enumerate(input_list):
		if len(line) > 0:
			pairs = line.split()
			for pair in pairs:
				splitted = pair.split(":")
				curr_fields[splitted[0]] = splitted[1]
		
		if len(line) == 0 or i == len(input_list) - 1:
			if check_and_validate_fields(curr_fields):
				n_valid += 1
			curr_fields = {}

	print(n_valid)

def check_and_validate_fields(curr_fields: dict):
	requirements = {
		'byr': {'min': 1920, 'max': 2002},
		'iyr': {'min': 2010, 'max': 2020},
		'eyr': {'min': 2020, 'max': 2030},
		'hgt': {'regex': '^[1-9]{1}[0-9]{1,2}(cm|in)$', 'min': {'cm': 150, 'in': 59}, 'max': {'cm': 193, 'in': 76}},
		'hcl': {'regex': '^#[0-9a-f]{6}$'},
		'ecl': {'val': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']},
		'pid': {'regex': '^[0-9]{9}$'}
	}

	for field, reqs in requirements.items():
		try:
			assert field in curr_fields

			if 'regex' in reqs:
				assert bool(re.match(reqs['regex'], curr_fields[field]))

			if 'val' in reqs:
				assert curr_fields[field] in reqs['val']

			if 'min' in reqs:
				if isinstance(reqs['min'], dict):
					val = int(curr_fields[field][:-2])
					mu = curr_fields[field][-2:]
					assert val >= reqs['min'][mu]
				else:
					val = int(curr_fields[field])
					assert val >= reqs['min']

			if 'max' in reqs:
				if isinstance(reqs['max'], dict):
					val = int(curr_fields[field][:-2])
					mu = curr_fields[field][-2:]
					assert val <= reqs['max'][mu]
				else:
					val = int(curr_fields[field])
					assert val <= reqs['max']
		except:
			return False

	return True

if __name__ == '__main__':
	input_list = read_input()
	day04(input_list)
	day04_2(input_list)