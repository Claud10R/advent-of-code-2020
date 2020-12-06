def read_input():
	list = []
	with open('06.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))
	
	return list

# Given some chars for each group of rows (separated by newline), find the total number of characters appearing.
# Duplicates have to be counted once only.
def day06(input_list: list):
	count = 0
	curr_sets = []

	for line in input_list:
		if len(line) == 0:
			count += len(sets_union(curr_sets))
			curr_sets = []
		else:
			curr_set = set()
			for char in line:
				curr_set.add(char)
			curr_sets.append(curr_set)

	count += len(sets_union(curr_sets))
	print(count)

def sets_union(sets: list):
	res = sets[0]

	for curr_set in sets[1:]:
		res = res.union(curr_set)

	return res

# Count the total number of characters appearing in all rows of each group
def day06_2(input_list: list):
	count = 0
	curr_sets = []

	for line in input_list:
		if len(line) == 0:
			count += len(sets_intersect(curr_sets))
			curr_sets = []
		else:
			curr_set = set()
			for char in line:
				curr_set.add(char)
			curr_sets.append(curr_set)

	count += len(sets_intersect(curr_sets))
	print(count)

def sets_intersect(sets: list):
	res = sets[0]

	for curr_set in sets[1:]:
		res = res.intersection(curr_set)

	return res

if __name__ == '__main__':
	input_list = read_input()
	day06(input_list)
	day06_2(input_list)