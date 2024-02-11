# Initialize the map grid
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]

# Print initial message
print("Hiding your treasure! X marks the spot.")

# Prompt the user to input the position for hiding the treasure
position = input("Where do you want to put your treasure buddy ? ")  # Where do you want to put the treasure? enter A1 or A2 or A3..B1...B3 or C1...C3

# The code below is where the position provided by the user is checked
# If it matches a valid position, the corresponding grid cell is updated with "X"

# If the position is A1, update the first row and first column
if position == "A1":
  map[0][0] = "X"
# If the position is B1, update the first row and second column
elif position == "B1":
   map[0][1] = "X"
# If the position is C1, update the first row and third column
elif position == "C1":
   map[0][2] = "X"
# If the position is A2, update the second row and first column
elif position == "A2":
   map[1][0] = "X"
# If the position is B2, update the second row and second column
elif position == "B2":
   map[1][1] = "X"
# If the position is C2, update the second row and third column
elif position == "C2":
   map[1][2] = "X"
# If the position is A3, update the third row and first column
elif position == "A3":
   map[2][0] = "X"
# If the position is B3, update the third row and second column
elif position == "B3":
   map[2][1] = "X"
# If the position is C3, update the third row and third column
elif position == "C3":
   map[2][2] = "X"

# Print a message indicating the treasure is hidden
print("Hiding your treasure! X marks the spot.")

# The code below prints the updated map with the treasure marked as 'X'
print(f"{line1}\n{line2}\n{line3}")

