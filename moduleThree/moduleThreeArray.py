# import python numpy module
import numpy as np

# Create an array of class students using numpy
# List also suits this scenario for storing the students but using numpy arrays just for the topic

students = np.array(['James Blank', 'Brett Hergenreter', 'Tilak Dash', 'George Curley', 'David Wieseler', 'Sajith Joseph',
            'Nicholas Crissie', 'Michael Bass', 'Dustin Hicks', 'Jegan Palaniyandi', 'Prema Venkatesan', 'Justin Koch',
            'Dennis Foley', 'Thomas Fugelsang', 'Joshua Lewis', 'Kaelen Woodruff', 'Charles Crittenden',
            'Murtadha AL Ismaiel'])

print()
print("*"*65)
print(" "*10 + "Module Two - discussion submission metrics")
print("*"*65+"\n")

print('\nTotal number of students in the class --> ' + str(len(students))+"\n")

print("Order of submission")
print("-"*19)
# print all the students
for i in range(0, len(students)):
    print(students[i], end="\n")

print()
# Using slicing to print the first three students
print('First three students who submitted in the discussion forum --> ', end='')
print(students[:3])
print()

# using slice again to print last three submitted students
print('Three students who meticulously(last) submitted in the discussion forum --> ', end='')
print(students[-3:])
print()

# Finding the position of someone from the list
position = np.where(students == 'Jegan Palaniyandi')[0]
print(f"Jegan submitted as {position}-th student in the module two discussion forum.\n")
