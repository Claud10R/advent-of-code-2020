def read_input():
	list = []
	with open('03.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))
	
	return list

# Starting top left of the input, moving 3 right 1 down, how many trees (#) are seen? Map is circular
# I.e., how many times you end up on a position occupied by a tree?
def day03(input_list):
	m = len(input_list[0])
	x = 0

	trees_seen = 0
	for line in input_list:
		if line[x % m] == '#':
			trees_seen += 1

		x += 3

	print(trees_seen)

# Testing different sets of moves, what's the product of all the trees seen?
def day03_2(input_list):
	product = 1
	moves = [[1,1], [3,1], [5,1], [7,1], [1,2]]
	
	for move in moves:
		product *= trees_for_move(input_list, move[0], move[1])

	print(product)

def trees_for_move(input_list, x_move, y_move):
	n = len(input_list)
	m = len(input_list[0])
	x = y = 0
	trees_seen = 0

	while y < n:
		line = input_list[y]
		pos = line[x % m]

		if pos == '#':
			trees_seen += 1

		x += x_move
		y += y_move

	print("[", x_move, ", ", y_move, "] -> ", trees_seen, sep = "")
	return trees_seen

if __name__ == '__main__':
	input_list = read_input()
	day03(input_list)
	day03_2(input_list)