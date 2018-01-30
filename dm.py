import requests
import json

def get_rhymes_from_datamuse(rhymes_with):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}
    params_diction["rel_rhy"] = rhymes_with
    response = requests.get(baseurl, params_diction)
    return response.json()

def get_word_list(data_muse_word_list):
    words = []
    for word_list in data_muse_word_list:
        words.append(word_list['word'])
    return words

def print_rhymes(word, max_rhymes=10):
    rhymes = get_word_list(get_rhymes_from_datamuse(word))

    print('Words that rhyme with', word)
    max2print = min(max_rhymes, len(rhymes))
    for i in range(max2print):
        print('\t', rhymes[i])

print_rhymes('blue')
