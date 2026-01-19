--  თუ არ გაქვთ შექმნილი, შექმენით მონაცემთა ბაზა სახელად hw_26  და შეასრულეთ შემდეგი დავალებები:
CREATE DATABASE if NOT EXISTS hw_26;

USE hw_26;
-- 1. დაწერეთ SQL, რომელიც შექმნის Authors ცხრილს, რომელსაც ექნება პირველადი გასაღები
CREATE TABLE Authors(
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL
);
-- 2. დაწერეთ SQL, რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID 
CREATE TABLE Books(
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(100) NOT NULL,
    PublishYear INT,
    AuthorID INT,
    Foreign Key (AuthorID) REFERENCES Authors(AuthorID)
);
-- 3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს
INSERT INTO Authors(`FirstName`, `LastName`, `Country`)
VALUES
('Nodar', 'Dumbadze', 'Georgia'),
('Ernest', 'Hemingway', 'USA'),
('Franz', 'Kafka', 'Czech Republic'),
('Chabua', 'Amirejibi', 'Georgia'),
('Alexandre', 'Dumas', 'France'),
('Harper', 'Lee', 'USA')
;

INSERT INTO Books(`Title`, `PublishYear`, `AuthorID`)
VALUES
('Data Tutashkhia', 1975, 4),
('The Sunny Night', 1967, 1),
('The White Flags', 1973, 1),
('To Kill a Mockingbird', 1960, 6),
('The Trial', 1925, 2),
('A Country Doctor', 1917, 3),
('Queen Margot', 1845, 4),
('The Count of Monte Cristo', 1846, 4)
;

-- 4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტული ჩანაწერის ერთ-ერთი ველის მნიშვნელობას
UPDATE Books
SET `AuthorID` = 5
WHERE Title = 'The Count of Monte Cristo'
;
UPDATE Books
SET `AuthorID` = 5
WHERE Title = 'Queen Margot'
;

-- 5. დაწერეთ SQL, რომელიც დაბეჭდავს გაერთიანებულ ცხრილებს
SELECT `Title`, `PublishYear`, `FirstName`, `LastName`, `Country`
FROM Books
JOIN Authors ON authors.`AuthorID` = books.`AuthorID`
;

-- 6. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან
TRUNCATE TABLE Books;
TRUNCATE TABLE Authors;

-- 7. წაშალეთ Author და Books ცხრილები
DROP TABLE Books;
DROP TABLE Authors;
