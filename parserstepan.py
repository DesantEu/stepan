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
        return 'vidos na podhode'

    if prompt.startswith('включи ') or prompt.startswith('найди '):
        search = scut(prompt,1)
        videostepan.youtube_search(search)
        return (f'looking for {search}')

    # panic
    if prompt == "красный код":
        return 'not implemented'

    # media controls
    if prompt == 'пауза':
        kb.press('play/pause')
        return 'pause ok'

    # прощаемся
    if prompt in ["хорош", "заткнись"]:
        return 'poka...'

    else: return '???'