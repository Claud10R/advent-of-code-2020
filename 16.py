import re

def read_input():
    list = []
    groups = open("16.txt").read().split("\n\n")

    for group in groups:
        list.append(group.splitlines())

    return list

def parse_input(input: list):
    rules = {}

    for line in input[0]:
        rule = line.split(":")[0]

        regex = re.compile(r"\d+")
        values = regex.findall(line)
        ranges = [[int(values[0]), int(values[1])], [int(values[2]), int(values[3])]]
        rules[rule] = ranges

    myticket = input[1][1].split(",")
    tickets = [line.split(",") for line in input[2][1:]]

    return rules, myticket, tickets

def check_value_against_rule(rule: list, value: int):
    return (rule[0][0] <= value <= rule[0][1]) or (rule[1][0] <= value <= rule[1][1])

# Given a set of rules, for each of which the possible ranges are known, and given some tickets containing values
# which have to match the rules (the binding is not known), determine the tickets containing impossible values
# (which can't be associated to any rules). Return the sum of these values.
def day16(rules: dict, tickets: list):
    scan_error_rate = 0
    valid_tickets = []

    for ticket in tickets:
        is_valid = True
        for value in ticket:
            if all(not check_value_against_rule(rules[rule], int(value)) for rule in rules):
                scan_error_rate += int(value)
                is_valid = False
        if is_valid:
            valid_tickets.append(ticket)

    print(scan_error_rate)
    return valid_tickets

# Given only the valid tickets, match their fields to the rules. Then return the product of the rules
# containing "departure" in their name for your ticket.
def day16_2(rules: dict, myticket: list, tickets: list):
    matches = {}
    for rule in rules:
        matches[rule] = list(range(len(myticket)))

    tickets.append(myticket)

    for ticket in tickets:
        for idx, value in enumerate(ticket):
            for rule in rules:
                if not check_value_against_rule(rules[rule], int(value)) and idx in matches[rule]:
                    matches[rule].remove(idx)

    deleted = []
    while True:
        to_delete = -1
        for rule in matches:
            x = matches[rule][0]
            if len(matches[rule]) == 1 and x not in deleted:
                to_delete = x
                break

        if to_delete == -1:
            break

        for rule in matches:
            if to_delete in matches[rule] and len(matches[rule]) > 1:
                matches[rule].remove(to_delete)

        deleted.append(to_delete)

    product = 1
    for rule in rules:
        if 'departure' in rule:
            match_idx = matches[rule][0]
            product *= int(myticket[match_idx])

    print(product)

if __name__ == '__main__':
    input = read_input()
    rules, myticket, tickets = parse_input(input)

    valid_tickets = day16(rules, tickets)
    day16_2(rules, myticket, valid_tickets)
