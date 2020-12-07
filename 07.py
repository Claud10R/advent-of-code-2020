import re

def read_input():
	list = []
	with open('07.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))
	
	return list

def parse_input(input_list: list):
	rules = {}

	for line in input_list:
		splitted = line.split(" bags contain ")
		outermost = splitted[0]
		rules[outermost] = {}
		
		inner = splitted[1]
		inner_list = re.findall("\d+ [a-z]+ [a-z]+", inner)
		innermost = [x.split() for x in inner_list]
	
		for entry in innermost:
			bag_color = " ".join(entry[1:])
			rules[outermost][bag_color] = int(entry[0])

	return rules

# For each rule, determine whether it eventually contains a 'shiny gold' bag or not. Return the total number of
# bags which contain shiny gold bags.
def day07(rules: dict, looking_for: str):
	count = 0

	for rule in rules:
		if looking_for in rules[rule]:
			count += 1
		else:
			if rule_bfs(rules, [rule], [], looking_for):
				count += 1

	print(count)

def rule_bfs(rules: dict, to_explore: list, explored: list, to_find: str):
	if len(to_explore) == 0:
		return False

	new_rule = to_explore[0]

	if to_find in rules[new_rule]:
		return True

	explored.append(new_rule)

	for bag in rules[new_rule]:
		if bag not in explored and bag not in to_explore:
			to_explore.append(bag)

	return rule_bfs(rules, to_explore[1:], explored, to_find)


# Starting from the 'shiny gold' bag, find the total number of bags it needs to contain according to the rules
def day07_2(rules: dict, looking_for: str):
	tot_bags = cnt_bags(rules, looking_for)
	print(tot_bags - 1) #-1 is needed because the "starting" bag does not need to be counted

def cnt_bags(rules: dict, curr_rule: str):
	new_rule = rules[curr_rule]

	if len(new_rule) == 0:
		return 1

	cnt = 1 #count the containing bag
	for bag in new_rule:
		cnt += new_rule[bag] * cnt_bags(rules, bag) #count all the contained bags

	return cnt

if __name__ == '__main__':
	input_list = read_input()
	rules = parse_input(input_list)
	day07(rules, "shiny gold")
	day07_2(rules, "shiny gold")
