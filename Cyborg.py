import time

from Robot import Robot
from Human import Human

class Cyborg(Robot, Human):
    def __init__(self, name='<unamed>', power=False, sex='Male'):
        self.__name = name
        self.__power = power
        self.__sex = sex

    def karaokeLauncher(self):
        paroles = ["\n\nVivre sous l'équateur du Brésil","Entre Cuba et Manille","A l'heure d'été c'est facile","Prends-moi la main, viens danser","J'ai du soleil sur la peau", "J'ai dans le cœur un bongo", "J'ai dans la tête un oiseau","Qui te dit tout haut, Viens danser !","Sous les sunlights des tropiques","L'amour se raconte en musique","On a toute la nuit pour s'aimer","En attendant viens danser !","J'aime l'océan pacifique","Ça m'fait quelque chose de magique","Y a rein à faire qu'à rêver","Prends-moi la main viens danser !"]
        print("Vous avez lancé : Gilbert Montaigné - Sunlight des tropiques\n")
        time.sleep(3)
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        print()
        for ligne in paroles:
            print(ligne)
            time.sleep(3.8)

robert = Cyborg("Robert", True, "Male")
robert.karaokeLauncher()