# Define the initial grid with three rows, each containing three elements
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

# Combine the rows into a 2D list to represent the map
map = [line1, line2, line3]

# Print the initial message
print("Hiding your treasure! X marks the spot.")

# Prompt the user to input the position to hide the treasure
position = input("Where do you want to put the treasure? ")

# Define a string representing the column labels
column_labels = "ABC"

# Convert the input position (e.g., 'A1', 'B2', etc.) to grid indices
row = int(position[1]) - 1  # Convert the second character to an integer and subtract 1 for zero-based indexing
col = column_labels.index(position[0])  # Find the index of the first character in the column_labels string

# Update the map at the specified row and column with "X" to mark the treasure location
map[row][col] = "X"

# Print the message indicating the treasure is hidden
print("Hiding your treasure! X marks the spot.")

# Print the updated map with the treasure marked as 'X'
for line in map:
    print(" ".join(line))

