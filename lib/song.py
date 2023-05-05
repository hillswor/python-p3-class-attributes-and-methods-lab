import ipdb


class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_artists(artist)
        Song.add_to_artist_count(artist)
        Song.add_to_genres(genre)
        Song.add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls, incrementer=1):
        cls.count += incrementer

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count.keys():
            cls.genre_count[f"{genre}"] = 1
        else:
            cls.genre_count[f"{genre}"] += 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count.keys():
            cls.artist_count[f"{artist}"] = 1
        else:
            cls.artist_count[f"{artist}"] += 1


# Song("99 Problems", "Jay Z", "Rap")
# Song("Halo", "Beyonce", "Pop")
# Song("Smells Like Teen Spirit", "Nirvana", "Rock")

# out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")

# ipdb.set_trace()
