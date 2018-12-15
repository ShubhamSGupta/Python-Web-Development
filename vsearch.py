def search4letters(phrase:str , letter:str = 'aeiou') -> set :
    return set(letter).intersection(set(phrase))