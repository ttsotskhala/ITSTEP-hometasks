
my_dict = {
    "students": [
        {"id": 20, "name": "Giorgi", "age": 25},
        {"id": 25, "name": "Giorgi", "age": 23},
        {"id": 56, "name": "Nika", "age": 25},
        {"id": 100, "name": "Nika", "age": 22},
        {"id": 1232, "name": "Dato", "age": 22},
        {"id": 846723, "name": "Archili", "age": 32}
    ],
    "subjects": [
        {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
        {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
        {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
        {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
        {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    ]
}

# სტუდენტების ID-ის სიის გამოტანა
student_ids = [str(student.get("id")) for student in my_dict.get("students", [])]
print("სტუდენტების ID:", ", ".join(student_ids))

# მომხმარებლისგან ID-ის მიღება
selected_id = input("აირჩიეთ სტუდენტის ID: ").strip()              #თუ ემთხვევით ზედმეტი სპაეისები დაბეჭდა

# ID-ს მიხედვით სტუდენტის პოვნა
student_info = None
for s in my_dict.get("students", []):
    if str(s.get("id")) == selected_id:
        student_info = s
        break

if student_info:
    print("\nstudent infomration:")
    print(f"ID: {student_info.get('id')}, Name: {student_info.get('name')}, Age: {student_info.get('age')}")
    
    for subject in my_dict.get("subjects", []):
        subject_name = subject.get("name")
        grade = subject.get("grades", {}).get(selected_id)
        print(f"subject: {subject_name}, grade: {grade}")
else:
    print("შეყვანილი ID არასწორია.")
