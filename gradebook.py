#This project is a simple gradebook application that allows users to add students, add grades, and calculate averages.

#Subject list
subjects = ["physics", "calculus", "potery", "history"]

#Grades
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["potery", 85], ["history", 88]]
print(gradebook)

#Adding a new subject and grade

gradebook.append(["Computer Science", 100])
print(gradebook)

gradebook.append(["Visual arts", 93])
print(gradebook)

gradebook[-1][1] = 98  # Update the last grade
print(gradebook)

# Swapping a grade number for pass/fail
gradebook[2].remove(85)
print(gradebook)
gradebook[2].append("pass")
print(gradebook)

#Adding two lists
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)