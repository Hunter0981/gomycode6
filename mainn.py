import numpy as np

# Ask the user to input the number of students and number of subjects
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Create a numpy array to store the marks of each student in each subject
marks = np.zeros((num_students, num_subjects))

# Ask the user to input the marks of each student in each subject
for i in range(num_students):
    print(f"Enter the marks for student {i+1}:")
    for j in range(num_subjects):
        while True:
            try:
                marks[i][j] = float(input(f"Subject {j+1}: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

# Calculate the total marks for each student using the sum() function of numpy
total_marks = np.sum(marks, axis=1)

# Calculate the percentage for each student
percentage = (total_marks / (num_subjects * 100)) * 100

# Calculate the grade for each student using the np.where() function and the grading system
grades = np.where(percentage >= 90, 'A+',
                  np.where(percentage >= 80, 'A',
                           np.where(percentage >= 70, 'B+',
                                    np.where(percentage >= 60, 'B',
                                             np.where(percentage >= 50, 'C', 'F')))))

# Display the result for each student in a tabular format
print("{:<15} {:<15} {:<15} {:<15}".format("Student Name", "Total Marks", "Percentage", "Grade"))
for i in range(num_students):
    print("{:<15} {:<15} {:<15} {:<15}".format(f"Student {i+1}", total_marks[i], percentage[i], grades[i]))
