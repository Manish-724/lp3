# Practical 1: Paper Prototype / Simple Key Master Game
# This is a console prototype to test the game rules and interactions.
board = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", "k", ".", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", "E", "#"],
    ["#", "#", "#", "#", "#"]
]

player_row, player_col = 1, 1
has_key = False

print("Controls: W=Up, A=Left, S=Down, D=Right")
print("Goal: Collect the key (k), then reach the exit (E).")

while True:
    print("\\n" + "-" * 15)
    for r in range(len(board)):
        row = ""
        for c in range(len(board[0])):
            row += " P " if (r, c) == (player_row, player_col) else f" {board[r][c]} "
        print(row)
    print("-" * 15)
    print("Key status:", "Unlocked" if has_key else "Locked")

    move = input("Move (W/A/S/D, Q to quit): ").strip().upper()
    if move == "Q":
        print("Game ended.")
        break

    new_row, new_col = player_row, player_col
    if move == "W":
        new_row -= 1
    elif move == "S":
        new_row += 1
    elif move == "A":
        new_col -= 1
    elif move == "D":
        new_col += 1
    else:
        print("Invalid move.")
        continue

    if not (0 <= new_row < len(board) and 0 <= new_col < len(board[0])):
        print("Out of bounds!")
        continue
    if board[new_row][new_col] == "#":
        print("You hit a wall!")
        continue

    player_row, player_col = new_row, new_col
    if board[player_row][player_col] == "k":
        has_key = True
        board[player_row][player_col] = "."
        print("You picked up the key!")
    elif board[player_row][player_col] == "E":
        if has_key:
            print("YOU WIN! You escaped!")
            break
        print("Door is locked. Find the key first!")
