import itertools
import time

def read_input():
	list = []
	with open('11.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))

	return list

# Given a map, where '.' -> floor, 'L' -> empty seat, '#' -> occupied seat
# At each round, an empty seat gets occupied iff no adjacent seats are occupied;
# an occupied seat is freed iff at least 4 of its adjacent seats are occupied
# Return the number of occupied seats when the system reaches stability
def day11(input: list):
	curr_map = input.copy()
	curr_occupied = 0

	while True:
		updates = False
		new_map = curr_map.copy()

		for i, line in enumerate(curr_map):
			for j, char in enumerate(line):
				if char == '.':
					continue

				adj_occupied = n_adjacent_seats_occupied(curr_map, i, j)
				
				if char == 'L' and adj_occupied == 0:
					updates = True

					new_map[i] = new_map[i][0:j] + '#' + new_map[i][j+1:]
					curr_occupied += 1
				
				if char == '#' and adj_occupied >= 4:
					updates = True
					
					new_map[i] = new_map[i][0:j] + 'L' + new_map[i][j+1:]
					curr_occupied -= 1
		
		if not updates:
			print(curr_occupied)
			return

		curr_map = new_map.copy()
	
def n_adjacent_seats_occupied(input: list, x: int, y: int):
	n_occupied = 0
	n = len(input)
	m = len(input[0])

	offsets = [-1, 0, 1]
	for i,j in itertools.product(offsets, offsets):
		if i == 0 and j == 0:
			continue

		if 0 <= x+i < n and 0 <= y+j < m:
			if input[x+i][y+j] == '#':
				n_occupied += 1

	return n_occupied

# Rule change! Take into consideration the first seat in each direction, instead of the 8 adjacent cells
# Furthermore, 5 occupied seats seen through this new rule are required to free an occupied seat.
# Return the number of occupied seats when the system reaches stability
def day11_2(input: list):
	curr_map = input.copy()
	curr_occupied = 0

	while True:
		updates = False
		new_map = curr_map.copy()

		for i, line in enumerate(curr_map):
			for j, char in enumerate(line):
				if char == '.':
					continue

				visible_occupied = n_line_of_sights_occupied(curr_map, i, j)
				if char == 'L' and visible_occupied == 0:
					updates = True
					
					new_map[i] = new_map[i][0:j] + '#' + new_map[i][j+1:]
					curr_occupied += 1

				if char == '#' and visible_occupied >= 5:
					updates = True
					
					new_map[i] = new_map[i][0:j] + 'L' + new_map[i][j+1:]
					curr_occupied -= 1

		if not updates:
			print(curr_occupied)
			return

		curr_map = new_map.copy()

def n_line_of_sights_occupied(input: list, x: int, y: int):
	n_occupied = 0
	n = len(input)
	m = len(input[0])

	#left
	r = range(y-1,-1,-1)
	n_occupied += check_line_of_sight(input, [x for _ in r], r)

	#right
	r = range(y+1,m)
	n_occupied += check_line_of_sight(input, [x for _ in r], r)

	#top
	r = range(x-1,-1,-1)
	n_occupied += check_line_of_sight(input, r, [y for _ in r])

	#bottom
	r = range(x+1,n)
	n_occupied += check_line_of_sight(input, r, [y for _ in r])

	#top-left
	n_occupied += check_line_of_sight(input, range(x-1,-1,-1), range(y-1,-1,-1))

	#bottom-right
	n_occupied += check_line_of_sight(input, range(x+1,n), range(y+1,m))

	#top-right
	n_occupied += check_line_of_sight(input, range(x-1,-1,-1), range(y+1,m))

	#bottom-left
	n_occupied += check_line_of_sight(input, range(x+1,n), range(y-1,-1,-1))
	
	return n_occupied

def check_line_of_sight(input: list, range_x: list, range_y: list):
	for i,j in zip(range_x, range_y):
		if input[i][j] == '.':
			continue
		else:
			if input[i][j] == '#':
				return 1
			break
	return 0

if __name__ == '__main__':
	input_list = read_input()
	day11(input_list)
	day11_2(input_list)