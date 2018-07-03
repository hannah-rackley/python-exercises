day = int(raw_input('Day (0-6)?\n'))

if day in range(1, 5):
    print "Go to work"
elif day == 0 or day == 6:
    print "Sleep in"
else:
    print "That is not a valid input."