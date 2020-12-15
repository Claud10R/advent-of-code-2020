def read_input():
	list = []
	with open('15.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))

	return list

def parse_input(input: list):
	memory = {}
	splitted = input[0].split(",")

	for i, num in enumerate(splitted):
		memory[int(num)] = int(i+1)

	return memory, int(splitted[-1])

def get_ith_number(memory: dict, latest: int, i: int):
	turn = len(memory) + 1
	n = latest

	while turn <= i:
		if n not in memory:
			memory[n] = turn - 1
			n = 0
		else:
			latest = memory[n]
			new_latest = turn - 1
			memory[n] = new_latest
			n = new_latest - latest

		turn += 1

	return n

# Given a start condition for Van Eck's sequence, determine the 2020th number
def day15(memory: dict, latest: int):
	x = get_ith_number(memory, latest, 2020)
	print(x)

# Given the same start condition, determine the 30000000th number
def day15_2(memory: dict, latest: int):
	x = get_ith_number(memory, latest, 30000000)
	print(x)

if __name__ == '__main__':
	input = read_input()
	memory, latest = parse_input(input)

	day15(memory.copy(), latest)
	day15_2(memory.copy(), latest)