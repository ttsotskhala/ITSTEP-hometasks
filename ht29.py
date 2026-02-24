import mysql.connector

# კავშირი MySQL-სთან
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="HuaMulan_2025",
    database="hw29"
)

cursor = conn.cursor()

# ცხრილის შექმნა
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    studentID INT AUTO_INCREMENT PRIMARY KEY,
    studentLastName VARCHAR(50),
    studentFirstName VARCHAR(50),
    studentAge INT
)
""")

# 5 მონაცემის დამატება
students_data = [
    ("აბულაძე", "გრიგოლ", 31),
    ("აბაშიძე", "ანა", 25),
    ("ლომიძე", "კახა", 26),
    ("შალიკაშვილი", "ვანო", 29),
    ("კახიძე", "ნინო", 24)
]

cursor.executemany(
    "INSERT INTO Students (studentLastName, studentFirstName, studentAge) VALUES (%s, %s, %s)",
    students_data
)
conn.commit()

# დაბეჭდვა ეკრანზე
print("საწყისი მონაცემები:")
cursor.execute("SELECT * FROM Students")
for row in cursor.fetchall():
    print(row)

# დამატება (კახიძე კოტე)
cursor.execute(
    "INSERT INTO Students (studentLastName, studentFirstName, studentAge) VALUES (%s, %s, %s)",
    ("კახიძე", "კოტე", 27)
)
conn.commit()

# დალაგება ანბანის მიხედვით: გვარი, სახელი
print("\n საბოლოო შედეგი (დალაგებული):")
cursor.execute("""
SELECT * FROM Students
ORDER BY studentLastName ASC, studentFirstName ASC
""")

for row in cursor.fetchall():
    print(row)

# კავშირის დახურვა
cursor.close()
conn.close()