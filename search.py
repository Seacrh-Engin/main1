import json

import numpy

index_file = open('C:/Users/HP/Documents/GitHub/main1/filexyz.json')
inverted_index = json.load(index_file)
https_file = open('C:/Users/HP/Documents/GitHub/main1/https.json')
https = json.load(https_file)

def pairing(len):
    pairs = set()
    for i in range(len):
        for j in range(len):
            if i != j:
                pairs.add((i,j))
    return pairs

def comparing_lists(word,artical1,occurances):
    rank1 = occurances
    # rank2 = 0
    # print(inverted_index[word])
    # print(artical1)
    list1 = inverted_index[word][artical1]
    # list2 = inverted_index[word][artical2]
    rank1 = (1+occurances)/list1[1]
    for i in range(3,list1[0]+2):
        rank1 += (i+occurances)/list1[i]

    return {str(rank1):https[artical1]}



def Ranking(word):
    articals_dict = inverted_index[word]
    # print(key for key in articals_dict.keys())
    # print(articals_dict)
    articals_length = {}
    for artical_id,array in articals_dict.items():
        articals_length[array[0]] = articals_length.get(array[0],[])+[artical_id]
    maximum_key = max(articals_length, key=lambda x: x)
    rank_lst = []
    # print(articals_length)
    occurances_list = list(articals_length)
    occurances_list.sort(reverse=True)
    ranklist = []
    rank_dict = {}

    for key,articals in articals_length.items():
        # compare_set = pairing(len(articals_length[i]))
        print(articals)
        for artical in articals:
            rank_dict.update (comparing_lists(word,artical,key))
    for rank in rank_dict:
        print(rank)
        ranklist.append(rank)
    ranklist.sort(reverse=True)

        # articals_length[key] = ranklist
        # rank_lst.append(rank_dict)
    # print(occurances_list)
    print(articals_length)
    print((ranklist))

    # for occurrence in occurances_list:
    #     for or_list in rank_lst:
    #         print("OR-----",or_list)
    #         for o_rank in articals_length[occurrence]:
    #             print(or_list[str(o_rank)])

    for rank in ranklist:
        print(rank_dict[rank])
Ranking("total")