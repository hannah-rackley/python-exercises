name = raw_input("WHAT IS YOUR NAME?\n")
# Make input capitalized.
caps_name = name.upper()
# Get length of the input.
length = len(name)
#Remove any spaces from the letter count.
space = " "
space_count = name.count(space, 0, len(name))
if " " in name:
    for i in range(space_count):
      length = length - 1

# Greet user with capitalized name and our string.
print "HELLO, %s!" % caps_name
# Tell the user how many letters are in the name they inputed.
print "YOUR NAME HAS %s LETTERS IN IT! AWESOME!" % length