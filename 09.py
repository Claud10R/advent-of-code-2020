def read_input():
	list = []
	with open('09.txt', 'r') as file:
		for line in file:
			list.append(int(line.replace("\n","")))

	return list

# Given a buffer size of 25, determine whether the buffer contains two numbers whose sum is the next element to be added.
# If not, add the new element to the buffer and remove the oldest one.
# Note: unoptimized solution, needs reworking
def day09(input: list):
	max_buffer = 25
	buffer = []

	for i, x in enumerate(input):
		if len(buffer) == max_buffer:
			x_found = False
			for j in range(0, len(buffer) - 1):
				for k in range(j + 1, len(buffer)):
					if buffer[j] + buffer[k] == x:
						x_found = True
						break
			if not x_found:
				print(x)
				return x

		if len(buffer) < max_buffer:
			buffer.append(x)
		else:
			buffer = buffer[1:25] + [x]

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
