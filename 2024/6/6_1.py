"""
1. Read input
2. Convert to numpy array
3. Find starting position
4. Convert to binary array for simplicity?
5. Run a loop, where in each iteration:
    5.1 Given current position and direction, find next stop (obsticle)
    5.2 If next stop exists, reassign current position, direction and update set of visited positions
    5.3 If next stop doesn't exist, update set of visited positions and finish the loop
"""

import numpy as np
from typing import Optional

with open("2024/6/input6.txt", "r") as f:
    lines = f.readlines()

matrix = [list(l.strip()) for l in lines]
location_map = np.array(matrix)
visited_positions: list[tuple[int, int]] = []
binary_map = np.zeros(location_map.shape, dtype=np.int8)
binary_map[location_map == "#"] = 1


def get_initial_position(location_map: np.ndarray) -> tuple[int, int]:
    y, x = np.where(location_map == "^")
    return y.item(), x.item()


def find_next_stop(
    position: tuple[int, int], direction: int
) -> Optional[tuple[int, int]]:
    y, x = position
    try:
        if direction == 0:
            beam = binary_map[:y, x][::-1].tolist()
            steps = beam.index(1)
            y -= steps
        elif direction == 1:
            beam = binary_map[y, x:].tolist()
            steps = beam.index(1) - 1
            x += steps
        elif direction == 2:
            beam = binary_map[y:, x].tolist()
            steps = beam.index(1) - 1
            y += steps
        else:
            beam = binary_map[y, :x][::-1].tolist()
            steps = beam.index(1)
            x -= steps
    except ValueError:
        return None

    return y, x


def update_visited_positions(
    start_position: tuple[int, int],
    end_position: Optional[tuple[int, int]],
    direction: int,
) -> None:
    y_start, x_start = start_position
    if end_position:
        y_end, x_end = end_position
        if x_start == x_end:
            # vertical move
            if y_start > y_end:
                # up
                for y_i in range(y_end, y_start + 1):
                    visited_positions.append((y_i, x_end))
            else:
                # down
                for y_i in range(y_start, y_end + 1):
                    visited_positions.append((y_i, x_end))
        else:
            # horizontal move
            if x_start > x_end:
                # left
                for x_i in range(x_end, x_start + 1):
                    visited_positions.append((y_end, x_i))
            else:
                # right
                for x_i in range(x_start, x_end + 1):
                    visited_positions.append((y_end, x_i))

    else:
        # move that goes out of the map
        if direction == 0:
            for y_i in range(0, y_start + 1):
                visited_positions.append((y_i, x_start))
        elif direction == 1:
            for x_i in range(x_start, binary_map.shape[1]):
                visited_positions.append((y_start, x_i))
        elif direction == 2:
            for y_i in range(y_start, binary_map.shape[0]):
                visited_positions.append((y_i, x_start))
        else:
            for x_i in range(0, x_start + 1):
                visited_positions.append((y_start, x_i))


current_position = get_initial_position(location_map)
direction = 0


while True:
    # Find next stop
    position = find_next_stop(current_position, direction)

    if position:
        # update direction
        direction += 1
        direction = direction % 4

        # update visited positions
        update_visited_positions(current_position, position, direction)

        # update current position
        current_position = position
    else:
        # update visited positions
        update_visited_positions(current_position, position, direction)
        break

print(len(set(visited_positions)))

# Visualize the path
for position in visited_positions:
    y, x = position
    location_map[y, x] = "X"
