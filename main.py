#from kivy.app import App

from filetypes.mp3 import MP3

#class MetadataEditor(App):
#    def build(self):
path = r'/Users/julian/Desktop/Stages/02 Fire.mp3'
x = MP3(path)
x.edit_title('Fire')
x.edit_disc_num('1')
x.edit_track_number('1')
print(x.get_tags())
# print(EasyID3.valid_keys.keys())


#if __name__ == '__main__':
#    MetadataEditor().run()
