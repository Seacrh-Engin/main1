# # import ast
# # import nltk
# # import json
# # import time
# # from nltk.stem import snowball
# # #
# # # # Opening JSON file
# # # # start_time = time.time()
# # # # file = open('/test/abcnews.json')
# # # # stemmer = snowball.EnglishStemmer()
# # # # stop_words = set(nltk.corpus.stopwords.words('english'))
# # # # articles = json.load(file)
# # # # x=0
# # # #
# # # # for article in articles:
# # # #     print(x)
# # # #     x+=1
# # from collections.abc import MutableMapping
# # #
# # class HashTable(MutableMapping):
# #     def __init__(self, *args, **kwargs):
# #         self.store = dict()
# #         self.update(dict(*args, **kwargs))
# #
# #     def __getitem__(self, key):
# #         return self.store[self.__keytransform__(key)]
# #
# #     def __setitem__(self, key, value):
# #         self.store[self.__keytransform__(key)] = value
# #
# #     def __delitem__(self, key):
# #         del self.store[self.__keytransform__(key)]
# #
# #     def __iter__(self):
# #         return iter(self.store)
# #
# #     def __len__(self):
# #         return len(self.store)
# #
# #     def __keytransform__(self, key):
# #         return key
# # #
# # #
# # # file = open('file.txt','r')
# # # file1 = open('file.json','w')
# # #
# # # # dec = "\"key\": \"value\" ,\"key1\": \"value1\""
# # # dec1 = {"key": "value" ,"key1": "value1"}
# # # # dec2 = {"key2": "value2" ,"key12": "value12"}
# # # #
# # # # json.dump(dec1, file)
# # # # json.dump(dec2, file)
# # #
# # # # data = json.load(file)
# # # # print(data)
# # # #file.write("\"aaaa\": 123")
# # # # file.write("\"bbb\": 123")
# # # x = '{'+file.read()+'}'
# # # x= ast.literal_eval(x)
# # # ha = HashTable(x)
# # # ha.update(dec1)
# # # file.write(ha)
# # # # json.dump(dict(ha), file1)
#
# import json
#
# # Create a hash table
# hash_table = HashTable()
#
# # Add some key-value pairs to the hash table
# hash_table['aaa'] = 1
# hash_table['baa;'] = 2
# hash_table.update({'c': 3, 'd': 4})
#
# # Serialize the hash table as a JSON object
# json_data = json.dumps(hash_table.store)
#
# # Open the file in write mode
# with open('file.json', 'w') as f:
#     # Write the JSON object to the file
#     f.write(json_data)

# Open the file in read mode
# file = open('file.json', 'r')
# x = file.read()
# print(type(x))

# x = {'aaa': {'y':[1],'p':[7]}, 'oi': {'rr':[6]}, 'c': {'q':[3]}, 'd': {'w':[4,9]}}
# y = {'zxc': {'nh':[1]}, 'oi': {'z':[2],'po':[4]}, 'sc': {'q':[4]}, 'dwa': {'w':[1,3]}}
# y = {**x, **y}
# # y = {'aaa': [1], 'baa;': [2], 'c': [3], 'd': [0]}
# for word, articles in x.items():
#     if word in y:
#         y[word].update(articles)
#     else:
#         y[word] = articles
# # y.update(x)
# print(y)

# import threading
# import time
#
#
# def my_function(arg1, arg2):
#     for i in range(10):
#         print(f"Hello from a thread with arguments: {arg1}, {arg2}")
#         time.sleep(arg1)
#
# # Create a thread with arguments
# for i in range(10):
#     thread = threading.Thread(target=my_function, args=(0.5, i))
#     thread.start()
#     thread1 = threading.Thread(target=my_function, args=(1, i))
#
# # Start the thread
#
#     thread1.start()
import json
file = open('C:/Users/HP/PycharmProjects/pythonProject1/test/foreverconscious.json')
file1 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/iceagenow.json')
file2 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/shadowproof.json')
file3 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/lifespa.json')

# file1 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/21stcenturywire.json')
articals = json.load(file3)
x=1
for artical in articals:
    print(x)
    x+=1