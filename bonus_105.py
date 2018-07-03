import time

init_num = raw_input("Enter starting countdown number: ")

def check_error(init_num):
    while True:
       try:
           int(init_num)
       except ValueError:
           init_num = raw_input("Oh no! You did not enter a number. Please enter a positive number: ")
       else:
           init_num = int(init_num)
           break
    return init_num

final_num = check_error(init_num)

while final_num >= 21 or final_num <= 0:
    if final_num >= 21:
        init_num = raw_input("Oh no! Your number was too large. Please enter a number less than 20: ")
        final_num = check_error(init_num)
    elif final_num <= 0:
        init_num = raw_input("Oh no! You entered a negative number. Please enter a positive number: ")
        final_num = check_error(init_num)

for i in range(final_num, -1, -1):
   if i == 0 :
       print "Blastoff!"
   else:
       print i
       time.sleep(1)