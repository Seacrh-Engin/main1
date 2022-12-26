# Optimized code
import time,nltk,json,string
from typing import MutableMapping

from nltk.stem import snowball
start_time = time.time()
# Opening JSON file
file = open('C:/Users/HP/PycharmProjects/pythonProject1/test/abcnews.json')
stemmer = snowball.EnglishStemmer()
articles = json.load(file)
text = ""
words = set()
word_to_docs = {}
stop_words = set(nltk.corpus.stopwords.words('english'))
forward_index = {}
def merge(dict1, dict2):
    for word, articles in dict2.items():
        if word in dict1:
            dict1[word].update(articles)
        else:
            dict1[word] = articles

for article in articles[:1000]:
    x = 0
    # print(x, end=" ")
    tokenized_text = [stemmer.stem(word) for word in  nltk.word_tokenize(article['content']) if  word not in stop_words]
    for word in tokenized_text:
        word_to_docs[word] = {article['id'] :  word_to_docs.get(word, {}).get(article['id'],[])+[x]}
    x+=1

temp = open('C:/Users/HP/PycharmProjects/pythonProject1/file.json','w')
json.dump(word_to_docs,temp)
file.close()
end_time = time.time()
run_time = end_time - start_time
print(f'Code run time: {run_time} seconds')