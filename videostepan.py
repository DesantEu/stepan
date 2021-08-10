import webbrowser
import urllib.request
from youtubesearchpython import VideosSearch


def open_link(link:str):
    webbrowser.open(link)

def youtube_search(prompt:str):
    videosSearch = VideosSearch(prompt, limit = 2)
    vid = dict(videosSearch.result())["result"][0]['id']
    open_link(f'https://www.youtube.com/watch?v={vid}')


def tovideo():
    open_link('https://www.youtube.com/watch?v=c9JNp6kdKqU')
