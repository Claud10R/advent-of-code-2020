import re

def read_input():
	list = []
	with open('18.txt', 'r') as file:
		for line in file:
			list.append(line.replace("\n",""))

	return list

# Given the index of a '(' char, returns the index of its corresponding closure [i.e., the corresponding ')' char]
def find_closing_bracket_idx(line: str, start: int):
    if line[start] != '(':
        raise Exception("Usage error")

    brackets = 0
    for i, char in enumerate(line[start:]):
        if char == '(':
            brackets += 1
        if char == ')':
            brackets -= 1

        if brackets == 0:
            return start+i

    raise Exception("Unbalanced expression")

def compute(op: str, d1: int, d2: int):
    if op not in ['+', '*']:
        raise Exception("Unsupported operation.",op,d1,d2)

    if op == '+':
        return d1+d2

    if op == '*':
        return d1*d2

# Given a list of expressions, compute their values. Rule: '+' and '*' have the same precedence.
# Return the same of the values of the expressions.
def day18(input: list):
    sum = 0
    for line in input:
        sum += evaluate_line_same_precedence(line)
    print(sum)

def evaluate_line_same_precedence(line: str):
    res, i = 0, 0
    op = None

    while i < len(line):
        if line[i] in ['+', '*']:       # Store the operation, will be used upon seeing the number on its right
            op = line[i]

        if line[i] == '(':              # Recursive call to evaluate all the content of the brackets, then operation performed (if any)
            j = find_closing_bracket_idx(line, i)

            bracket_res = evaluate_line_same_precedence(line[i+1:j])
            res = bracket_res if op is None else compute(op, res, bracket_res)

            i = j

        if re.match('^\d$', line[i]):   # Number seen. Get all its digit, perform the last seen operation
            x = line[i]
            k = i + 1
            
            while k < len(line) and re.match('^\d$', line[k]):
                x += str(line[k])
                k += 1

            i = k
            val = int(x)
            res = val if res == 0 else compute(op, res, val)

        i += 1

    return res

# Given a list of expressions, compute their values. Rule: '+' has precedence over '*'.
# Return the same of the values of the expressions.
def day18_2(input: list):
    sum = 0
    for line in input:
        sum += evaluate_line_sum_first(line)
    print(sum)

def evaluate_line_sum_first(line: str):
    if '+' not in line:                 # If no '+' is found, then we can re-use the previous function
        return evaluate_line_same_precedence(line)

    if '(' not in line:                 # If there are no brackets, then we can just split on the '*' sign, evaluate the factors, and multiply them.
        factors = line.split("*")
        
        product = 1
        for factor in factors:
            x = evaluate_line_same_precedence(factor)
            product *= x 
        
        return product
    else:                               # Otherwise, evaluate the leftmost expression inside brackets, replace the result in the line and make a recursive call.
        brackets = re.finditer('\(', line)
        i = next(brackets).start()
        j = find_closing_bracket_idx(line, i)

        res = evaluate_line_sum_first(line[i+1:j])
        new_line = line[:i] + str(res) + line[j+1:]

        return evaluate_line_sum_first(new_line)


if __name__ == '__main__':
    input = read_input()
    day18(input)
    day18_2(input)