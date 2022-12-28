# Optimized code
import time, nltk, json, spacy, os

from nltk.stem import snowball

start_time = time.time()
# Opening JSON file
# file = open('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/newsdata/abcnews.json')
stemmer = snowball.EnglishStemmer()
# nlp = spacy.load('en_core_web_sm')
# text = ""
lexicon_set = set()
stop_words = set(nltk.corpus.stopwords.words('english'))
def forward_indexing(articles):
    y = 0
    forward_index = {}
    for article in articles[:1000]:
        forward_index[article['id']] = {}
        print(y, end=" ")
        tokenized_text = [stemmer.stem(word) for word in nltk.word_tokenize(article['content']) if
                           word.isalpha() and word not in stop_words]
        tokenized_text_set = set(tokenized_text)
        global lexicon_set
        lexicon_set = lexicon_set.union(tokenized_text_set)
        for i in tokenized_text_set:
            forward_index[article['id']][i] = []
        for word in range(0, len(tokenized_text)):
            forward_index[article['id']][tokenized_text[word]].append(word)
        y += 1
    return forward_index
def inverted_indexing(forward__,lexicon__):
    count = 0
    inverted_index = {}
    for word in lexicon__:
        inverted_index[word] = {}
    for artical_id,word_dict in forward__.items():
        for word in word_dict:
            temp = {artical_id : forward__[artical_id][word]}
            inverted_index[word].update(temp)
        count+=1
        print(count, end=" ")

    return inverted_index
def merge_indexing(dict2):
    x = open('C:/Users/HP/Documents/GitHub/main1/inverted_indexing.json', 'r')
    dict1 = json.load(x)
    x.close()
    for word, articles in dict2.items():
        if word in dict1:
            dict1[word].update(articles)
        else:
            dict1[word] = articles
    temp = open('C:/Users/HP/Documents/GitHub/main1/inverted_indexing.json', 'w')
    json.dump(dict1, temp)
    file.close()


for temp in os.listdir('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/test/'):
    file = open('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/test/' + temp)
    articles = json.load(file)
    forward_index = forward_indexing(articles)
    inverted_index = inverted_indexing(forward_index, lexicon_set)
    merge_indexing(inverted_index)

    break


end_time = time.time()
run_time = end_time - start_time
print(f'Code run time: {run_time} seconds')
