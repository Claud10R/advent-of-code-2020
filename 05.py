def read_input():
	list = []
	with open('05.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))
	
	return list

# Find the boarding passes' IDs by determining its row and column (id = row * 8 + column). Each row of the input
# identifies a specific seat. The 10 characters are so distributed:
# - 1-7 is either F or B. Rows are in range [0,127], each F means take the lower half, each B the upper half
# - 8-10 is either R or L. Columns are in range [0,7], R means upper half, L lower half
# e.g. FBFBBFFRLR -> row 44, column 5
# Output the max id
def day05(input_list: list):
	max_id = 0

	for line in input_list:
		id = line2id(line)
		max_id = max(id, max_id)

	print(max_id)

def line2id(line: str):
	line_binary = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
	line_int = int(line_binary, 2)
	return line_int

# Find the missing boarding pass ID, which is not at the very front, nor at the very back. Some IDs don't exist at all.
# Boarding passes with ID+1 and ID-1 exist for the missing ID.
def day05_2(input_list: list):
	ids = []

	for line in input_list:
		id = line2id(line)
		ids.append(id)
	
	ids.sort()
	
	for i in range(0, len(ids) - 1):
		if ids[i+1] == ids[i] + 2:
			print(ids[i] + 1)
			return

if __name__ == '__main__':
	input_list = read_input()
	day05(input_list)
	day05_2(input_list)