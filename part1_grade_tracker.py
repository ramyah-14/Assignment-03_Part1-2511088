# Task 1 — Data Parsing


raw_students = [
    {"name": " ayesha SHARMA ",  "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": " Priya Nair ",      "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

for student in raw_students:
    # Clean the name: remove spaces from start/end, inconsistent casing
    clean_name = student["name"].strip().title()


    # Convert roll number from text to a real number
    clean_roll = int(student["roll"])


    # Split the marks string into a list of numbers
    # e.g. "88, 72, 95" becomes [88, 72, 95]
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]


    # Check each word in the name contains only letters
    words = clean_name.split()
    is_valid = all(word.isalpha() for word in words)
    if is_valid:
        print(clean_name + " — ✓ Valid name")
    else:
        print(clean_name + " — ✗ Invalid name")


    # Print the profile card
    print("================================")
    print(f"Student : {clean_name}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("================================")

#  find roll 103 and print name in CAPS and lowercase
for student in raw_students:
    if student["roll"] == "103":
        name_103 = student["name"].strip().title()
        print("CAPS:", name_103.upper())
        print("lowercase:", name_103.lower())




# Task 2 — Marks Analysis
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"\nMarks report for {student_name}")
for i in range(len(subjects)):
    m = marks[i]
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"  {subjects[i]}: {m}  →  {grade}")

total = sum(marks)
average = round(total / len(marks), 2)
highest_index = marks.index(max(marks))
lowest_index  = marks.index(min(marks))

#printing the total, average, highest and lowest marks
print(f"\nTotal marks  : {total}")
print(f"Average      : {average}")
print(f"Highest      : {subjects[highest_index]} ({max(marks)})")
print(f"Lowest       : {subjects[lowest_index]} ({min(marks)})")

#Simulating Mark entry system
new_count = 0
while True:
    subject_input = input("\nEnter subject name (or 'done' to stop): ")
    #Break if done is entered
    if subject_input.lower() == "done":
        break
    marks_input = input(f"Enter marks for {subject_input} (0-100): ")
    try:
        new_marks = int(marks_input)
        if 0 <= new_marks <= 100:
            subjects.append(subject_input)
            marks.append(new_marks)
            new_count += 1
        else:
            print("Warning: marks must be between 0 and 100")
    except ValueError:
        print("Warning: please enter a number, not text")

#Updated details and average after new subject addition
print(f"\nNew subjects added: {new_count}")
print(f"Updated average: {round(sum(marks)/len(marks), 2)}")


# Task 3 — Class Performance
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

#Formatted Class Report
print(f"\n{'Name':<15} | {'Average':>7} | Status")
print("-" * 38)

#Class Performance Table
results = []
for name, student_marks in class_data:
    avg = round(sum(student_marks) / len(student_marks), 2)
    status = "Pass" if avg >= 60 else "Fail"
    results.append((name, avg, status))
    print(f"{name:<15} | {avg:>7.2f} | {status}")

passed_count = sum(1 for _, _, s in results if s == "Pass")
failed_count = len(results) - passed_count
topper = max(results, key=lambda x: x[1])
class_avg = round(sum(r[1] for r in results) / len(results), 2)

#Overall Class Performance
print(f"\nPassed: {passed_count}   Failed: {failed_count}")
print(f"Class topper: {topper[0]} with {topper[1]}")
print(f"Class average: {class_avg}")

# Task 4 — String Manipulation
essay = " python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "



# Step 1: remove spaces from start and end
clean_essay = essay.strip()


# Step 2: Title Case
print("Title Case:", clean_essay.title())


# Step 3: count how many times 'python' appears
print("Count of 'python':", clean_essay.count("python"))


# Step 4: replace 'python' with 'Python 🐍'
print("Replaced:", clean_essay.replace("python", "Python 🐍"))


# Step 5: split into sentences
sentences = clean_essay.split(". ")
print("Sentences list:", sentences)


# Step 6: print each sentence numbered
for i, sentence in enumerate(sentences, 1):
    if not sentence.endswith("."):
        sentence = sentence + "."
    print(f"{i}. {sentence}")



