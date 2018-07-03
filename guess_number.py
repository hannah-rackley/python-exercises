import random
secret_number = random.randint(1, 10)
guess = int(raw_input("I am thinking of a number between 1 and 10.\nYou have 5 guesses left.\nWhat's the number? "))
guesses_left = 5
play_again = "Y"

while play_again == "Y":
    while guess != secret_number and guesses_left > 1:
        guesses_left -= 1
        if guess < secret_number:
            guess = int(raw_input("%i is too low.\nWhat's the number? " % guess))
            print "You have %i guesses left." % guesses_left
        else:
            guess = int(raw_input("%i is too high.\nWhat's the number? " % guess))
            print "You have %i guesses left." % guesses_left
    if guesses_left == 1:
        if guess < secret_number:
            print ("%i is too low.\nYou ran out of guesses!" % guess)
        else:
            print ("%i is too high.\nYou ran out of guesses!" % guess)
        play_again = raw_input("Do you want to play again (Y or N)? ")
        if play_again == "Y":
            guesses_left = 5
    if guess == secret_number:
        print "Yes! You win!"
        play_again = raw_input("Do you want to play again (Y or N)? ")
        if play_again == "Y":
            guesses_left = 5
else: 
    print "Bye!"

