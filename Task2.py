class road:
    thickness = 0.05
    mass = 25
    #_lenght = "lenght"
    #_width = "width"

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def asphalt_mass(self):
        return self._lenght*self._width*self.mass*self.thickness


obj1 = road(20, 5000)
print(obj1.asphalt_mass())
#какой смысл создавать защищённые атрибуты класса,
# если они передаются при создании обьекта
# этот код работает и без них
# или задание некоректно написано? Ну или я не понял
# "Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах)." ну или я не понял