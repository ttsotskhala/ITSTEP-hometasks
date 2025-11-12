import csv, time

# ფაილის მისამართი
FILE_PATH = 'students.csv'

# სვეტების სახელები
FIELDNAMES = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']

# საწყისი მონაცემები
data = [
    {'id': 1, 'name': 'Nino', 'age': 20, 'grade': '2', 'subject_name': 'Math', 'mark': 95},
    {'id': 2, 'name': 'Giorgi', 'age': 21, 'grade': '3', 'subject_name': 'Physics', 'mark': 87},
    {'id': 1, 'name': 'Nino', 'age': 20, 'grade': '2', 'subject_name': 'Physics', 'mark': 88},
    {'id': 2, 'name': 'Giorgi', 'age': 21, 'grade': '3', 'subject_name': 'Math', 'mark': 92},
    {'id': 3, 'name': 'Kirile', 'age': 21, 'grade': '3', 'subject_name': 'Physics', 'mark': 91},
    {'id': 3, 'name': 'Kirile', 'age': 21, 'grade': '3', 'subject_name': 'Math', 'mark': 93},
    ]

# ფაილის შექმნა
with open(FILE_PATH, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
    writer.writeheader()                             # ჩავწეროთ სვეტების სათაურები
    writer.writerows(data)                           # ჩავწეროთ სტუდენტების მონაცემები

print("CSV ფაილი წარმატებით შეიქმნა:", FILE_PATH)
time.sleep(2)


# === 1. ახალი სტუდენტის დამატება (ან ახალი საგნის არსებულ სტუდენტთან) ===
def add_student():
    student_id = input("შეიყვანეთ სტუდენტის ID: ")

    data = []
    try:
        with open(FILE_PATH, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        pass

    # ID-ის მიხედვით სტუდენტის შემოწმება
    existing = [row for row in data if row['id'] == student_id]

    if existing:
        existing_student = existing[0]
        print(f"ID {student_id}-ის მქონე სტუდენტი ნაპოვნია: {existing_student['name']}, "
              f"{existing_student['age']} წლის, {existing_student['grade']} კურსი.")

        # ასაკისა და კურსის შემოწმება
        name_check = input("შეიყვანეთ სტუდენტის სახელი (შესამოწმებლად): ")
        age_check = input("შეიყვანეთ სტუდენტის ასაკი (შესამოწმებლად): ")

        if name_check != existing_student['name'] or age_check != existing_student['age']:
            print("შეცდომა: სახელი და ასაკი არ ემთხვევა არსებული სტუდენტის მონაცემებთან!")
            return

        # ახალი საგნის და ქულის ჩამატება
        subject_name = input("შეიყვანეთ ახალი საგნის დასახელება: ")
        mark = input("შეიყვანეთ ქულა: ")

        new_row = {
            'id': student_id,
            'name': existing_student['name'],
            'age': existing_student['age'],
            'grade': existing_student['grade'],
            'subject_name': subject_name,
            'mark': mark
        }
        data.append(new_row)

    else:
        # ახალი სტუდენტის დამატება
        new_student = {
            'id': student_id,
            'name': input("შეიყვანეთ სახელი: "),
            'age': input("შეიყვანეთ ასაკი: "),
            'grade': input("შეიყვანეთ კურსი: "),
            'subject_name': input("შეიყვანეთ საგნის დასახელება: "),
            'mark': input("შეიყვანეთ ქულა: ")
        }
        data.append(new_student)

    # სორტირება და ჩაწერა
    data.sort(key=lambda x: int(x['id']))
    with open(FILE_PATH, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)

    print("სტუდენტი ან ახალი საგანი წარმატებით დაემატა\n")


# === 2. სტუდენტების წაკითხვა ===
def read_students(student_id=None):
    try:
        with open(FILE_PATH, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students = list(reader)

            if not students:
                print("ფაილი ცარიელია")
                return

            if student_id:
                found = [s for s in students if s['id'] == str(student_id)]
                if found:
                    print(f"\n{student_id} ID-ის მქონე სტუდენტზე ინფორმაცია:")
                    for row in found:
                        print(row)
                else:
                    print("აღნიშნული ID-ის მქონე სტუდენტი არ იძებნება.")
            else:
                print("\nყველა სტუდენტი:")
                for row in students:
                    print(row)
    except FileNotFoundError:
        print("ფაილი არაა ნაპოვნი.")


# === 3. საშუალო ქულის გამოთვლა ===
def average_marks_by_subject():
    try:
        with open(FILE_PATH, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            if not data:
                print("ფაილი ცარიელია")
                return

            subjects = {}
            for row in data:
                subj = row['subject_name']
                mark = float(row['mark'])
                subjects.setdefault(subj, []).append(mark)

            print("\nსაგნების მიხედვით საშუალო ქულები:")
            for subj, marks in subjects.items():
                avg = sum(marks) / len(marks)
                print(f"{subj}: {avg:.2f}")
    except FileNotFoundError:
        print("ფაილი არაა ნაპოვნი.")


# === 4. საგნის ქულის განახლება ===
def update_mark():
    student_id = input("შეიყვანეთ სტუდენტის ID: ")
    subject = input("შეიყვანეთ საგნის დასახელება: ")
    new_mark = input("შეიყვანეთ ახალი ქულა: ")

    updated = False

    try:
        with open(FILE_PATH, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        for row in data:
            if row['id'] == student_id and row['subject_name'].lower() == subject.lower():
                row['mark'] = new_mark
                updated = True
                break

        if updated:
            with open(FILE_PATH, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(data)
            print("ქულა წარმატებით განახლდა.\n")
        else:
            print("სტუდენტი ან საგანი არაა ნაპოვნი.\n")

    except FileNotFoundError:
        print("ფაილი არაა ნაპოვნი.")


# === გამოყენება ===
if __name__ == "__main__":
    while True:
        print("\n მენიუ:")
        print("1. ახალი სტუდენტის დამატება (ან ახალი საგნის არსებულ სტუდენტთან)")
        print("2. ყველა სტუდენტის ჩვენება")
        print("3. ID-ის მიხედვით კონკრეტული სტუდენტის ჩვენება")
        print("4. საგნის მიხედვიტ საშუალო ქულის ჩვენება")
        print("5. ქულის განახლება")
        print("0. გამოსვლა")

        choice = input("აირჩიეთ მოქმედება: ")

        if choice == '1':
            add_student()
            time.sleep(2)
        elif choice == '2':
            read_students()
            time.sleep(2)
        elif choice == '3':
            sid = input("შეიყვანეთ სტუდენტის ID: ")
            read_students(student_id=sid)
            time.sleep(2)
        elif choice == '4':
            average_marks_by_subject()
            time.sleep(2)
        elif choice == '5':
            update_mark()
            time.sleep(2)
        elif choice == '0':
            print("პროგრამიდან გამოსვლა.")
            time.sleep(1)
            break
        else:
            print("\n არასწორი არჩევანი. სცადეთ თავიდან.")
            time.sleep(2)
