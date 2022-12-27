import json

index_file = open('C:/Users/HP/Documents/GitHub/main1/file.json')
inverted_index = json.load(index_file)

def pairing(len):
    pairs = set()
    for i in range(len):
        for j in range(len):
            if i != j:
                pairs.add((i,j))
    return pairs

def comparing_lists(word,artical1,artical2,total_articals):
    list1 = inverted_index[word][artical1]
    list2 = inverted_index[word][artical2]
    for i in range(1,list1[0]):


def Ranking(word):
    articals_dict = inverted_index[word]
    # print(key for key in articals_dict.keys())
    # print(articals_dict)
    articals_length = {}
    for artical_id,array in articals_dict.items():
        articals_length[array[0]] = articals_length.get(array[0],[])+[artical_id]
    print(articals_length)
    maximum_key = max(articals_length, key=lambda x: x)
    # print(maximum_key)

    for i in range(maximum_key,0,-1):
        compare_set = pairing(len(articals_length[i]))



Ranking("today")