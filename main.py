class Person:
    def __init__(self,name,age,birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    isMale = True
h = Person("Alex", 15, '29 February')


year = [2023, 2024, 2025, 2026, 2027, 2028]

for i in year:
    if (i %400) == 0:
        print(True, i)


    if (i % 4 == 0) and (i % 100 != 0):
        print(True, i)

    else:
        print(False, i)


print("на ближайші шість років я буду святкувати всій день народження високосного дня:")
print(year)



