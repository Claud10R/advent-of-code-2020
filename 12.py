import math

def read_input():
	list = []
	with open('12.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))

	return list

def manhattan_distance(source: list, pos: list):
	distance = 0
	distance += abs(pos[0] - source[0])
	distance += abs(pos[1] - source[1])
	return distance

# Move a ship a round a map with the following commands:
# - N, S, E, W move the ship in the corresponding direction
# - L, R rotate the ship (left or right) of the corresponding number of degrees
# - F moves the ship forward, according to the current rotation
# Return the manhattan distance between starting and final position
def day12(input: list):
	direction = 0
	directions_map = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
	
	origin = [0,0]
	curr_pos = origin.copy()

	for line in input:
		action = line[0]
		value = int(line[1:])

		if action in ['L', 'R']:
			direction += value if action == 'L' else -value
			direction = direction % 360

		if action == 'F':
			action = directions_map[direction]

		if action in ['N','S']:
			curr_pos[1] += value if action == 'N' else -value

		if action in ['E', 'W']:
			curr_pos[0] += value if action == 'E' else -value

	print(manhattan_distance(origin,curr_pos))

# New rule! The ship now follows a waypoint, which moves depending on the rules:
# - N, S, E, W move the waypoint in the corresponding direction
# - L, R rotate the waypoint around the ship
# - F moves the ship to the waypoint a number of times equal to the given value
# Return the manhattan distance between starting and final position
def day12_2(input: list):
	origin = [0,0]
	curr_pos = origin.copy()
	waypoint = [10,1]

	for line in input:
		action = line[0]
		value = int(line[1:])

		if action in ['L', 'R']:
			angle = value if action == 'L' else -value
			rad_angle = to_radians(angle % 360)
			new_wp = [0,0]
			new_wp[0] = round(waypoint[0] * math.cos(rad_angle) - waypoint[1] * math.sin(rad_angle))
			new_wp[1] = round(waypoint[0] * math.sin(rad_angle) + waypoint[1] * math.cos(rad_angle))
			waypoint = new_wp

		if action == 'F':
			curr_pos[0] += waypoint[0] * value
			curr_pos[1] += waypoint[1] * value

		if action in ['N','S']:
			waypoint[1] += value if action == 'N' else -value

		if action in ['E', 'W']:
			waypoint[0] += value if action == 'E' else -value

	print(manhattan_distance(origin,curr_pos))

def to_radians(angle: int):
	return math.pi * angle / 180

if __name__ == '__main__':
	input_list = read_input()
	day12(input_list)
	day12_2(input_list)