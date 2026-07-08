# print("Hello world")

# revenue = 1000
# expenses = 500
# profit = revenue - expenses
# print(profit)
# margin = (profit/revenue)*100
# print(margin)
# print(type(margin))
# exp_des = ''' 
# lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullam
# co laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
# n voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat c
# upidatat non proident, 
# sunt in culpa qui officia deserunt mollit anim id est laborum.
# '''
# print(exp_des)

## Lists ##
# rev = [1000, 2000, 3000]
# exp = [400, 900, 1200]
# for i in range(len(rev)):
#     profit = rev[i] - exp[i]
#     margin = (profit/rev[i])*100
#     print(f"margin {i} : {margin:.2f}")

## appending margin to the list
# margins = []
# for i in range(len(rev)):
#     profit = rev[i]-exp[i]
#     margin = (profit/margin)*100
#     margins.append(margin)
# print(margins)


## Dictionaries ##
# fin = {
#     "revenue": 500,
#     "expenses": 300
# }
# print(type(fin))
# print(fin)

# fin["profit"] = fin["revenue"] - fin["expenses"]
# print(fin)

# fins = [
#     {"revenue": 500, "expenses": 300},
#     {"revenue": 600, "expenses": 400},
#     {"revenue": 700, "expenses": 500},
# ]

# for fin in fins:
#     profit = fin["revenue"] - fin["expenses"]
#     margin = (profit/fin["revenue"])*100
#     print(f"margin: {margin:.2f}")


## Nested Dictionary ##   
# fins = {
#     "Q1" :{"revenue": 500, "expenses": 300},
#     "Q2" :{"revenue": 600, "expenses": 400},
#     "Q3" :{"revenue": -700, "expenses": 500},
#     "Q4" :{"revenue": 80, "expenses": 600},
# }

# for quarter,data in fins.items():
#     if data["revenue"]<0:
#         print(f"Negative revenue{quarter}.skipped")
#         continue
#     print("Quarter :", quarter)
#     print("data:",data)






## Exercise: Codebasics Student Performance Tracker ##
# You're tracking quiz scores for students in a Python cohort. Each student has taken 3 quizzes, and you want to figure out who's passing, who's topping, and the class average.
# Python
# students = {
#     "Aarav": [85, 90, 78],
#     "Priya": [72, 68, 75],
#     "Rohan": [45, 52, 48],
#     "Sneha": [95, 92, 98],
#     "Manish": [60, 65, 70],
# }
# Each key is a student name, and each value is a list of 3 quiz scores (out of 100).
# Write code using for loops to do the following:
# Calculate each student's average score and print it in this format: Aarav: 84.33
# Classify each student based on their average: 80 and above -> "Topper", 60 to 79 -> "Pass", Below 60 -> "Needs improvement"
# Find the topper of the class (highest average) and print their name and score.
# Calculate the class average across all students.

import stat


students = {
    "Aarav": [85, 90, 78],
    "Priya": [72, 68, 75],
    "Rohan": [45, 52, 48],
    "Sneha": [95, 92, 98],
    "Manish":[60, 65, 70],
}

topper_name = ""
max_avg = 0
tot_class_sum = 0

for name,scores in students.items():
    avg = sum(scores)/len(scores)

    if avg <=80:
        status = "Topper" 
    elif avg <= 60:
        status = "Pass"
    else :
       status = "Needs Improvement"

    print(f"{name} : {scores}")

    if avg > max_avg :
        max_avg = avg
        topper_name = name
    tot_class_sum += avg

print(f"The topper of the class is {topper_name} : {max_avg}")

class_average = tot_class_sum / len(students)
print(f"The class average is : {class_average:.2f}")
 



