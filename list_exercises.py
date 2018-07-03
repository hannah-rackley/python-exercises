numbers = [-2, -1.3, -.4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 25, 36, 43, 54]
list_one = [0, 1, 3, 6, 10]
list_two = [9, 6, 4, -8, 10]
factor = 6
lst  = ["2", "2", "hello", "goodbye", 3, 5, 6, 3, "Hello"]

#Sum the Numbers
def find_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print find_sum(numbers)

#Largest Number
def largest_number(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print largest_number(numbers)

#Smallest Number
def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

print smallest_number(numbers)

#Even Numbers
def even_number(numbers):
    evens = []
    for number in numbers:
        if number > 0:
            if number % 2 == 0:
                evens.append(number)
    return evens

print even_number(numbers)

#Positive Numbers
def positive_numbers(numbers):
    positives = []
    for number in numbers:
        if number > 0 :
            positives.append(number)
    return positives

positive_numbers(numbers)

#Positive Numbers II
def positive_numbers2(numbers):
    new_list = []
    for number in numbers:
        if number > 0:
            new_list.append(number)
    return new_list

print positive_numbers2(numbers)

#Multiply a list
def multiply_list(numbers, factor):
    new_list = []
    for number in numbers:
        new_list.append(number * factor)
    return new_list

print multiply_list(numbers, factor)

#Multiply Vectors
def multiply_vectors(list_one, list_two):
    new_list = []
    for i in range(len(list_one)):
        new_list.append(list_one[i] * list_two[i])
        i += 1
    return new_list

print multiply_vectors(list_one, list_two)

#Matrix Addition
m1 = [[0, 1], [2, 3]]
m2 = [[0, 2], [3, 5]]
r = []
for row in m1:
    wip = []
    for col in row:
        wip.append(0)
    r.append(wip)

width = len(r[0])
height = len(r)

for i in range(height):
    for j in range(width):
        sum = m1[i][j] + m2[i][j]
        r[i][j] = sum
print r

#De-up
def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
print new_list


#Matrix multiplication:
matrix1 = [[1, 2, 3], [4]]
matrix2 = [[1, 2, 3], [2]]
final_matrix = []

for i in range(len(matrix1)):
    final_matrix.append([])
    for j in range(len(matrix1[i])):
        for k in range(len(matrix2)):
        final_matrix[i].append(matrix1[i][j] * matrix2[i][j])
print final_matrix

