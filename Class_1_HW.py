user_name = input("What is your name: ")
user_age = input("What about your age: ")
user_roll = input("Tell me your roll: ")
bangla_mark = int(input("Your marks in bangla: "))
english_mark = int(input("Your marks in english: "))
math_mark = int(input("Your marks in math: "))

print(" ")
print("Student Report:")
print("-----------------------")
print("Name: ", user_name)
print("Age: ", user_age)
print("Roll Number: ", user_roll)

total_marks = bangla_mark + english_mark + math_mark

print("Your total marks is: ",total_marks)
print("Your average marks is: ", total_marks/3)