# Practical 2: Grid Explorer - Move a character using WASD
GRID_SIZE = 5
player_x, player_y = 2, 2

print("=" * 35)
print("WELCOME TO GRID EXPLORER")
print("=" * 35)
print("W = Up | A = Left | S = Down | D = Right | Q = Quit")

while True:
    print("\\n  " + " ".join(str(i) for i in range(GRID_SIZE)))
    for r in range(GRID_SIZE):
        row = f"{r} "
        for c in range(GRID_SIZE):
            row += "P " if r == player_y and c == player_x else ". "
        print(row)
    print(f"Position -> x: {player_x}, y: {player_y}")

    move = input("Enter move (W/A/S/D/Q): ").strip().upper()

    if move == "W":
        if player_y > 0:
            player_y -= 1
        else:
            print("Hit the top edge!")
    elif move == "S":
        if player_y < GRID_SIZE - 1:
            player_y += 1
        else:
            print("Hit the bottom edge!")
    elif move == "A":
        if player_x > 0:
            player_x -= 1
        else:
            print("Hit the left edge!")
    elif move == "D":
        if player_x < GRID_SIZE - 1:
            player_x += 1
        else:
            print("Hit the right edge!")
    elif move == "Q":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input! Use W, A, S, D, or Q.")
