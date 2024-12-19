import collections

with open("../advent/input.txt", "r") as f:
    lines = f.readlines()

pairs = [l.split() for l in lines]
left_ids = [pair[0] for pair in pairs]
right_ids = [pair[1] for pair in pairs]

c = collections.Counter(right_ids)

sim_score = 0
for id in left_ids:
    sim_score += int(id) * int(c.get(id, 0))

print(sim_score)
