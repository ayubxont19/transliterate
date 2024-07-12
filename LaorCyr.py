from transliterate import to_cyrillic, to_latin, transliterate

import regex

def latinOrCyrillic(text):
    check = bool(regex.search(r'\p{IsCyrillic}', text))
    if check == True:
        result = to_latin(text)
    else :
        result = to_cyrillic(text)
    return result
