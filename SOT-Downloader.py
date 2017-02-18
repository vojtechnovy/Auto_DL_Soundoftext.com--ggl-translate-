import webbrowser
import time

new = 2

words = ["%EC%8B%9C%EA%B0%84", "%EC%96%B4%EA%B9%A8", "%EC%95%84%ED%8C%8C", "Hello", "Just", "an", "Example"] # replace this list with your own words

for i in words:
    time.sleep(0.1)     # delay each request for 0.1 sec, should not be necessary
    url = "http://soundoftext.com/static/sounds/ko/%s.mp3" % i  # replace "ko" with language of your choice!!
    webbrowser.open(url, new=new)
