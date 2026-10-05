# 8 Puzzle using Iterative Deepening Search (IDS)

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


# Generate possible next states
def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Up, Down, Left, Right
    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
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


# Depth Limited Search
def depth_limited_search(state, goal, limit, path):

    # Goal test
    if state == goal:
        return path

    # Depth limit reached
    if limit == 0:
        return None

    for next_state in get_neighbors(state):

        # Avoid cycles in current path
        if next_state not in path:

            result = depth_limited_search(
                next_state,
                goal,
                limit - 1,
                path + [next_state]
            )

            if result is not None:
                return result

    return None


# Iterative Deepening Search
def ids(initial, goal):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        result = depth_limited_search(
            initial,
            goal,
            depth,
            [initial]
        )

        if result is not None:
            return result

        depth += 1


# Print puzzle
def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()


# Run IDS
solution = ids(initial, goal)

print("\nIDS Solution")
print("Number of moves:", len(solution) - 1)
print()

for i, state in enumerate(solution):

    print("Step", i)
    print_puzzle(state)