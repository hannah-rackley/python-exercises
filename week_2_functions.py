#Word Histogram
def get_sentence():
    sentence = raw_input("Please enter a sentence with no punctuation: ")
    return sentence

def get_word_count():
    sentence = get_sentence()
    words_in_sentence = sentence.split(" ")
    dictionary = {}
    for word in words_in_sentence:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

print get_word_count()

#Leetspeak with cheater methods
def get_string():
    string = raw_input("Please enter some text: ")
    return string
    
def make_leetspeak():
    string = get_string()
    final_string = ""
    leet_dictionary = {
        "A": "4",
        "E": "3",
        "G": "6",
        "I": "1",
        "O": "0",
        "S": "5",
        "T": "7"
    }
    for character in string:
        upper_character = character.upper()
        if upper_character in leet_dictionary:
            character = leet_dictionary[upper_character]
        
        final_string += character
    return final_string
    
print make_leetspeak()

# Madlib
def get_madlib_input():
    print "Please fill in the blanks below:\n" + "___name____'s favorite animal is _____animal____."
    name = raw_input("What is your name?\n")
    animal = raw_input("What is you favorite animal?\n")
    return {
        "name": name, 
        "animal": animal
        }

def build_mad_lib():
    inputs = get_madlib_input()
    return "%s's favorite animal is the %s." % (inputs["name"], inputs["animal"])

print build_mad_lib()
