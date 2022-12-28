import nltk
import json
import time
# nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
stemmer = PorterStemmer()
lammatizer = WordNetLemmatizer()
st = time.time()
# from nltk import regexp_tokenize
stop_words = stopwords.words("english")
json_file = open("abcnews.json")
articles = json.load(json_file)
counter_article = 0
counter = 0
article_dict = {}
article_words_list = []
forward_index_dict = {}
inverted_index_dic = {}
flag = False
for article in articles:
    temp_list = []
    counter_article = counter_article + 1
    if counter_article == 101:
        break
    article_text = (article["title"] + article["content"]).lower()
    # print(article_text)
    article_text_words = nltk.word_tokenize(article_text)
    # print(len(article_text_words))
    article_text_words = set(article_text_words)
    # print(len(article_text_words))
    # print(article_text_words)
    for word in article_text_words:
        word = stemmer.stem(word)
        # word = lammatizer.lemmatize(word)
        if word not in stop_words and word.isalpha() and word not in article_words_list :
            article_words_list.append(word)
            article_dict[counter] = word
            temp_list.append(counter)
            inverted_index_dic[counter] = article["id"]
            counter = counter + 1
            # flag = True
            # print(counter)
    forward_index_dict[article["id"]] = temp_list
et = time.time()
# print(article_dict)
print(forward_index_dict)
print(inverted_index_dic)
print("Execution Time", et-st)
