# Method to reverse a string
def reversedString(someString):
    return someString[::-1]


# Get the input string from standard input.
inputString = raw_input("Enter a word:")


# Check the input string against a reversed string
if inputString == reversedString(inputString):
  print("The word, %s is a palidrome" %inputString)
else:
  print("The word, %s is not a palindrome" %inputString)
