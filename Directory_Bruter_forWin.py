#!/usr/bin/python
# -*- coding: utf-8 -*-
# @EmreYbs
# ----------------------------------------------------------------------
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>
# ----------------------------------------------------------------------
# @author EmreYbs | github.com/emreYbs

#           The aim of this python script is to brute-force directories
#               with the help of a wordlist by Netsparker.
#                   Brute force is not only for passwords but also for website directories
#                       and this project aims to get leftover settings, etc.



# I commented some code in order for Windows10 to run the code. For Linux, use my other version in my repo or edit the code as you wish.

import queue
import requests
import sys
import threading
#import pyfiglet  # Not necessary for the Directory_Bruter normally. Just added for terminal "feeling" :). You can leave it and related code.

AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
EXTENSIONS = ['.php', '.bak', '.orig', '.inc']

#from pyfiglet import Figlet
#custom_fig = Figlet(font='slant')
print("\n\n")
#print(custom_fig.renderText('D i r e c t o r y   B r u t e r'))
print(""" \tWelcome to Directory Bruter \t@author:EmreYbs\n\n
    The aim of this python script is to get the leftover development files,
    debugging scripts and configutations files in the server.
    So maybe, we can get some sensitive information by hunting common filenames and directories. 
    Therefore, we can get some precaution for the leftovers.\n\n""")

print("NOTE: Write the website properly like this: https://wwww.website.com \n")
#TARGET = print(pyfiglet.figlet_format("Target URL", font = "bubble"))

TARGET = input("Which website do you want to perform a directory brute force? \n")


THREADS = 50
#WORDLIST = "/home/emreYbs/Desktop/all.txt"  # Here, provide the wordlist path. I assume the path as "username/Desktop".
#This wordlist(SVNDigger) can be gotten from Netsparker Website. I chose the wordlist called "all.txt" when unzipped from SVNDigger. You can provide another wordlist to use, as you wish.
WORDLIST = "Desktop\\all.txt" # For Windows OS. You need to have the wordlist 'all' in your Windows Desktop path.Or arrange accordingly

def get_words(resume=None):
    def extend_words(word):
        if "." in word:
            words.put(f'/{word}')
        else:
            words.put(f'/{word}/')

        for extension in EXTENSIONS:
            words.put(f'/{word}{extension}')

    with open(WORDLIST) as f:
        raw_words = f.read()
    found_resume = False
    words = queue.Queue()
    for word in raw_words.split():
        if resume is not None:
            if found_resume:
                extend_words(word)
            elif word == resume:
                found_resume = True
                print(f'Resuming wordlist from: {resume}')
        else:
            print(word)
            extend_words(word)
    return words


def dir_bruter(words):
    headers = {'User-Agent': AGENT}
    while not words.empty():
        url = f'{TARGET}{words.get()}'
        try:
            r = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            sys.stderr.write('x')
            sys.stderr.flush()
            continue

        if r.status_code == 200:
            print(f'\nSuccess ({r.status_code}: {url})')
        elif r.status_code == 404:
            sys.stderr.write('.')
            sys.stderr.flush()
        else:
            print(f'{r.status_code} => {url}')


if __name__ == '__main__':
    words = get_words()
    print('\n\tPress return to continue.\n\n')
    print ("\tNow, I'll try to perform directory scan in: ",TARGET)
    sys.stdin.readline()
    for _ in range(THREADS):
        t = threading.Thread(target=dir_bruter, args=(words,))
        t.start()
