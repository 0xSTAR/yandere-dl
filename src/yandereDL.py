#!/usr/bin/env python3

from sites import yandere
from sites import danbooru
from sites import gelbooru
from sites import zerochan
from sites import nhentai

class yandereDL(object):
    def main(self):
        while True:
            # disgusting while loop.
            site = input('Which site would you like to download from? :  ')
            if site=='yande.re':site = yandere();break
            elif site=='danbooru':site = danbooru();break
            elif site=='gelbooru':site = gelbooru();break
            elif site =='zerochan':site = zerochan();break
            elif site=='nhentai':site = nhentai(); break
            print(f'\n\n error: Must be either \'yande.re\' or \'danbooru\', or \'gelbooru\' or \'zerochan\' or \'nhentai\'.\n\n')
        del(site)
        print('\n\nDone . . . ! Thank you for using my service!\n')
    def __init__(self):
        self.main()
