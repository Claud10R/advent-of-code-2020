def read_input():
	list = []
	with open('02.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))
	
	return list

# Line example: 1-2 d: pdhd
# - pdhd is the password to inspect, 'd' is the character to find
# - 1-2 are the min and max number of occurrences allowed for the character in the password
# Find the number of passwords which comply to their policies
def day02(input_list):
	psw_ok = 0

	for line in input_list:
		splitted_line = line.split()
		thresholds = splitted_line[0].split("-")
		char2find = splitted_line[1].replace(":","")
		psw = splitted_line[2]

		occurs = count_occurrences(psw, char2find)
		if occurs >= int(thresholds[0]) and occurs <= int(thresholds[1]):
			psw_ok += 1

	print(psw_ok)

def count_occurrences(password, char2find):
	cnt = 0
	
	for char in password:
		if char == char2find:
			cnt += 1

	return cnt


# Line example: 1-2 d: pdhd
# - pdhd is the password to inspect, 'd' is the character to find
# - 1-2 are the positions in the password where exactly one occurrence of the character needs
#   to be
# Find the number of passwords which comply to their policies
def day02_2(input_list):
	psw_ok = 0

	for line in input_list:
		splitted_line = line.split()
		positions = splitted_line[0].split("-")
		char2find = splitted_line[1].replace(":","")
		psw = splitted_line[2]

		if check_positions(psw, int(positions[0]), int(positions[1]), char2find):
			psw_ok += 1

	print(psw_ok)

def check_positions(password, pos1, pos2, char2find):
	if password[pos1-1] == char2find and password[pos2-1] != char2find:
		return True

	if password[pos1-1] != char2find and password[pos2-1] == char2find:
		return True

	return False

if __name__ == '__main__':
	input_list = read_input()
	day02(input_list)
	day02_2(input_list)