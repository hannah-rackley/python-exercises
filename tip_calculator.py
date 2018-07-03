bill = raw_input("Total bill amount? ")
while True:
    try:
        float(bill)
    except ValueError:
        bill = raw_input("Oh no! That is not a number. Please enter a positive number: ")
    else:
        bill = float(bill)
        break

while bill <= 0:
    bill = float(raw_input("Oh no! You entered a negative number. Please enter a positive number: "))

service = raw_input("Level of service? ")
service_options = ["good", "fair", "poor"]

while service not in service_options:
    service = raw_input("Please enter 'good', 'fair', or 'poor': ")

if service == "good":
    tip = 0.20 * bill
elif service == "fair":
    tip = 0.15 * bill
elif service == "poor":
    tip = 0.10 * bill

total = bill + tip
print "Tip Amount: $%.2f" % tip
print "Total Amount: $%.2f" % total
