# 297. DocStrings and Raw Literals
# =============================================================================

class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song's creator.
        duration (int): The duration of the song in seconds. May be a zero.
    """

    def __init__(self, title, artist, duration=0):
        """Song init method
        
        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): An Artist object representing the song's creator.
            duration (Optional[int]): Intial value for the 'duratino' attribute.
                Will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

# From lesson 8
# -------------------------------------------------------------------------------
# help(Song.__init__)
# print(Song.__doc__)
# print(Song.__init__.__doc__)

# Song.__init__.__doc__ =  """Song init method
        
#         Args:
#             title (str): Initialises the 'title' attribute
#             artist (Artist): An Artist object representing the song's creator.
#             duration (Optional[int]): Intial value for the 'duratino' attribute.
#                 Will default to zero if not specified.
#         """

# help(Song)
# -------------------------------------------------------------------------------