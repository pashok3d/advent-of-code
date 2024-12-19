from collections import defaultdict

with open("../advent/input5.txt", "r") as f:
    lines = f.readlines()

rules = []
updates = []

prohibited_r_neighbours_dict = defaultdict(set)
larger_items = defaultdict(set)


def is_larger(left, right):
    # check if left is larger than right
    return left in larger_items[right]


def sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if is_larger(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array


def find_middle_element(update) -> int:
    index = len(update) // 2
    return update[index]


def check_update_order(update) -> bool:
    for i, item in enumerate(update):
        prohibited_r_neighbours: set[int] = prohibited_r_neighbours_dict[item]
        if len(set(update[i:]) & prohibited_r_neighbours):
            return False
    return True


for line in lines:
    if "|" in line:
        rule = list(map(int, line.strip().split("|")))
        left, right = rule[0], rule[1]
        rules.append(rule)
        prohibited_r_neighbours_dict[right].update({left})
        larger_items[left].update({right})
    elif "," in line:
        updates.append(list(map(int, line.strip().split(","))))


sum = 0
for update in updates:
    if check_update_order(update):
        # sum += find_middle_element(update)
        pass
    else:
        sorted_array = sort(update)
        assert check_update_order(update)
        sum += find_middle_element(sorted_array)

pass
