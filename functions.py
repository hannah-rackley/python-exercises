
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

print "Sum of numbers: %s" % find_sum(numbers)

#Largest Number
def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print "Largest number: %s" % largest_number(numbers)

#Smallest Number
def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

print "Smallest number: %s" % smallest_number(numbers)

#Even Numbers
def even_number(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print "Even numbers: %s" % even_number(numbers)

#Positive Numbers
def positive_numbers(numbers):
    positives = []
    for number in numbers:
        if number > 0 :
            positives.append(number)
    return positives

print "Positive numbers: %s" % positive_numbers(numbers)

#Positive Numbers II
def positive_numbers2(numbers):
    new_list = []
    for number in numbers:
        if number > 0:
            new_list.append(number)
    return new_list

print "Positive numbers: %s" % positive_numbers2(numbers)

#Multiply a list
def multiply_list(numbers, factor):
    new_list = []
    for number in numbers:
        new_list.append(number * factor)

    return new_list

print "List multiplied by a factor: %s" % multiply_list(numbers, factor)

#Multiply Vectors
def multiply_vectors(list_one, list_two):
    new_list = []
    for i in range(len(list_one)):
        new_list.append(list_one[i] * list_two[i])

    return new_list

print "Two lists multiplied by each other: %s" % multiply_vectors(list_one, list_two)

#Matrix addition
matrix1 = [[0, 1], [2, 3]]
matrix2 = [[0, 2], [3, 5]]

width = len(matrix1[0])
height = len(matrix1)

def add_matrices(matrix1, matrix2):
    width = len(matrix1[0])
    height = len(matrix1)
    empty_matrix = []
    for i in range(0, height):
        empty_matrix.append([])
        for j in range(0, width):
            empty_matrix[i].append(0)
    matrix = empty_matrix
    for i in range(height):
        for j in range(width):
            sum = matrix1[i][j] + matrix2[i][j]
            matrix[i][j] = sum
    return matrix

result = add_matrices(matrix1, matrix2)

print "Sum of matrices: %s" % result

#De-up
def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

print "List without duplicates: %s" % remove_duplicates(lst)


#Matrix multiplication:
# matrix1 = [[1, 2, 3], [4]]
# matrix2 = [[1, 2, 3], [2]]
# final_matrix = []

# for i in range(len(matrix1)):
#     final_matrix.append([])
#     for j in range(len(matrix1[i])):
#         for k in range(len(matrix2)):
#         final_matrix[i].append(matrix1[i][j] * matrix2[i][j])
# print final_matrix