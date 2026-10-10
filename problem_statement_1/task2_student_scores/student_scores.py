import requests
import csv
from io import StringIO
import matplotlib.pyplot as plt

API_URL = "https://api.datapoint.market/r/data37/student-performance"

response = requests.get(API_URL)
response.raise_for_status()

reader = csv.DictReader(StringIO(response.text))
students = list(reader)

print(f"Number of students: {len(students)}")
print(f"First student: {students[0]}")

scores = []

for student in students:
    g3_score = student.get('G3')
    if g3_score is not None:
            g3_score = int(g3_score)
            scores.append(g3_score)
average_score = sum(scores) / len(scores) if scores else 0
print(f"Average G3 score: {average_score:.2f}")   

student_labels = [f"Student {i+1}" for i in range(len(scores))]
plt.figure(figsize=(12, 6))
plt.bar(student_labels, scores, color='skyblue')
plt.xlabel('Students')
plt.ylabel('G3 Scores')
plt.title('G3 Scores of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()