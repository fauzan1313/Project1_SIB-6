from Modules.libraryitem import libraryitem


class CD(libraryitem):
    def __init__(self, title, upc, subject, artist):
        super().__init__(title, upc, subject)  # Parameter Init libraryitem
        self.artist = artist
