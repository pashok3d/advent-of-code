with open("../advent/input.txt", "r") as f:
    lines = f.readlines()

pairs = [l.split() for l in lines]
left_ids = [pair[0] for pair in pairs]
right_ids = [pair[1] for pair in pairs]

left_ids_sorted = sorted(left_ids)
right_ids_sorted = sorted(right_ids)

sum_distance = 0
for left_id, right_id in zip(left_ids_sorted, right_ids_sorted):
    sum_distance += abs(int(left_id) - int(right_id))

print(sum_distance)
