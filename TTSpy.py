# coding: utf-8
#
import pyttsx3


def words_to_voice(words: str, language='CN'):

    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.setProperty('volume', 1.0)

    if language != 'EN':
        engine.setProperty("voice",
                           "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0")

    else:
        engine.setProperty("voice",
                            'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    engine.say(words)
    engine.runAndWait()

def words_to_voiceEN(words: str, language='EN'):

    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 1.0)
    # print(language)
    engine.say(words)
    engine.runAndWait()

def test_TTS():
    words_to_voice('hi，eva', 'EN')
    words_to_voice('你好吉利')
    print('TTS Done')

if __name__ == '__main__':
    test_TTS()