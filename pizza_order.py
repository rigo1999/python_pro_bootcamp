#Python Pizza

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill = 0
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill = bill + 2
  else:
    bill = 15
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill = bill + 3
  else:
    bill = 20
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill = bill + 3
  else:
    bill = 25
if extra_cheese == "Y":
  bill = bill + 1

print(f"Your final bill is: ${bill}.")
  

