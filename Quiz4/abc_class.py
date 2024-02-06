from abc import ABC, abstractmethod
import os

class Country(ABC):
    @abstractmethod
    def continent(self):
        pass

    @abstractmethod
    def flag_colors(self):
        pass

class Mexico(Country):
    def continent(self):
        print("Mexico is in North America")

    def flag_colors(self):
        print("Mexico flag has red, white, and green")
        

class Brazil(Country):
    def continent(self):
        print("Brazil is in South America")
    
    def flag_colors(self):
        print("Brazil flag has green, gold, blue")


def  main():
    mexico = Mexico()
    mexico.continent()
    mexico.flag_colors()

    print("\n")

    brazil = Brazil()
    brazil.continent()
    brazil.flag_colors()

if __name__=="__main__":
    main()