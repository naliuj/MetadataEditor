from filetypes.audio import Audio
from mutagen import mp3
from errors import MetadataError


class MP3(Audio):

    def get_tags(self):
        return self.tags

    def get_title(self):
        return self.tags['title']

    def edit_title(self, title):
        self.tags['title'] = title

    def get_artist(self):
        return self.tags['artist']

    def edit_artist(self, artist):
        self.tags['artist'] = artist

    def get_album(self):
        return self.tags['album']

    def edit_album(self, album):
        self.tags['album'] = album

    def get_genre(self):
        return self.tags['genre']

    def edit_genre(self, genre):
        self.tags['genre'] = genre

    def get_disc_num(self):
        return self.tags['discnumber']

    def edit_disc_num(self, discnumber):
        self.tags['discnumber'] = discnumber

    def get_total_discs(self):
        raise MetadataError('Total Discs')

    def edit_total_discs(self, disc):
        raise MetadataError('Total Discs')

    def get_year(self):
        return self.tags['year']

    def edit_year(self, year):
        self.tags['year'] = year

    def get_track_number(self):
        return self.tags['tracknumber']

    def edit_track_number(self, track):
        self.tags['tracknumber'] = track

    def get_album_artist(self):
        return self.tags['albumartist']

    def edit_album_artist(self, albumartist):
        self.tags['albumartist'] = albumartist

    def save(self):
        pass

    def __init__(self, path):
        self.path = path
        self.tags = mp3.EasyMP3(self.path)
