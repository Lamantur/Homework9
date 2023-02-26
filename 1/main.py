class Name:

    def __get__(self, instance, value):
        return instance.__dict__[self.attribute]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Значение должно быть строкой')
        instance.__dict__[self.attribute] = value

    def __set_name__(self, owner, attribute):
        self.attribute = attribute


class Positions:

    def __set__(self, instance, value):
        if value not in Worker.position_list:
            raise TypeError('Нет такой должности в списке')
        instance.__dict__[self.attribute] = value

    def __set_name__(self, owner, attribute):
        self.attribute = attribute


class Worker:
    name = Name()
    surname = Name()
    position = Positions()
    income_list = {30000: 5000, 40000: 7000, 50000: 8000,
                   60000: 9000, 70000: 10000, 80000: 11000, 100000: 15000}
    position_list = {"Генеральный директор",
                     "Исполнительный директор",
                     "Финансовый директор",
                     "Коммерческий директор",
                     "Заведующий хозяйством",
                     "Менеджер"}
    _income = income_list

    def __init__(self, name, surname, income, position) -> None:
        self.name = name
        self.surname = surname
        self.income = income
        self.position = position


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self, income):

        return self.income_list.get(income) + income

    def __str__(self) -> str:
        return f"{self.name} {self.surname}, {self.position}: {self.income + self.income_list.get(self.income)}"


ivanivanov = Position("Вася", "Иванов", 30000, "Менеджер")


print(ivanivanov.get_total_income(ivanivanov.income))
print(ivanivanov)
