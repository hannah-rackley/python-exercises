string = raw_input("Please enter some text: ")
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
new_string = ""

for char in string:
    letter = char
    for j in range(len(lowercase)):
        if lowercase[j] == char:
            letter = uppercase[j]
            break
    new_string += letter

print new_string
