sentence = raw_input("Please enter a word: ")
words = sentence.split(" ")
dictionary = {}


for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
    
dict_array = dictionary.items()

top = ['', 0]
second = ['', 0]
third = ['', 0]

for item in dict_array:
    if item[1] > top[1]:
        third = second
        second = top
        top = item
    elif item[1] > second[1]:
        third = second
        second = item
    elif item[1] > third[1]:
        third = item

print "top value: " + str(top) + "second value" + str(second) + "third value:" + str(third)