class Student:

    def __init__(self, name, stud_id):
        self.name = name
        self.stud_id = stud_id
        self.lap = self.Laptop()

    def show(self):
        """Вывести информацию о студенте и его ноутбуке"""
        print(self.name, self.stud_id)
        print(self.lap.brand, self.lap.cpu, self.lap.ram)

    class Laptop:

        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i5'
            self.ram = 8


s1 = Student('Ivan', 2)
s2 = Student('Mary', 3)
s1.show()

s1.lap.ram = 16
s1.show()

lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))