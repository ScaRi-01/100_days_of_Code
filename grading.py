student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_grades = {}

for key, value in student_scores.items():
    if value<101 and value > 90:
        student_grades[key] = 'Outstanding'
    elif value<91 and value > 80:
        student_grades[key] = 'Exceeds Expectations'
    elif value<81 and value > 70:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'

print(student_grades)