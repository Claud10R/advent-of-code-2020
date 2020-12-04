def read_input():
	list = []
	with open('01.txt', 'r') as file:
		for line in file:
			val = int(line)
			list.append(val)
	
	return list

# Find the two elements whose sum is 2020. Return their product.
def day01(input_list):
	complements2020 = {}

	for x in input_list:
		if x not in complements2020:
			complements2020[2020-x] = 1
		else:
			result = x * (2020 - x)
			print(result)
			return

# Find the three elements whose sum is 2020. Return their product.
def day01_2(input_list):
	seen = []
	complements2020 = {}

	for x in input_list:
		if x not in complements2020:
			for y in seen:
				complements2020[2020-x-y] = [x,y]
			seen.append(x)
		else:
			result = x * complements2020[x][0] * complements2020[x][1] 
			print(result)
			return

if __name__ == '__main__':
	input_list = read_input()
	day01(input_list)
	day01_2(input_list)