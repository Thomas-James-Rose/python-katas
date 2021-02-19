import sys
import string
import functools 

def longest_palindrome(input_string):
  if(input_string == ""):
    print(f"Input String: \"\"")
    print("Length: 0")
    return

  print(f"Input String: {input_string}")

  substrings = []
  for i in range(0, len(input_string)):
    remaining_string = input_string[i + 1 : len(input_string)]
    for i2 in range(0, len(remaining_string)):
      substrings.append((input_string[i] + remaining_string[0:i2+1]).lower())

  print(f"Searching for largest palindrome from: {substrings}")

  palindrome_reducer = lambda acc, s: (s if len(s) > len(acc) and s == s[::-1] else acc)
  longest_palindrome = functools.reduce(palindrome_reducer, substrings, input_string[0])

  print(f"Longest Palindrome: {longest_palindrome}")
  print(f"Length: {len(longest_palindrome)}")
  print("\n")

longest_palindrome(sys.argv[1])