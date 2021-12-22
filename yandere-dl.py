#!/usr/bin/env python3

from __future__ import print_function
import os, sys, subprocess

def ins(mod):
    subprocess.check_call([sys.executable,'-m','pip','install','-U',mod])

try:import requests
except ModuleNotFoundError:ins('requests');import requests
try:from bs4 import BeautifulSoup
except ModuleNotFoundError:ins('beautifulsoup4');from bs4 import BeautifulSoup

import datetime, time

class Yandere(object):
    def take_input(self):
        self.yandere_page = 'https://yande.re/post?page=1&tags='
        search = input('Search tags: ')
        rating= input('Rating (ratings: safe, explicit, questionable) (defaults to none): ')
        order=input('Order (rank, score) (defaults to rank): ')
        pages = input('Pages: ') # local
        if not pages == '' and int(pages) >= 1:
            self.pages_of=int(pages)
        elif int(pages) <= 0:
            print(f'page cannot be value: {pages}. only values of \'\'(blank string) and a num>=1 are allowed.')
        if not search == '':
            self.yandere_page += str(search.replace(' ','+'))
        if rating != '': #and rating=='safe' or rating=='explicit'or rating=='questionable':
            if rating=='e':rating='explicit'
            elif rating=='q':rating='questionable'
            elif rating=='s': rating='safe'
            if rating=='explicit' or rating=='questionable' or rating=='safe':
                self.yandere_page += '+rating:'+str(rating)
        if not order == '' and order=='rank' or order=='score':
            self.yandere_page += '+order:'+str(order)
        return

    def get(self):
        r = requests.get(self.yandere_page)
        html_doc = r.text
        soup = BeautifulSoup(html_doc,'html.parser')
        for link in soup.find_all('a'):
            temp_link = link.get('href')
            if temp_link != None and temp_link.startswith('https://files.yande.re/'):
                self.image_links.append(temp_link)
        if self.image_links == []:
            print('\n\nNo results were found . . .'); return

    def dl(self):
        print(f'\n\n-- Downloading images from page {str(self.page)} of {str(self.pages_of)} --\n')
        for link in self.image_links:
            file_name = '{} '.format(str(datetime.date.today()).replace('-','.'))+str(datetime.datetime.now().hour)+'.'+str(datetime.datetime.now().minute)+'.'+str(datetime.datetime.now().second)+'.'+str(datetime.datetime.now().microsecond)
            r = requests.get(link, stream=True)
            if link.endswith('.jpeg'): # check for jpeg
                file_ext = link[-5:]
            elif link[-4:].startswith('.'): # everything else . . . (png , jpg, gif even)
                file_ext = link[-4:]
            with open('./{}/'.format(self.folder)+str(file_name) + file_ext,'wb') as file_destination:
                try:r.raise_for_status()
                except: # HTTPError as http_error:
                    print('An unexpected error has occured: ' + repr())
                    print('Error: '+ r.status_code+' when attempting to access{}'.format(l))
                    if r.status_code != requests.codes.ok:
                        print(f'{r.status_code} is not an OK status code')
                    sys.exit()
                print(f'Downloading image No. {self.file_no}')
                for chunk in r.iter_content(chunk_size=128):
                        file_destination.write(chunk)

            self.file_no+=1

    def update(self):
        self.image_links = []
        self.page+=1
        self.yandere_page = self.yandere_page.replace('page={}'.format(str(self.page-1)),'page={}'.format(str(self.page))) # replace old page value (one less) with new page value

    def leave_mark(self):
        with open('./{}/{}'.format(self.folder,'yandere-dl.txt'),'w') as mark:
            mark.write('downloaded from yande.re using yandere-dl v1.1.0: https://github.com/0xSTAR/yandere-dl')

    def __init__(self):
        self.image_links = []
        self.file_no = 0 # gets converted to string
        #self.yandere_page = 'https://yande.re/post?page=1&tags='
        self.pages_of = 1
        self.page = 1
        self.folder = 'yande.re '+str(datetime.date.today())
        self.name = 'yande.re'

