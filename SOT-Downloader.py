# -*- coding: utf-8 -*-
import webbrowser
import time
import urllib


# path to your txt file here with double "\\" 
word_file = 'C:\\Users\\antonin\\Desktop\\book2.txt' 


# see browser opening 
new = 2
# see Reading source file
lines = []
# see url code conversion
words_url = []


# Reading source file by lines and adding it to a list, here UTF is useless and we want to read as binary 'rb'
with open(word_file, 'rb') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines] # you may also want to remove whitespace characters like `\n` at the end of each line

    
# we take a list, convert it to url code and save it into a new list
for word in lines:
    word_url = urllib.parse.quote_plus(word)
    words_url.append(word_url)

print(words_url) 

# Opens a link in new window in your browser for each word in the list
for i in words_url:
    time.sleep(0.1)     # delay each request for 0.1 sec, should not be necessary
    url = "http://soundoftext.com/static/sounds/ko/%s.mp3" % i  # replace "ko" with language of your choice!!
    webbrowser.open(url, new=new)
