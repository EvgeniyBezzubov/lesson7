class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 80000, "bonus": 8000}


class Position(Worker):


    def get_full_name(self):
        #  print(self.name +" " + self.surname)
        get_full_name_otvet = self.name + " " + self.surname
        return get_full_name_otvet

    def get_total_income(self):
        # print(self._income.get("wage") + self._income.get("bonus"))
        get_total_income_otvet = self._income.get("wage") + self._income.get("bonus")
        return get_total_income_otvet

    def __str__(self):
        otvet = str(obj1.get_full_name()) + "  " + str(obj1.get_total_income())
        return otvet


obj1 = Position("Evgeniy", "Bezzubov", "admin")
print(obj1)

# я решил, что изначально не понял задание : "содайте атрибут класса"
# поэтому с этого задания буду делать по другому.
