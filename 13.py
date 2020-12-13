def read_input():
	list = []
	with open('13.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))

	return list

def parse_input(input: list):
	arrival = int(input[0])
	bus_info = {int(x):i for i,x in enumerate(input[1].split(",")) if x != 'x'}
	
	return arrival, bus_info

# You are given your arrival time at a bus terminal, and a list of bus ids and departure times (from time t=0, each bus departs every x minutes, x = bus id). 
# Find how long you have to wait at the bus terminal before the first bus leaves. Return this number multiplied by the id of the leaving bus.
def day13(arrival_time: int, bus_info: list):
	min_wait = None
	min_id = None

	for bus_id in bus_info:
		remainder = arrival_time // bus_id
		earliest_departure = bus_id * (remainder+1)
		wait = earliest_departure - arrival_time
		
		if min_wait is None or wait < min_wait:
			min_wait = wait
			min_id = bus_id

	print(min_wait*min_id) 


# Given the same rules for buses' departures, find the timestamp t such that for each bus, it departs at t+i, where i is the index of the bus in the buses list.
# For example, given [7,13,x,x,59,x,31,19], we need to find t so that bus 7 to leave at t, bus 13 to leave at t+1, bus 59 to leave at t+4 and so on.
def day13_2(bus_info: list):
	# Resolving with the chinese remainder theorem
	# verify (7,13,59,31,19) are coprimes
	# t %  7 == 0      -> 	t === 0 mod 7
	# t % 13 == 13 - 1 -> 	t === 12 mod 13
	# t % 59 == 59 - 4 -> 	t === 55 mod 59
	# t % 31 == 31 - 6 -> 	t === 25 mod 31
	# t % 19 == 19 - 7 -> 	t === 12 mod 19
	# N = 7 * 13 * 59 * 31 * 19
	# 1) n_1 = 7 ; y_1 = N / n_1 - z_1 = y_1 ^ -1 mod n_1
	# 2) ...
	# 6) x = sum(a_i * y_i * z_i) mod N

	n = 1
	seen = []
	for bus_id in bus_info:
		for x in seen:
			if max(bus_id,x) % min(bus_id,x) == 0:
				raise Exception("Error - all numbers must be coprimes")
		seen.append(bus_id)
		n *= bus_id

	t = 0
	for bus_id in bus_info:
		n_i = bus_id
		
		a_i = (n_i - bus_info[n_i]) % n_i
		y_i = int(n / n_i)
		z_i = int(ext_euclid(y_i, n_i))

		t += a_i * y_i * z_i

	t = t % n
	print(t)

def ext_euclid(a: int, b: int):
	if max(a,b) % min(a,b) == 0:
		raise Exception("a,b must be coprimes")

	mtx = [[0, a, 1, 0], [0, b, 0, 1]]

	while mtx[-1][1] != 0:
		q_i = mtx[-2][1] // mtx[-1][1]
		r_i = mtx[-2][1] % mtx[-1][1]
		x_i = mtx[-2][2] - q_i * mtx[-1][2]
		y_i = mtx[-2][3] - q_i * mtx[-1][3]
		
		mtx.append([q_i, r_i, x_i, y_i])

	return mtx[-2][2]

if __name__ == '__main__':
	input_list = read_input()
	arrival_time, bus_info = parse_input(input_list)
	day13(arrival_time, bus_info)
	day13_2(bus_info)