import time
#Print a square
square = []
for x in range(5):
    square.append(["*"] * 5)
for row in square:
    print "".join(row)

#method 2 - with no for loop
x = 0
while x < 5:
    print ("*" * 5)
    x += 1

#Print a square II
square = []
n = int(raw_input("How big is the square? "))
for x in range(n):
    square.append(["*"] * n)
for row in square:
    print "".join(row)

#Print a box
box = []
width = int(raw_input("Width? "))
height = int(raw_input("Height? "))
one_less = height - 1
middle = width -2
middle_row = " " * middle
middle_rows = ["*"] + ([" "] * middle) + ["*"]

for y in range(height):
    if y == 0 or y == one_less:
        box.append(["*"] * width)
    else:
        box.append(middle_rows)
        
for row in box:
    print "".join(row)

#method 2 - no for loops
y = 0
while y < height:
    if y == 0 or y == one_less:
        print ("*" * width)
        y += 1
    else:
        print ("*%s*" % middle_row)
        y += 1

#Print a triangle/ Print a triangle II
triangle = []
height = int(raw_input("Height? "))
base_stars = height + (height - 1)
spaces = base_stars - 1
star_count = 1
spaces_around = spaces/2

while spaces_around > -1:
    spaces_printed = [" "] * spaces_around
    stars_printed = ["*"] * star_count
    triangle.append(spaces_printed + stars_printed + spaces_printed)
    star_count = star_count + 2
    spaces_around = spaces_around - 1

for row in triangle:
    print "".join(row)
#method 2
height = int(raw_input("Height? "))
i = 1
spaces = (height * 2) - 2
j = spaces/2

while i <= height:
    while j >= 0:
        print (j * " ") + (i * "*") + (j * " ")
        j -= 1
        i += 2

#Multiplication Table
table = []
numbers = []
n = int(raw_input("Enter number for multiplication table: "))
string = ("%d X %d = ")

for x in range(1, (n + 1)):
    numbers.append(x)
for num in numbers:
    init_num = 1
    table.append("--------")
    while init_num <= n:
        amount = str(num * init_num)
        table.append(string % (num, init_num) + amount)
        init_num = init_num + 1

for i in table:
    print i

#method 2
n = 1
x = 1
while x < 11:
    while n < 11:
        print "%d X %d = %d" % (x, n, (n*x))
        n += 1
    x += 1
    n = 1
    print "--------"

#method 3
n = 1
m = 1
x = int(raw_input("Number for multiplication table? "))
while n < (x + 1):
    while m < (x + 1):
        print "%d X %d = %d" % (n, m, (m*n))
        m += 1
    n += 1
    m = 1
    print "--------"

#Print a banner
box = []
text = raw_input("Text? ")
width = len(text) + 2

for y in range(3):
    if y == 1:
        box.append("*%s*" % text)
    else:
         box.append(["*"] * width)
        
for row in box:
    print "".join(row)
#Method 2
y = 0
while y < 3:
    if y == 0:
        print ("*" * width)
        y +=1
    elif y == 1:
        print ("*%s*" % text)
        y += 1
    else:
        print ("*" * width)
        y += 1

#Print triangular number
number = 1
total = 0
numbers = []
triangular_number = int(raw_input("Enter number here: "))
while number <= triangular_number:
    total = total + number
    number = number + 1
    numbers.append(total)
for num in numbers:
    print num

#Factor a number
number = int(raw_input("Please enter number to determine its factors: "))
factors = []
for x in range(1, number + 1):
    if number % x == 0:
        factors.append(x)
print factors

init_num = int(raw_input("Enter starting countdown number: "))

while init_num <= 0 or init_num > 20:
    init_num = int(raw_input("Oh no! That number is not a valid entry! Please enter a number between 0 and 21: "))
for i in range(init_num, -1, -1):
    if i == 0 :
        print "Blastoff!"
    else:
        print i
        time.sleep(1)

    

    
