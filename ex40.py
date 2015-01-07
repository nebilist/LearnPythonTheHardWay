class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        for line in self.lyrics:
            print line
    def sing_song_backwards(self):
        for i in reversed(xrange(len(self.lyrics))):
            print self.lyrics[i]
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                   
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
songObject = ["Os iusti meditabitur sapientiam", 
              "Et lingua eius Loquetur",
              "Beatus vir qui Sufert tentationem",
              "Quoniam cum probates fuerit Accipiet coronam vitae"]
          
lilium = Song(songObject)
lilium.sing_song_backwards()
