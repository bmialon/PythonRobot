import time

class Robot():
    __name = ""
    __power = False
    __current_speed = 0
    __battery_level = 0
    __state = 'shutown'

    def __init__(self, name="<unnamed>", power=False):
        self.__name = name
        self.__power = power
        self.updateState()

    def updateState(self):
      if self.__power:
          self.__state = 'running'
      else:
          self.__state = 'shutown'

    def setName(self, name):
        self.__name=name

    def pushButtonPower(self):
        self.__power = not self.__power
        self.updateState()

    def chargeRobot(self):
        while(self.__battery_level < 100):
            self.__battery_level += 1
            print(self.__battery_level + "%")
            time.sleep(100)
    
    def setSpeed(self, speed):
        self.__current_speed = speed
    
    def getSpeed(self):
        return self.__current_speed
    
    def stopRobot(self):
        self.__current_speed = 0

    def resume(self):
        print(self.__name, " is ", self.__state, "with ", self.__battery_level, "%. The currrent speed is ", self.__current_speed, "kmh/h")