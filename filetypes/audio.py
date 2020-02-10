from abc import ABC, abstractmethod


class Audio(ABC):

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def edit_title(self, title):
        pass

    @abstractmethod
    def get_artist(self):
        pass

    @abstractmethod
    def edit_artist(self, artist):
        pass

    @abstractmethod
    def get_album(self):
        pass

    @abstractmethod
    def edit_album(self, album):
        pass

    @abstractmethod
    def get_genre(self):
        pass

    @abstractmethod
    def edit_genre(self, genre):
        pass

    @abstractmethod
    def get_disc_num(self):
        pass

    @abstractmethod
    def edit_disc_num(self, disc):
        pass

    @abstractmethod
    def get_total_discs(self):
        pass

    @abstractmethod
    def edit_total_discs(self, disc):
        pass

    @abstractmethod
    def get_year(self):
        pass

    @abstractmethod
    def edit_year(self, year):
        pass

    @abstractmethod
    def get_track_number(self):
        pass

    @abstractmethod
    def edit_track_number(self, track):
        pass

    @abstractmethod
    def get_tags(self):
        pass

    @abstractmethod
    def get_album_artist(self):
        pass

    @abstractmethod
    def edit_album_artist(self, albumartist):
        pass

    @abstractmethod
    def save(self):
        pass
