import numpy as np

with open("../advent/input4.txt", "r") as f:
    lines = f.readlines()

# convert to numpy array used as global variable
matrix = np.array([list(row.strip()) for row in lines])

# prep all xmas permutations as set
# xmas_permuts_set = set(itertools.permutations(list("XMAS")))
xmas_permuts_set = {tuple(["X", "M", "A", "S"]), tuple(["S", "A", "M", "X"])}


def check_word(word_chars: list[str]) -> bool:
    return tuple(word_chars) in xmas_permuts_set


def check_horizontal(i, j) -> int:
    is_xmas = check_word(matrix[i, j : j + 4].tolist())
    return int(is_xmas)


def get_horizontal_mask(i, j) -> np.ndarray:
    return np.array([i] * 4), np.array([j for j in range(j, j + 4)])


def check_vertical(i, j) -> int:
    is_xmas = check_word(matrix[i : i + 4, j].tolist())
    return int(is_xmas)


def get_vertical_mask(i, j) -> np.ndarray:
    return np.array([i for i in range(i, i + 4)]), np.array([j] * 4)


def check_r_diagonal(i, j) -> int:
    if i + 3 < matrix.shape[0] and j + 3 < matrix.shape[1]:
        chars = matrix[[i + l for l in range(4)], [j + l for l in range(4)]].tolist()
        is_xmas = check_word(chars)
        return int(is_xmas)
    else:
        return 0


def get_r_diagonal_mask(i, j) -> np.ndarray:
    return np.array([i + l for l in range(4)]), np.array([j + l for l in range(4)])


def check_l_diagonal(i, j) -> int:
    if i + 3 < matrix.shape[0] and j - 3 >= 0:
        chars = matrix[[i + l for l in range(4)], [j - l for l in range(4)]].tolist()
        is_xmas = check_word(chars)
        return int(is_xmas)
    else:
        return 0


def get_l_diagonal_mask(i, j) -> np.ndarray:
    return np.array([i + l for l in range(4)]), np.array([j - l for l in range(4)])


masked_matrix = np.zeros_like(matrix, dtype=int)

count = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if check_vertical(i, j):
            count += 1
            mask = get_vertical_mask(i, j)
            masked_matrix[mask[0], mask[1]] += 1

        if check_horizontal(i, j):
            count += 1
            mask = get_horizontal_mask(i, j)
            masked_matrix[mask[0], mask[1]] += 1

        if check_r_diagonal(i, j):
            count += 1
            mask = get_r_diagonal_mask(i, j)
            masked_matrix[mask[0], mask[1]] += 1

        if check_l_diagonal(i, j):
            count += 1
            mask = get_l_diagonal_mask(i, j)
            masked_matrix[mask[0], mask[1]] += 1


print(count)
