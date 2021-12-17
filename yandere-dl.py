#!/usr/bin/env python3

# welcome to the spaghetti central of no shame

from __future__ import print_function
import os, sys, subprocess

def ins(mod):
    subprocess.check_call([sys.executable,'python','-m','pip','install','-U',mod])

try:import requests
except ModuleNotFoundError:ins('requests');import requests
try:from bs4 import BeautifulSoup
except ModuleNotFoundError:ins('beautifulsoup4')

image_links = []
file_name = ''
file_no = 0 # gets converted to string
yandere_page = ''
pages_of = 1
page = 1

def check_page(page): 
    #for y in data:
    if not page.startswith('https://yande.re/'):
        print('Improper link. Exiting . . .');sys.exit()
    return
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# redundant now that the link builds itself

import datetime

def file_name_():
    global file_name
    # abolish the ISO 8601 format for time!! 
    file_name = '{} '.format(str(datetime.date.today()).replace('-','.'))+str(datetime.datetime.now().hour)+'.'+str(datetime.datetime.now().minute)+'.'+str(datetime.datetime.now().second)+'.'+str(datetime.datetime.now().microsecond)

def take_input():
    global yandere_page
    yandere_page = 'https://yande.re/post?page=1&tags='

    search = input('Search tags: ')
    rating= input('Rating (ratings: safe, explicit, questionable) (defaults to none): ')
    order=input('Order (rank, score) (defaults to rank): ')
    pages = input('Pages: ') # local
    if not pages == '':
        if int(pages) >= 1:
            global pages_of
            pages_of=int(pages)
        else:
            print(f'page cannot be value: {pages}. only values of \'\'(blank string) and a num>=1 are allowed.')   
    if not search == '':
        yandere_page = str(yandere_page)+str(search)
    if rating != '':
        yandere_page = str(yandere_page)+str('+rating:'+rating)
    if not order == '':
        if order == 'rank' or order == 'score':
            yandere_page = str(yandere_page)+str('+order:'+order)
    return   

# parse page for all good links
def get_links(yp): # global_list = link, yp = yandere page
    global image_links
    r = requests.get(yp)
    html_doc = r.text
    soup = BeautifulSoup(html_doc,'html.parser') 
    for link in soup.find_all('a'):
        temp_link = link.get('href')
        if temp_link != None and temp_link.startswith('https://files.yande.re/'):
            image_links.append(temp_link)
    if image_links == []:
        print('\n\nNo results were found. Exiting . . .'); return #sys.exit()

def dl_imgs():
    global file_no
    for l in image_links:
        file_name_()
        r = requests.get(l, stream=True)
        with open('./{}/'.format(str(datetime.date.today()))+str(file_name) + l[-4:],'wb') as file_destination:
            try:r.raise_for_status()
            except: # HTTPError as http_error:
                print('An error has occured: ' + repr(http_error))
                print('Error: '+ r.status_code+' when attempting to access{}'.format(l))
                if r.status_code != requests.codes.ok:
                    print(f'{r.status_code} is not an OK status code')
                sys.exit()
            print(f'Downloading image No. {file_no}')
            for chunk in r.iter_content(chunk_size=128):
                file_destination.write(chunk)
        file_no+=1

def update_page():
    global yandere_page,page,image_links
    image_links = []
    page+=1
    yandere_page = yandere_page.replace('page={}'.format(str(page-1)),'page={}'.format(str(page)))

import time

def init():
    # ansi art? or ascii. i don't really know what to call it.
    print("""
               _________________
             _/                 \_
        _.-| WELCOME TO YANDERE-DL |-._
            \      by 0xSTAR      /
    <<<<.....\___________________/....>>>>
    
    
    """)
    global image_links; image_links = []

def main():
    global page
    take_input()
    try:os.mkdir(path=str(datetime.date.today()),mode=511,dir_fd=None);print(f'new directory {str(datetime.date.today())} created')
    except FileExistsError:
        print(f'Directory {str(datetime.date.today())} already exists. Continuing . . .')
    while page <= pages_of:
        check_page(yandere_page)
        get_links(yandere_page)
        dl_imgs()
        update_page()
    print('\n\n\n . . . Done! Thank you for using my service... !\n')

if __name__ == '__main__':
    init()
    main()
    time.sleep(5)
    sys.exit()
