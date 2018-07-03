letter_mapping = {
   "A": "a",
   "B": "b",
   "C": "c",
   "D": "d",
   "E": "e",
   "F": "f",
   "G": "g",
   "H": "h",
   "I": "i",
   "J": "j",
   "K": "k",
   "L": "l",
   "M": "m",
   "N": "n",
   "O": "o",
   "P": "p",
   "Q": "q",
   "R": "r",
   "S": "s",
   "T": "t",
   "U": "u",
   "V": "v",
   "W": "w",
   "X": "x",
   "Y": "y",
   "Z": "z"
}

#Leet speak
string = raw_input("Please enter some text: ")
new_string = ""
final_string = ""
letters = "aegiost"
numbers = "4361057"
leet_cipher = { 
    "a": "4",
    "e": "3",
    "g": "6",
    "i": "1",
    "o": "0",
    "s": "5",
    "t": "7"
}

for char in string:
    if char in letter_mapping:
        new_string += letter_mapping[char]
    else:
        new_string += char

for character in new_string:
    if character in leet_cipher:
        final_string += leet_cipher[character]
    else: 
        final_string += character

print final_string