class Danbooru(object):
    def take_input(self):
        tokens = 0 # max of 2 tokens when searching
        search = input('Search: ')
        rating = input('Rating: ')
        order = input('Order: ')
        pages = input('Pages: ')
        if str(pages) != '' and int(pages) >1:
            self.pages_of=int(pages)
        elif not str(pages) == '' and int(pages)<=0:
            print(f'pages cannot be of any value <= 0. Got: {str(pages)}. Pages must be any value >= 1')
        if not search == '':
            self.danbooru_page+=search.replace(' ','+')
            #print(self.danbooru_page)
            tokens+=len(search.split(' '))
        if rating != '':
            if rating=='e':rating='explicit'
            elif rating=='q':rating='questionable'
            elif rating=='s': rating= 'safe'

            if rating == 'explicit' or rating == 'questionable' or rating == 'safe':
                tokens+=1 # only one rating allowed, no multiple ratings like multiple search tags
                self.danbooru_page+='+rating:'+rating
        if not order=='' and order=='score':
            # token optimized to not permit order: rank which is the site default.
            tokens+=1
            self.danbooru_page+='+order:'+order
        print(f'Search uses {str(tokens)} tokens')
        if tokens > 2:
            print(f'Max token count of 2 exceeded. Used: {str(tokens)}. Read the documentation in the README file for more info on the Danbooru downloader which has specific restrictions. Exiting . . .')
            time.sleep(3)
            sys.exit()

    def get(self):
        r=requests.get(self.danbooru_page)
        if not r.status_code == requests.codes.ok:
            print(f'Bad status code: {r.status_code}. Exiting . . .');time.sleep(2);sys.exit()
        soup = BeautifulSoup(r.text,'html.parser')
        for link in soup.find_all('a'):
            preview_link=link.get('href')
            #if preview_link.startswith('https://danbooru.donmai.us/posts/'):
            # danbooru does some blackmagic wizardry with ids for the images LOL
            if preview_link.startswith('/posts/'):
                preview = requests.get('https://danbooru.donmai.us'+preview_link)
                soup2 = BeautifulSoup(preview.text,'html.parser')
                for l in soup2.find_all('a'):
                    href_tag = l.get('href')
                    # Original may not be present always but download always is
                    if href_tag.startswith('https://cdn.donmai.us/original/') and href_tag[-11:]=='?download=1' and not href_tag[-15:].startswith('.zip'):
                        # dodge GIFs in the format of zips...
                        self.links.append(href_tag.replace('?download=1',''))
        if self.links == []:
            print('No results found . . .');return

    def dl(self):
        print(f'\n\n Downloading page {str(self.page)} of {str(self.pages_of)}\n')
        for link in self.links:
            r = requests.get(link,stream=True)
            now = datetime.datetime.now()
            ending = link.split('.')[3] # well that's an easier way of doing it. . .
            try:
                file_name='{} {}.{}.{}.{}.{}'.format(str(datetime.date.today()).replace('-','.'),str(now.hour),str(now.minute),str(now.second),str(now.microsecond),ending)
            except NameError:
                print(f'File type currently not supported . . . got extension: .{ending}')
            print(f'Downloading image No. {str(self.file_no)}')
            with open('./{}/{}'.format(self.folder,file_name),'wb') as file_dest:
                for data in r.iter_content(chunk_size=1024): # larger for danbooru cause of videos
                    file_dest.write(data)
            self.file_no+=1

    def update(self):
        self.links = []
        self.page+=1;self.danbooru_page=self.danbooru_page.replace('page={}'.format(str(self.page-1)),'page={}'.format(str(self.page)))

    def leave_mark(self):
        with open('./{}/{}'.format(self.folder,'yandere-dl.txt'),'w') as mark:
            mark.write('downloaded from Danbooru using yandere-dl v1.1.0: https://github.com/0xSTAR/yandere-dl')

    def __init__(self):
        self.page:int = 1 # page no.
        self.pages_of:int = 1 # no. of pages
        self.danbooru_page:str = 'https://danbooru.donmai.us/posts?page=1&tags=' # base url for search
        self.links = []
        self.file_no:int = 0
        self.folder:str = 'danbooru '+str(datetime.date.today())
        self.name = 'danbooru'

