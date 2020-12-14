from itertools import product
import time

def read_input():
	list = []
	with open('14.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))

	return list

def parse_input(input: list):
	list = []
	for line in input:
		parsed = line.split(" = ")
		if parsed[0] == 'mask':
			list.append(['mask', parsed[1]])
		else:
			list.append([int(parsed[0][4:-1]), int(parsed[1])])
	return list

def day14(input: list):
	memory = {}
	curr_mask = ""

	for address,value in input:
		if address == 'mask':
			curr_mask = value
			continue
		else:
			value |= int(curr_mask.replace("X","0"),2)
			value &= int(curr_mask.replace("X","1"),2)
			memory[address] = value

	print(sum(memory.values()))

def day14_2(input: list):
	memory = {}
	curr_mask = ""

	for address, value in input:
		if address == 'mask':
			curr_mask = value
			continue
		else:
			all_addresses = mask_gen_addresses(curr_mask, address)
			for addr in all_addresses:
				memory[addr] = value

	curr_sum = 0
	print(sum(memory.values()))

def mask_gen_addresses(mask: str, address: int):
	xs = []
	for i, char in enumerate(mask):
		if char == 'X':
			xs.append(i)
	
	mask = int(mask.replace('X','0'),2)
	address |= mask

	replacements = list(product(['0','1'], repeat=len(xs)))
	address_bin = "{0:b}".format(address).zfill(36)

	addresses = []
	for new_bits in replacements:
		new_addr = address_bin[:]

		for i, offset in enumerate(xs):
			new_addr = new_addr[0:offset] + new_bits[i] + new_addr[offset+1:]

		addresses.append(int(new_addr,2))

	return addresses

if __name__ == '__main__':
	input = read_input()
	input = parse_input(input)
	
	day14(input)
	day14_2(input)