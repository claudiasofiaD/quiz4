from collections.abc import Iterable

class VideoGame:
    def __init__(self, title, developer):
        self._title = title
        self._developer = developer

    @property
    def title(self):
        return self._title, self._developer

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            val1 , val2 = new_title
        else: 
            val1=new_title
            val2="No input"
        self._title = val1
        self._developer = val2


def main():
    video_game = VideoGame("Elden Ring", "FromSoftware")

    print("Video game title (using properties):", video_game.title)

    video_game.title = "Silent Hill"
    print("Video game title after change (using properties):", video_game.title)

    video_game.title = ["Resident Evil" , "Capcom"]
    print("Video game title after change:", video_game.title)

if __name__ == "__main__":
    main()