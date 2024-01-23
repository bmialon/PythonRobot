from abc import ABCMeta
from abc import abstractmethod

class Vehicule(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def doMission(self):
        pass
    @abstractmethod
    def goForward(self):
        pass

class AerialVehicule(metaclass=ABCMeta):
    @abstractmethod
    def land(self):
        pass

class GroundVehicule(metaclass=ABCMeta):
    @abstractmethod
    def park(self):
        pass
	
class UnderseaVehicule(metaclass=ABCMeta):
    @abstractmethod
    def drown(self):
        pass
	
 
class UAV(Vehicule, AerialVehicule):
    @staticmethod
    def doMission(self):
        print("Mission Complete")
        pass

    def goForward(self):
        print("Flying...")
        pass

    def land(self):
        print("Landed lets go")
        pass

class UUV(Vehicule, UnderseaVehicule):
    @staticmethod
    def doMission(self):
        print("Mission Complete")
        pass

    def goForward(self):
        print("Swiming...")
        pass

    def drown(self):
        print("Drowned lets go")
        pass
	
class UGV(Vehicule, GroundVehicule):
    @staticmethod
    def doMission(self):
        print("Mission Complete")
        pass

    def goForward(self):
        print("Rolling...")
        pass

    def park(self):
        print("Parked lets go")
        pass