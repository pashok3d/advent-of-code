import numpy as np

with open("../advent/input4.txt", "r") as f:
    lines = f.readlines()

# convert to numpy array used as global variable
matrix = np.array([list(row.strip()) for row in lines])
xmas_permuts_set = {tuple(["M", "A", "S"]), tuple(["S", "A", "M"])}


def check_word(word_chars: list[str]) -> bool:
    return tuple(word_chars) in xmas_permuts_set


def check_r_diagonal(i, j) -> int:
    if i + 2 < matrix.shape[0] and j + 2 < matrix.shape[1]:
        chars = matrix[[i + l for l in range(3)], [j + l for l in range(3)]].tolist()
        is_xmas = check_word(chars)
        return int(is_xmas)
    else:
        return 0


def get_r_diagonal_mask(i, j) -> np.ndarray:
    return np.array([i + l for l in range(3)]), np.array([j + l for l in range(3)])


def check_l_diagonal(i, j) -> int:
    if i + 2 < matrix.shape[0] and j - 2 >= 0:
        chars = matrix[[i + l for l in range(3)], [j - l for l in range(3)]].tolist()
        is_xmas = check_word(chars)
        return int(is_xmas)
    else:
        return 0


def get_l_diagonal_mask(i, j) -> np.ndarray:
    return np.array([i + l for l in range(3)]), np.array([j - l for l in range(3)])


masked_matrix = np.zeros_like(matrix, dtype=int)

count = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if check_r_diagonal(i, j) and check_l_diagonal(i, j + 2):
            count += 1
            mask = get_r_diagonal_mask(i, j)
            masked_matrix[mask[0], mask[1]] += 1
            mask = get_l_diagonal_mask(i, j + 2)
            masked_matrix[mask[0], mask[1]] += 1


print(count)
