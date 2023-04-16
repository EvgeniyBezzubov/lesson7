import time


class TrafficLight:
    __color = None

    def running(self):
        __color = "red"
        print(__color)
        time.sleep(7)
        __color = "yellow"
        print(__color)
        time.sleep(2)
        __color = "green"
        print(__color)
        time.sleep(5)


obj1 = TrafficLight()
obj1.running()
