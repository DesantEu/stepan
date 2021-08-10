import speech_recognition as sp
import parserstepan

mic = sp.Microphone()
r = sp.Recognizer()
res = 'bruh'

while True:

    try:
        # слушаем микро
        with mic as source:
            print(".")
            audio = r.listen(source, timeout=1, phrase_time_limit=5)
        # распознаем и пишем че поняли
        res = r.recognize_google(audio, language="ru-RU").lower()
        print("@ " + res)

        # если обращались к степану то парсим
        # if res.startswith('степан') or res.startswith('стёпа'):
        ress = res.split(' ')
        if 'степан' in ress or 'стёпа' in ress:
            print('1')
            bres = ''
            for i in range(len(ress)):
                print(f"'{ress[i]}'")
                if ress[i] == 'степан' or ress[i] == 'стёпа':
                    bres = parserstepan.parse(parserstepan.scut(res, i))
                    print('oxetm '+ parserstepan.scut(res, i))
                    print('# ' + bres)
                    break

            # это если прощаемся
            if bres == "poka...":
                break

    # anticrash 3000
    except Exception as e:
        print('... ' + str(e))
