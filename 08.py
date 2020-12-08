def read_input():
	list = []
	with open('08.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))
	
	return list

def parse_input(input_list: list):
	for i, line in enumerate(input_list):
		instruction = line[:3]
		parameter = int(line[4:])
		input_list[i] = [instruction, parameter]

# Build an interpreter for the three listed instruction:
# - acc adds its parameter to the accumulator, increases the program counter by 1
# - nop increases the program counter by 1
# - jmp adds its parameter to the program counter
# The input causes an infinite loop. Return the value of the accumulator before executing any instruction
# a second time.
def day08(input: list):
	pc = 0
	accumulator = 0
	executed = set()

	while True:
		if pc in executed:
			print(accumulator)
			return

		instruction, parameter = input[pc]
		executed.add(pc)

		pc, accumulator = execute_instruction(pc, accumulator, instruction, parameter)

def execute_instruction(pc: int, acc: int, instruction: str, parameter: int):
	if instruction not in ['acc', 'nop', 'jmp']:
		raise("Unsupported Instruction")

	if instruction == 'acc':
		acc += parameter

	if instruction in ['acc', 'nop']:
		pc += 1

	if instruction == 'jmp':
		pc += parameter

	return pc, acc

# The program can terminate by changing exactly one 'jmp' instruction to 'nop', or vice versa.
# Find the correct alteration, return the value of the accumulator before halting.
def day08_2(input: list):
	for i, [instruction, parameter] in enumerate(input):
		if instruction not in ['jmp', 'nop']:
			continue

		if instruction == 'jmp':
			new_input = input[0:i].copy() + [['nop', parameter]] + input[i+1:].copy()

		if instruction == 'nop':
			new_input = input[0:i].copy() + [['jmp', parameter]] + input[i+1:].copy()

		terminated, final_acc = program_terminates(new_input)
		if terminated:
			print(final_acc)
			return

def program_terminates(input: list):
	pc = 0
	accumulator = 0
	executed = set()

	while True:
		if pc >= len(input):
			return True, accumulator

		if pc in executed:
			return False, 0

		instruction, parameter = input[pc]
		executed.add(pc)

		pc, accumulator = execute_instruction(pc, accumulator, instruction, parameter)

if __name__ == '__main__':
	input_list = read_input()
	parse_input(input_list)
	day08(input_list)
	day08_2(input_list)
