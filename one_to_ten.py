#1 to 10
for i in range(1, 11):
    print i

#n to m
start_number = int(raw_input("Please enter starting number here: "))
end_number = int(raw_input("Please enter ending number here: "))

while end_number < start_number:
    print "Uh-oh! Your numbers cannot create a proper range. Please make sure your end number is larger than your start number."
    start_number = int(raw_input("Please enter starting number here: "))
    end_number = int(raw_input("Please enter ending number here: "))

for i in range(start_number, (end_number + 1)):
    print i

#Odd Numbers
for i in range(1, 11, 2):
    print i
for i in range(start_number, end_number):
    if i % 2 != 0:
        print i

#How many coins?
coins = 0
another = "yes"

while another == "yes":
    if coins == 1:
        print "You have 1 coin."
        another = raw_input("Do you want another? ")
        coins = coins +1
    else:
        print "You have %d coins." % coins
        another = raw_input("Do you want another? ")
        coins = coins + 1
else: 
    print "Bye."
