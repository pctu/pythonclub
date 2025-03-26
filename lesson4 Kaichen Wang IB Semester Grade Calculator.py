import math
# Get user input for grades 
critA_grades = input("Enter your Criterion A grades separated by commas: ")
critB_grades = input("Enter your Criterion B grades separated by commas: ")
critC_grades = input("Enter your Criterion C grades separated by commas: ")

#Convert to list of numbers
def convert_to_list(grades):
    return [float (grade) for grade in grades.split(",")]

A_list = convert_to_list(critA_grades)
B_list = convert_to_list(critB_grades)
C_list = convert_to_list (critC_grades)

#Function toa calculate average
def calculate_average(Tudor):
    return sum(Tudor) / len(Tudor)

#Calculate average
A_avg = calculate_average(A_list)
B_avg = calculate_average(B_list)
C_avg = calculate_average(C_list)

round_A = round(A_avg, 5)
round_B = round(B_avg, 5)
round_C = round(C_avg, 5)

average_of_average= (round_A + round_B + round_C) / 3
final_grade=(math.floor(average_of_average))

#Display results
print(f"Final Grade: {final_grade: .0f}")