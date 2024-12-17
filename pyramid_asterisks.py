rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(rows - i):
    # Inner loop prints spaces for each row
    print(" ", end="")
  for k in range(2 * i - 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks

 