class Gelbooru(object):
    def take_input(self):
        #
        search = input('Search: ')
        rating = input('Rating: ')
        sort = input('Sort: ')
        pages = input('Pages: ')
        if str(pages) != '' and int(pages) >= 1:
            self.pages_of = int(pages)
        elif str(pages) != '':
            print(f'Pages value must be >= 1. Got: {int(pages)}. Exiting . . .')
            time.sleep(3)
            sys.exit()
        if not str(search) == '':
            self.link+=str(search).replace(' ','+')
        if not str(rating) == '':
            if str(rating) == 'e':
                rating = 'explicit'
            elif str(rating) == 'q':
                rating = 'questionable'
            elif str(rating) == 's':
                rating = 'safe'

            if str(rating) == 'explicit' or str(rating) == 'questionable' or str(rating) =='safe':
                self.link+='+rating:'+rating
            else:
                print(f'Invalid rating. Got: {str(rating)}. Must be either explicit, safe, questionable, or their short-hands: e,s,q .')
                print('Exiting . . .')
                time.sleep(5)
                sys.exit()

        if str(sort) != '':
            if str(sort)=='rank' or str(sort)=='score' or str(sort).startswith('score>=') or str(sort).startswith('score<=') or str(sort).startswith('score>') or str(sort).startswith('score<'):
                self.link+='+sort:'+sort

        # page id !!
        self.link+='&pid=0' # page 1, actual page: 0

    def get(self):
        print('\n\n Fetching page . . .\n')
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text,'html.parser')
        for view in soup.find_all('a'):
            if view.get('href')[:51]=='https://gelbooru.com/index.php?page=post&s=view&id=':
                soup2 = BeautifulSoup(requests.get(view.get('href')).text,'html.parser')
                for link in soup2.find_all('a'):
                    link_href = link.get('href')
                    if link_href[:33]=='https://img3.gelbooru.com/images/':
                        self.links.append(link_href)
        if self.links == []:
            print('No results found . . .')
            return

    def dl(self):
        print(f'\n\nDownloading page {str(self.page)} of {str(self.pages_of)} . . .\n')
        for link in self.links:
            ending = link.split('.')[3]
            now = datetime.datetime.now()
            file_name='{} {}.{}.{}.{}.{}'.format(str(datetime.date.today()).replace('-','.'),str(now.hour),str(now.minute),str(now.second),str(now.microsecond),ending)
            print(f'Downloading image No. {str(self.file_no)}')
            img = requests.get(link,stream=True)
            with open('./{}/{}'.format(self.folder,file_name),'wb') as destination:
                for data in img.iter_content(chunk_size=1024):
                    destination.write(data)
                destination.close()
            self.file_no+=1

    def update(self):
        self.links = []
        self.page+=1
        self.actual_page += 1
        self.link = self.link.replace('pid={}'.format(str((self.actual_page-1) * 42)),'pid={}'.format(str(self.actual_page*42)))

    def leave_mark(self):
        with open('./{}/{}'.format(self.folder,'yandere-dl.txt'),'w') as mark:
            mark.write('downloaded from Gelbooru using yandere-dl v1.1.0: https://github.com/0xSTAR/yandere-dl')

    def __init__(self):
        self.links = []
        self.file_no:int = 0
        self.page:int = 1
        self.actual_page:int = 0
        self.pages_of:int = 1
        self.folder:str = 'gelbooru '+str(datetime.date.today())
        # base url for listing
        self.link:str = 'https://gelbooru.com/index.php?page=post&s=list&tags='
        self.name = 'gelbooru'


def main():
    # ansi art? or ascii. i don't really know what to call it.
    print("""
               _________________
             _/                 \_
        _.-| WELCOME TO YANDERE-DL |-._
            \      by 0xSTAR      /
    <<<<.....\___________________/....>>>>

          ..... supported sites .....

             - yande.re
             - danbooru
             - gelbooru

    """)
    while not not (site != 'yande.re' and not site=='danbooru' and not site=='gelbooru'):
        site = input('Which site would you like to download from? :  ')
        if site=='yande.re':
            site = Yandere()
            break
        elif site=='danbooru':
            site = Danbooru()
            break
        elif site=='gelbooru':
            site = Gelbooru()
            break
        print(f'\n\n Must be either \'yande.re\' or \'danbooru\', or \'gelbooru\'.\n\n')

    try:os.mkdir(path=site.folder,mode=511,dir_fd=None);print(f'New directory: \'{site.folder}\' created')
    except FileExistsError:
        #print(f'Directory {site.folder} already exists. Continuing . . .') # debug
        pass
    site.take_input()
    site.leave_mark()
    while site.page <= site.pages_of:
        if not site.folder.endswith(str(datetime.date.today())):
            # for if people run this thing overnight
            print('A new day is upon us!')
            site.folder = site.name+' '+str(datetime.date.today())
            try:os.mkdir(path=site.folder,mode=511,dir_fd=None);print(f'New directory: \'{site.folder}\' created.')
            except FileExistsError:
                pass
        site.get()
        site.dl()
        site.update()
    print('\n\n\n . . . Done! Thank you for using my service... !\n')


if __name__ == '__main__':
    try:main()
    except NameError:time.sleep(2);sys.exit()
    time.sleep(5)
    sys.exit()
