def read_input():
	list = []
	with open('09.txt', 'r') as file:
		for line in file:
			list.append(int(line.replace("\n","")))

	return list

# Given a buffer size of 25, determine whether the buffer contains two numbers whose sum is the next element to be added.
# If not, add the new element to the buffer and remove the oldest one.
def day09(input: list):
	max_buffer = 25

	for i in range(25, len(input)):
		x = input[i]
		if not check_sum(x, input[i-max_buffer:i]):
			print(x)
			return x
	print(i)

def check_sum(target: int, buffer: list):
	complements = {}

	for x in buffer:
		if x in complements:
			return True
		else:
			complements[target-x] = 1

	return False

# Find a subarray in the sequence whose sum equals the result from part one. Return the sum of the maximum
# and minimum element of this sequence.
def day09_2(input: list, to_find: int):
	curr_sum = 0
	min_idx = 0

	for i,x in enumerate(input):
		while curr_sum > to_find and min_idx < i:
			curr_sum -= input[min_idx]
			min_idx += 1

		if curr_sum == to_find:
			min_v = min(input[min_idx : i + 1])
			max_v = max(input[min_idx : i + 1])
			print(min_v + max_v)
			return

		curr_sum += x

if __name__ == '__main__':
	input_list = read_input()
	x = day09(input_list)
	day09_2(input_list, x)
