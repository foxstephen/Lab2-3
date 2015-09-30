inputString = raw_input("Enter a word:")

def reversedString(someString):
    return someString[::-1]

if inputString == reversedString(inputString):
  print("This word is a palidrome")
else:
  print("This word is not a palindrome")
