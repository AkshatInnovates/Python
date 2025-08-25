dictionary = {'Alice':85,
              'Bob':90,
              'Charlie':78,
              'David':92,
              'Eva':88}
name = input("Enter the student's name:")
if name in dictionary:
    print(f"{name}'s marks: {dictionary[name]}")
else:
    print("Student not found.")