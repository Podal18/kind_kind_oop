


class Man:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 110:
            self.__age = age
        else:
            print("НЕдопустимое значение")

    @property
    def name(self):
        return self.__name

    # def __repr__(self): для красивоо выводав консоль
    def __str__(self):
        return f"Имя - {self.__name}\nВозраст - {self.__age}"

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        return [self, other]

class Worker(Man):

    # def __init__(self, name):
    #     self.name = name

    def __del__(self):
        # print(self.__dict__)
        # print(f"Пропал человек с именем {self._Man__name}")
        print(f"Пропал человек с именем {self.name}")

class coaches(Man):

    def __init__(self, qualification):
        self.qualiffication = qualification





pt1 = Man("Семен", 20)
print(pt1)
pt1.age = 999
pt1.age = 21
print(pt1)

pt2 = Worker("Семен", 20)
print(pt2)
# print(pt2._Man__name)
print(pt2.name)

pt3 = coaches("Андрей", 19)
print(pt3)

print(*(pt1 + pt2))
