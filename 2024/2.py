with open("../advent/input2.txt", "r") as f:
    reports = f.readlines()


def is_safe(reports: list[int]) -> bool:
    prev_direction = None
    for left, right in zip(reports, reports[1:]):
        if left > right:
            if (prev_direction and prev_direction == "asc") or (left - right > 3):
                return False
            prev_direction = "desc"
        elif right > left:
            if (prev_direction and prev_direction == "desc") or (right - left > 3):
                return False
            prev_direction = "asc"
        else:
            return False

    return True


def generate_permuts(report: list[int]) -> list[list[int]]:
    permuts = []
    for i in range(len(report)):
        permuts.append(report[:i] + report[i + 1 :])
    return permuts


counter = 0
for report in reports:
    report = [int(item) for item in report.split()]
    if not is_safe(report):
        r_permuts = generate_permuts(report)
        counter += int(any([is_safe(r) for r in r_permuts]))
    else:
        counter += 1

print(counter)
