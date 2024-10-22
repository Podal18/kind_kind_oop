class Man:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        if age > 0 and age < 110:
            self.__age = age
        else:
            print("НЕдопустимое значение")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def prnt_info(self):
        print(f"Имя - {self.__name}\nВозраст - {self.__age}")


class Worker(Man):

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Пропал человек с именем {self.name}")


class coaches(Man):
    pass


# pt1 = Man("Александра", 20)
# pt1.prnt_info()
# pt1.set_age(888)
# pt1.set_age(19)
# pt1.prnt_info()

pt2 = Worker("Семен")
pt2.prnt_info()

# pt3 = coaches("Андрей", 19)
# pt3.prnt_info()
