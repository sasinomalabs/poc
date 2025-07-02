import re

def is_palindrome(data) -> bool:
  """
  Checks if a string or integer is a palindrome.

  Args:
    data: The string or integer to check.

  Returns:
    True if the data is a palindrome, False otherwise.
  """
  if not isinstance(data, (str, int)):
    raise TypeError("Input must be a string or an integer.")

  s = str(data)
  # Remove non-alphanumeric characters and convert to lowercase
  s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

  # Check if the string is equal to its reverse
  return s == s[::-1]
