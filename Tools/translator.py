from googletrans import *


def translate(text, des_lang):
    temp = ""
    try:
        temp = Translator().translate(text, dest="ta")
    except Exception as e:
        print(e)
        temp = translate(text)
    return temp


print([translate(x, "ta").text for x in ['Ayurveda', 'Siddha', 'Unani']])
