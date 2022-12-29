import json,ast
from nltk.stem import snowball

import numpy

index_file = open('C:/Users/HP/Documents/GitHub/main1/inverted_indexing.json')
inverted_index = json.load(index_file)
https_file = open('C:/Users/HP/Documents/GitHub/main1/https.json')
https = str(https_file.read())+'}'
https = json.loads(https)
# https = ast.literal_eval(https)
# title_file = open('C:/Users/HP/Documents/GitHub/main1/atrical_titles.json')
# titles = json.load(title_file)
stemmer = snowball.EnglishStemmer()


def pairing(len):
    pairs = set()
    for i in range(len):
        for j in range(len):
            if i != j:
                pairs.add((i,j))
    return pairs

def comparing_lists(word,artical1,occurances):
    rank1 = occurances
    if(artical1 in inverted_index[word]):
        list1 = inverted_index[word][artical1]
        if list1[0]==1:
            rank1+=5
        rank1 += (1+occurances)/(list1[1])
        for i in range(2,len(list1)):
            rank1 += (i+occurances)/(list1[i]-list1[(i-1)])

    return {str(rank1):https[artical1]}



def Ranking(word):
    word = stemmer.stem(word)
    if word in inverted_index:
        articals_dict = inverted_index[word]
        articals_length = {}

        for artical_id,array in articals_dict.items():
            articals_length[len(array)] = articals_length.get(len(array),[])+[artical_id]

        occurances_list = list(articals_length)
        occurances_list.sort(reverse=True)
        ranklist = []
        rank_dict = {}

        for key,articals in articals_length.items():
            articals = articals
            for artical in articals:
                rank_dict.update (comparing_lists(word,artical,key))
        for rank in rank_dict:
            ranklist.append(rank)
        ranklist.sort(reverse=True)
        print((ranklist))

        for rank in ranklist:
            print(rank_dict[rank])
    else:
        print("Not Found")
Ranking("agreement")