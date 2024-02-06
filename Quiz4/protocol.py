from typing import Protocol
import os

class Country(Protocol):
    def continents(self) -> None: 
        ...
    
    def flag_colors(self) -> None: 
        ...

class Mexico:
    def continent(self) -> None:
        print("Mexico is in North America")

    def flag_colors(self) -> None:
        print("Mexico flag has red, white, and green")

class Brazil:
    def continent(self) -> None:
        print("Brazil is in South America")

    def flag_colors(self) -> None:
        print("Brazil flag has green, gold, blue")

def main() -> None:
    mexico: Country = Mexico()
    mexico.continent()
    mexico.flag_colors()

    print("\n")

    brazil: Country = Brazil()
    brazil.continent()
    brazil.flag_colors()

if __name__=="__main__":
    main()