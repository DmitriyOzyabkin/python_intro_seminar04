def find_synonym(word: str) -> str:
    '''
    Find synonym in dictionary and return it
    or ask for another word if synonym doesn'et exist
    '''
    return synonym_dict.get(word, 'Такого слова нет в словаре').capitalize()



def add_pair_to_synonym_dict(synonyms: str) -> None:
    '''
    Splits two words and adds both to synonyms dictioanary
    '''
    word_1, word_2 = synonyms.lower().split(' - ')
    synonym_dict[word_1] = word_2
    synonym_dict[word_2] = word_1


n_pair = int(input('Введите количество пар слов: '))
synonym_dict = {}


for entry in range(1, n_pair + 1):
    synonyms = input(f'Введите пару №{entry} (формат ввода: слово - слово):  ')
    add_pair_to_synonym_dict(synonyms)

run_programm = True

while run_programm:
    word = input('Введите слово: ').lower()
    if word != 'exit':
        answer = find_synonym(word)
        print(f'Синоним: {answer}')
    else:
        run_programm = False



