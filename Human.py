class Human():
    __name = "Bastien"
    __sex = "male"
    __eated = []

    def __init__(self, name='Bastien', sex="male"):
        self.__name = name
        self.__sex = sex

    def eat(self, foods):
        for food in foods:
            print("miam", food)
        self.__eated = foods
    
    def digerer(self):
        for food in self.__eated:
            print("Burp de", food)