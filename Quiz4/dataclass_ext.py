from dataclasses import dataclass
from statistics import mean

@dataclass
class VideoGame:
    title: str
    price: float
    release: int
    reviews: list

    def average_rating(self) -> float:
        return mean(self.reviews)

def main():
    videoGames = [
        VideoGame("Elden Ring", 59.99, 2022, [5, 5, 5, 4, 4]),
        VideoGame("Avatar: Frontiers of Pandora", 60.99, 2023, [3, 4, 5, 4, 5]),
        VideoGame("Suicide Squad: Kill the Justice League", 69.99, 2024, [3, 3, 4, 5, 5])
    ]

    videoGames.append(VideoGame("Hitman 3", 39.99, 2021, [5, 5, 4, 3, 4]))

    expensive_videoGame=max(videoGames, key=lambda p:p.price)
    print(f"The most expensive video game is {expensive_videoGame.title}")

    latest_videoGame=max(videoGames, key=lambda p:p.release)
    print(f"The most recent video game is {latest_videoGame.title}")

    for videoGame in videoGames:
        print(f"The average rating of {videoGame.title} is {videoGame.average_rating()}")
    
if __name__=="__main__":
    main()

    