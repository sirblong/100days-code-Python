# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height