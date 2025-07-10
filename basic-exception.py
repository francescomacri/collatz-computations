def collatz(n):
  """
  This function takes a positive integer as input and generates the Collatz sequence.

  Args:
    n: The starting number for the Collatz sequence.

  Returns:
    A list containing the Collatz sequence starting with n.
  """
  sequence = [n]  # Initialize a list to store the sequence, starting with n
  while n != 1:
    if n % 2 == 0:  # If n is even
      n = n // 2
    else:  # If n is odd
      n = 3 * n + 1
    sequence.append(n)  # Add the new value of n to the sequence
  return sequence

# Get input from the user
try:
  num = int(input("Enter a positive integer: "))
  if num <= 0:
    print("Please enter a positive integer.")
  else:
    print(collatz(num))  # Print the generated Collatz sequence
except ValueError:
  print("Invalid input. Please enter a positive integer.")