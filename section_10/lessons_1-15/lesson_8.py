# 298. Album class and More on DocStings

class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song's creator.
        duration (int): The duration of the song in seconds. May be a zero.
    """

    def __init__(self, title, artist, duration=0):
       
        self.title = title
        self.artist = artist
        self.duration = duration
        

class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        album_name (str): The name of the album.
        year (int): The year album was released.
        artist (Artist): The artist responsible for the album. If not specified,
            the artist will default to an artist with the name "Various Artist".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artis = Artist("Various Atrist")
        else:
            self.aritst = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): A song to add.
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if nevessary.
                Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)