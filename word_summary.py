sentence = raw_input("Please enter a word: ")
words = sentence.split(" ")
dictionary = {}

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
print dictionary

#Create a replacement for split
sentence = raw_input("Please enter a lowercase statement with no punctuation: ")
sentence_ = sentence + " "
words = []
current_word = ""

for letter in sentence_:
    if letter == " ":
        words.append(current_word)
        current_word = ""
    else: 
        current_word += letter

print words



