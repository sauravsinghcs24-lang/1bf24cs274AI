# Vacuum Cleaner Agent

print("===== VACUUM CLEANER AGENT =====")

# Get room status
room_A = input("Is Room A dirty? (yes/no): ").lower()
room_B = input("Is Room B dirty? (yes/no): ").lower()

# Get vacuum position
position = input("Where is the vacuum? (A/B): ").upper()

print("\n--- Agent Actions ---")

# Vacuum starts in Room A
if position == "A":

    if room_A == "yes":
        print("Room A is dirty")
        print("Action: SUCK")
        room_A = "no"
    else:
        print("Room A is already clean")

    print("Action: MOVE RIGHT")
    position = "B"

    if room_B == "yes":
        print("Room B is dirty")
        print("Action: SUCK")
        room_B = "no"
    else:
        print("Room B is already clean")


# Vacuum starts in Room B
elif position == "B":

    if room_B == "yes":
        print("Room B is dirty")
        print("Action: SUCK")
        room_B = "no"
    else:
        print("Room B is already clean")

    print("Action: MOVE LEFT")
    position = "A"

    if room_A == "yes":
        print("Room A is dirty")
        print("Action: SUCK")
        room_A = "no"
    else:
        print("Room A is already clean")


else:
    print("Invalid position!")


# Goal test
if room_A == "no" and room_B == "no":
    print("\nGoal achieved!")
    print("Both rooms are clean.")