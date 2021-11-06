import videostepan
from pynput.keyboard import Key, Controller
import keyboard as kb

keyboard = Controller()



def scut(string:str, words:int):
    return ' '.join(string.split(' ')[words:])


def parse(prompt:str):
    prompt = scut(prompt, 1)

    # video stuff
    if prompt == "включай музыку":
        videostepan.tovideo()
        return 'видос на подходе'

    if prompt.startswith('включи ') or prompt.startswith('найди '):
        search = scut(prompt,1)
        videostepan.youtube_search(search)
        return (f'ищу {search}')

    # panic
    if prompt == "красный код":
        return 'хуй соси'

    # media controls
    if prompt == 'пауза':
        kb.press('play/pause')
        return 'ладно'

    if prompt == 'я хочу дико д******':
        link = 'https://www.youtube.com/watch?v=xwC3VZlLrzQ'
        videostepan.open_link(link)
        return 'дрочи дрочи не бойся'

    # прощаемся
    if prompt in ["хорош", "заткнись"]:
        return 'пока...'

    else: return 'не могу сказать что я понял'