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
	curr_answers = {}

	for line in input_list:
		if len(line) == 0:
			count += len(curr_answers)
			curr_answers = {}
		else:
			for char in line:
				curr_answers[char] = 1

	count += len(curr_answers)
	print(count)

# Count the total number of characters appearing in all rows of each group
def day06_2(input_list: list):
	count = 0
	curr_answers = {}
	curr_rows = 0

	for line in input_list:
		if len(line) == 0:
			count += count_correct_occurrences(curr_answers, curr_rows)
			curr_rows = 0
			curr_answers = {}
		else:
			for char in line:
				curr_answers[char] = 1 if char not in curr_answers else curr_answers[char] + 1
			curr_rows += 1

	count += count_correct_occurrences(curr_answers, curr_rows)
	print(count)

def count_correct_occurrences(answers: dict, expected_val: int):
	count = 0
	for _, val in answers.items():
		if val == expected_val:
			count += 1
	return count

if __name__ == '__main__':
	input_list = read_input()
	day06(input_list)
	day06_2(input_list)