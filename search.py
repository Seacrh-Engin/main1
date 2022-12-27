import json

index_file = open('C:/Users/HP/Documents/GitHub/main1/filexyz.json')
inverted_index = json.load(index_file)

def pairing(len):
    pairs = set()
    for i in range(len):
        for j in range(len):
            if i != j:
                pairs.add((i,j))
    return pairs

def comparing_lists(word,artical1,total_articals):
    rank1 = 0
    # rank2 = 0
    # print(inverted_index[word])
    # print(artical1)
    list1 = inverted_index[word][artical1]
    # list2 = inverted_index[word][artical2]
    rank1 = (1+total_articals)/list1[1]
    for i in range(3,list1[0]+2):
        rank1 += (i+total_articals)/list1[i]

    return {rank1:artical1}



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
    for key,articals in articals_length.items():
        # compare_set = pairing(len(articals_length[i]))
        rank_dict = {}
        # print(articals)
        for artical in articals:
            rank_dict.update(comparing_lists(word,artical,key))
        rank_lst.append([rank_dict])
    # print((rank_lst))
    for key,value in ra
Ranking("act")