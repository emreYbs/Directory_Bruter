#!/usr/bin/python
# -*- coding: utf-8 -*-
# emreYbs - Previous Version: https://github.com/emreYbs/Directory_Bruter/blob/main/directory_bruter.py

import csv
from termcolor import colored
import queue
import requests
import sys
import threading
from urllib.parse import urljoin

print(colored("Welcome to Directory Bruter V2", 'green'))
print(colored("This script is written by @emreybs", 'green'))
print(colored("This script is written for educational purposes only", 'green'))
print(colored("This code will be used for the security purposes in a PHP based web site.", 'green'))
AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/90.0"
EXTENSIONS = ['.php', '.bak', '.orig', '.inc']


def get_words(wordlist_path: str, resume: str = None) -> queue.Queue:
    def extend_words(word: str) -> None:
        if "." in word:
            words.put(f'/{word}')
        else:
            words.put(f'/{word}/')

        for extension in EXTENSIONS:
            words.put(f'/{word}{extension}')

    with open(wordlist_path) as f:
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


def dir_bruter(target: str, words: queue.Queue) -> None:
    headers = {'User-Agent': AGENT}
    while not words.empty():
        url = urljoin(target, words.get())
        try:
            r = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            sys.stderr.write('x')
            sys.stderr.flush()
            continue

        if r.status_code == 200:
            print(colored(f'\nSuccess ({r.status_code}: {url})', 'green'))
            with open('results.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([url])
        elif r.status_code == 404:
            sys.stderr.write('.')
            sys.stderr.flush()
        else:
            print(f'{r.status_code} => {url}')


if __name__ == '__main__':
    target = input(
        "Which website do you want to perform a directory brute force? \n")
    print("\n\nThe aim of this python script is to get the leftover development files, debugging scripts and configutations files in the server. So maybe, we can get some sensitive information by hunting common filenames and directories. Therefore, we can get some precaution for the leftovers.\n\n")
    print(
        f"NOTE: Write the website properly like this: https://wwww.website.com \n\nNow, I'll try to perform directory scan in: {target}")
    input('\nPress return to continue.\n\n')
# Example Path: Desktop - Arrange the PATH accordingly, to where you download and extracted the Wordlist
    wordlist_path = input("Provide the wordlist path: ")

    words = get_words(wordlist_path)
    threads = []
    for _ in range(50):
        t = threading.Thread(target=dir_bruter, args=(target, words))
        t.start()
        threads.append(t)
    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("\n\n[!] User interrupted the process. Exiting...\n")
        sys.exit(0)
