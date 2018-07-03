#Uppercase a string
string = raw_input("Please enter some text: ")
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
new_string = ""

for char in string:
    if char in uppercase:
        new_string += char
    elif char in lowercase:
        for j in range(len(lowercase)):
            if lowercase[j] == char:
                new_string += uppercase[j]
                break
    else:
        new_string += char
print new_string

#Capitalize a string
string = raw_input("Please enter some text: ")
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
new_string = ""
capitalized = True

for char in string:
    if char == " ":
        capitalized = True
        new_string += char
    if capitalized:
        if char in uppercase:
            new_string += char
            capitalized = False
        elif char in lowercase:
            for j in range(len(lowercase)):
                if lowercase[j] == char:
                    new_string += uppercase[j]
                    capitalized = False
                    break
 #If after first letter in word   
    else:  
        if char in lowercase:
            new_string += char
        elif char in uppercase:
            for j in range(len(lowercase)):
                if uppercase[j] == char:
                    new_string += lowercase[j]
                    break       
        
print new_string

#Reverse a String
string = raw_input("Please enter some text: ")
new_string = ""

for i in range((len(string)-1), -1, -1):
    new_string += string[i]

print new_string

#Leetspeak
string = raw_input("Please enter some text: ")
new_string = ""
final_string = ""
letters = "aegiost"
numbers = "4361057"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxzy"

for char in string:
    if char in lowercase:
        new_string += char
    elif char in uppercase:
        for j in range(len(lowercase)):
            if uppercase[j] == char:
                new_string += lowercase[j]
                break
    else:
        new_string += char

for character in new_string:
    if character in letters:
        for l in range(len(letters)):
            if character == letters[l]:
                final_string += numbers[l]
                break
    else: 
        final_string += character

print final_string

#Long-long vowels
string = raw_input("Please enter some text: ")
vowels = "AEIOUaeiou"
new_string = ""
vowel = False

for i in string:
    if vowel and vowel_ == i:
        new_string += (i * 3)
        vowel = False
    if i in vowels:
        new_string += i
        vowel = True
        vowel_ = i
    else:
        new_string += i

print new_string
#Caesar Cipher
string = "lbh zhfg hayrnea jung lbh unir yrnearq"
new_string = ""
final_string = ""
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

for i in string:
    if i in lowercase:
        new_string = new_string + i
    elif i in uppercase:
        for j in range(len(lowercase)):
            if uppercase[j] == i:
                new_string += lowercase[j]
                break
    else:
        new_string += i

for k in new_string:
    if k not in lowercase:
        final_string += k
    for l in range(len(lowercase)):
        if k == lowercase[l]:
            if l > 12:
                shift = l - 13
            else:
                shift = l + 13
            final_string += lowercase[shift]

print final_string

string = "lBh zHfg hayrnea junG lBh uNir yrnearq"
new_string = ""
final_string = ""
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

for k in string:
    if k not in lowercase and k not in uppercase:
        final_string += k
    else:
        for l in range(len(lowercase)):
            if k == lowercase[l]:
                shift = (l + 13) % 26
                final_string += lowercase[shift]
            if k == uppercase[l]:
                shift = (l + 13) % 26
                final_string += uppercase[shift]
    
print final_string
    

