#1
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"({self.x}, {self.y})"


# მაგალითად:
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (5, 7)

#2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False


# მაგალითად:
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print(book1 == book2)  # True
print(book1 == book3)  # False

#3
class Car:
    def __new__(cls, *args, **kwargs):                                    # __new__ პასუხისმგებელია ობიექტის შექმნაზე მეხსიერებაში
        print(">>> __new__ გამოძახებულია — ობიექტი შეიქმნა მეხსიერებაში")
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):                                # __init__ პასუხისმგებელია ობიექტის ინიციალიზაციაზე (ატრიბუტების მინიჭება)
        print(">>> __init__ გამოძახებულია — ობიექტის ინიციალიზაცია დასრულდა")

        self._brand = None
        self._model = None
        self._year = None

        # setter-ების გამოყენებით ვანიჭებთ საწყის მნიშვნელობებს
        self.brand = brand
        self.model = model
        self.year = year

    # ----------- brand -----------
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError("ბრენდი უნდა იყოს ტექსტური ტიპის (str)")
        if not value.strip():
            raise ValueError("ბრენდი არ შეიძლება იყოს ცარიელი")
        self._brand = value.strip()

    # ----------- model -----------
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise TypeError("მოდელი უნდა იყოს ტექსტური ტიპის (str)")
        if not value.strip():
            raise ValueError("მოდელი არ შეიძლება იყოს ცარიელი")
        self._model = value.strip()

    # ----------- year -----------
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError("წელი უნდა იყოს მთელი რიცხვი (int)")
        if value < 1886:  # პირველი ავტომობილი შეიქმნა 1886 წელს
            raise ValueError("წელი არ შეიძლება იყოს 1886-ზე ნაკლები")
        self._year = value

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    

# მაგალითად:
car1 = Car("Toyota", "Camry", 2020)
print(car1)  # Output: Toyota Camry (2020)

car1.brand = "Honda"
car1.year = 2023
print(car1)  # Output: Honda Camry (2023)

# არასწორი მაგალითები:
# car1.year = "2020"      # გამოიწვევს TypeError-ს
# car1.brand = ""          # გამოიწვევს ValueError-ს
# car1.year = 1800         # გამოიწვევს ValueError-ს

