from filetypes.audio import Audio
from mutagen.flac import FLAC as f


class FLAC(Audio):

    def get_title(self):
        return self.audio['title'][0]

    def edit_title(self, title):
        self.audio['title'] = title

    def get_artist(self):
        return self.audio['artist'][0]

    def edit_artist(self, artist):
        self.audio['artist'] = artist

    def get_album(self):
        return self.audio['album'][0]

    def edit_album(self, album):
        self.audio['album'] = album

    def get_genre(self):
        return self.audio['genre'][0]

    def edit_genre(self, genre):
        self.audio['genre'] = genre

    def get_disc_num(self):
        return self.audio['tracknumber'][0]

    def edit_disc_num(self, disc):
        self.audio['discnumber'] = disc

    def get_total_discs(self):
        return self.audio['totaltracks'][0]

    def edit_total_discs(self, disc):
        self.audio['totaltracks'] = disc

    def get_year(self):
        return self.audio['date'][0]

    def edit_year(self, year):
        self.audio['date'] = year

    def get_track_number(self):
        return self.audio['tracknumber'][0]

    def edit_track_number(self, track):
        self.audio['tracknumber'] = track

    def get_all_tags(self):
        return self.audio()

    def get_artist(self):
        return self.audio['artist'][0]

    def edit_artist(self, artist):
        self.audio['artist'] = artist

    def save(self):
        self.audio.pprint()
        self.audio.save()

    def __init__(self, path):
        self.path = path
        self.audio = f(self.path)
