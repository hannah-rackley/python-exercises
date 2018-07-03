bill = raw_input("Total bill amount? ")
while True:
    try:
        float(bill)
    except ValueError:
        bill = raw_input("Oh no! You did not enter a number. Please enter a positive number: ")
    else:
        bill = float(bill)
        break

while bill <= 0:
    bill = float(raw_input("Oh no! You entered a negative number. Please enter a positive number: "))

service = raw_input("Level of service? ")
service_options = ["good", "fair", "poor"]

while service not in service_options:
    service = raw_input("Please enter 'good', 'fair', or 'poor': ")

split = int(raw_input("Split how many ways? "))

if service == "good":
    tip = 0.20 * bill
elif service == "fair":
    tip = 0.15 * bill
elif service == "poor":
    tip = 0.10 * bill

total = bill + tip
amount = total/split
check_amount = (round(amount, 2) * split)
difference = (total - check_amount)

print "Tip Amount: $%.2f" % tip
print "Total Amount: $%.2f" % total
print "Amount per person: $%.2f" % amount

if difference != 0:
    odd_amount = amount + difference

print "Odd amount for person: $%.2f" % odd_amount