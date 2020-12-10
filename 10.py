def read_input():
	list = []
	with open('10.txt', 'r') as file:
		for line in file:
			list.append(int(line.replace("\n","")))

	return list

# Find the number of 1-differences and 3-differences between ordered numbers. Return the product between those.
def day10(input: list):
	differences = {1: 0, 2: 0, 3: 0}

	for i in range(0, len(input) - 1):
		if abs(input[i] - input[i+1]) > 3:
			print("Error")
			return

		differences[abs(input[i] - input[i+1])] += 1

	print(differences[1]*differences[3])

# Find the total number of valid combinations, obtained by removing 1 or more number from the sequence.
# A combination is valid iff the difference between two consecutive numbers is 3 at max
def day10_2(input: list):
	unnecessary = {}

	for i in range(1, len(input) - 1):
		if abs(input[i-1]-input[i+1]) <= 3:
			unnecessary[input[i]] = i

	run = []
	combs = 1
	for x in unnecessary:
		if len(run) == 0 or abs(run[-1] - x) == 1:
			run.append(x)
		else:
			combs *= run_to_combs(run)
			run = [x]
	
	combs *= run_to_combs(run)
	print(combs)

def run_to_combs(run: list):
	factor = 2 ** len(run)
	if len(run) >= 3:
		factor -= 1

	return factor

if __name__ == '__main__':
	input_list = read_input()
	input_list.sort()
	input_list = [0] + input_list + [input_list[-1] + 3]
	
	day10(input_list)
	day10_2(input_list)
