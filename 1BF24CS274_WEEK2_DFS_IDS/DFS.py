# 8 Puzzle using DFS

initial = (
    1, 2, 3,
    0, 4, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# Generate possible moves
def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Right, Down, Left, Up
    moves = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank and tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


# DFS
def dfs(initial, goal):

    stack = [(initial, [initial])]

    # Mark initial state as visited immediately
    visited = {initial}

    while stack:

        current, path = stack.pop()

        # Goal test
        if current == goal:
            return path

        # Generate next states
        for next_state in get_neighbors(current):

            if next_state not in visited:

                # Mark visited BEFORE adding to stack
                visited.add(next_state)

                stack.append(
                    (next_state, path + [next_state])
                )

    return None


# Print puzzle
def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()


# Run DFS
solution = dfs(initial, goal)


if solution:

    print("DFS Solution")
    print("Number of moves:", len(solution) - 1)
    print()

    for i, state in enumerate(solution):

        print("Step", i)
        print_puzzle(state)

else:

    print("No solution found")