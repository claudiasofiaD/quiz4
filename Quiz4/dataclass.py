from dataclasses import dataclass

@dataclass
class VideoGame:
    title: str
    price: float
    release: int

def main():
    videoGames = [
        VideoGame("Elden Ring", 59.99, 2022),
        VideoGame("Avatar: Frontiers of Pandora", 60.99, 2023),
        VideoGame("Suicide Squad: Kill the Justice League", 69.99, 2024)
    ]

    videoGames.append(VideoGame("Hitman 3", 39.99, 2021))

    expensive_videoGame=max(videoGames, key=lambda p:p.price)
    print(f"The most expensive video game is {expensive_videoGame.title}")

    latest_videoGame=max(videoGames, key=lambda p:p.release)
    print(f"The most recent video game is {latest_videoGame.title}")
    
if __name__=="__main__":
    main()

    