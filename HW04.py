def create_oroginal_dict(text: str) -> dict:
    pass

def invert_dict(original_dict: dict) -> dict:
    pass


data = '''Создайте программу для лингвистов, которая будет инвертировать полученный
словарь. То есть в качестве ключа будет частота, а в качестве значения —
список символов с этой частотой.'''


data = data.lower()
letter_frec_dict = create_oroginal_dict(data)

inv_dict = invert_dict(letter_frec_dict)

print(letter_frec_dict)
print(inv_dict)