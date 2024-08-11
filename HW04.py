from pprint import pprint

def create_original_dict(text: str) -> dict:
    original_dict={}
    for sym in text:
        original_dict[sym] = original_dict.get(sym, 0) + 1
    return original_dict

def invert_dict(original_dict: dict) -> dict:
    invert_dict = {}
    for letter in original_dict.keys():
        frec = original_dict[letter]
        if frec not in invert_dict:
            invert_dict[frec] = [letter]
        else:
            invert_dict[frec].append(letter)
    return invert_dict



data = input('Введте текст: ') 

data = data.lower()
letter_frec_dict = create_original_dict(data)
inv_dict = invert_dict(letter_frec_dict)

print('Оригинильный словарь частот:')
pprint(letter_frec_dict)
print('Инвертированный словарь частот:')
pprint(inv_dict)