import lpthw_40_mystuff as mystuff

class MyStuff(object):
    def __init__(self):
        self.tangerine = "An now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = (MyStuff())
thing.apple()
print(thing.tangerine)

# mystuff = {'apple': "I am apples!"}
# print(mystuff['apple'])

# print(mystuff.apple())

# print(mystuff.tangerine)

# class MyStuff(object):
#     def __init__(self):
#         self.tangerine = "And now a thousand years between"
#
#     def apple(self):
#         print("I AM CLASSY APPLES!")

'''
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there",
                   "\n"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full fo shells",
                        "\n"])

thinking_out_loud = Song(["Place your head on my beating heart",
                          "I'm thinking out loud",
                          "Maybe we found love right where we are",
                          "\n"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

thinking_out_loud.sing_me_a_song()

'''