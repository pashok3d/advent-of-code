with open("../advent/input3_2.txt", "r") as f:
    text = f.read()


def consume_numer_tuple(text: str) -> list:
    numbers = []
    current_number_str = ""
    for ch in text:
        if ch.isnumeric():
            current_number_str += ch
        elif ch == "," and not numbers:
            numbers.append(int(current_number_str))
            current_number_str = ""
        elif ch == ")" and numbers:
            numbers.append(int(current_number_str))
            break
        else:
            break
    return numbers


i = 0
result = 0
toggle = True
while True:
    if text[i : i + 4] == "mul(":
        numbers = consume_numer_tuple(text[i + 4 :])
        i += 4
        if len(numbers) == 2:
            shift = len(f"{numbers[0]},{numbers[1]})")
            i += shift
            if toggle:
                result += numbers[0] * numbers[1]
    elif text[i : i + 4] == "do()":
        toggle = True
        i += 4
    elif text[i : i + 7] == "don't()":
        toggle = False
        i += 7
    else:
        i += 1

    if i >= len(text):
        break

print(result)
