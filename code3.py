import nltk
import json
import time
import numpy
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
st = time.time()
stop_words = stopwords.words("english")
json_file = open("abcnews.json")
articles = json.load(json_file)
counter_article = 0
article_dict = {}
uniqueLexicon = []
smallLexicon = []
for article in articles:
    temp_list = []
    if counter_article == 1000:
        break
    article_text = (article["title"] + article["content"]).lower()
    article_text_words = nltk.word_tokenize(article_text)
    for word in article_text_words:
        word = stemmer.stem(word)
        if word.isalpha() and word not in stop_words:
            temp_list.append(word)
            # numpy.unique(uniqueLexicon.append(word))
    smallLexicon.append(temp_list)
    # temp_list = numpy.unique(temp_list)
    # uniqueLexicon = temp_list
    uniqueLexicon = uniqueLexicon + list(set(temp_list))
    uniqueLexicon = uniqueLexicon + temp_list
    counter_article = counter_article + 1
et = time.time()
print("Unique Lexicon:\n", uniqueLexicon)
print("Small Lexicon:\n", smallLexicon)
print("Execution Time", et-st)