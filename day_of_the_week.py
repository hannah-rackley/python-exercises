day = int(raw_input('Day (0-6)?\n'))

days = {
    0: "Sunday", 
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

if day in days:
    print days[day]
else:
    print "That is not a valid input."