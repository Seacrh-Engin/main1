# Optimized code
import time, nltk, json, spacy, os

from nltk.stem import snowball

start_time = time.time()
# Opening JSON file
# file = open('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/newsdata/abcnews.json')
stemmer = snowball.EnglishStemmer()
nlp = spacy.load('en_core_web_sm')
text = ""
words = set()

stop_words = set(nltk.corpus.stopwords.words('english'))
def inverted_index(forward__,lexicon__):
    count = 0
    inverted_index = {}
    # print(forward__)
    # print("_______________")
    # print(lexicon__)
    for word in lexicon__:
        inverted_index[word] = {}
    for artical_id,word_dict in forward__.items():
        for word in word_dict:
            # print(artical_id)
            print(count)
            temp = {artical_id : forward__[artical_id][word]}
            inverted_index[word].update(temp)
        count+=1
            # print(inverted_index)

def merge_indexing(dict2):
    x = open('C:/Users/HP/PycharmProjects/pythonProject1/filexyz.json', 'r')
    dict1 = json.load(x)
    x.close()
    for word, articles in dict2.items():
        if word in dict1:
            dict1[word].update(articles)
        else:
            dict1[word] = articles
    temp = open('C:/Users/HP/PycharmProjects/pythonProject1/filexyz.json', 'w')
    json.dump(dict1, temp)
    file.close()


# def merge_articals( dict2):
#     x = open('C:/Users/HP/Documents/GitHub/main1/atrical_titles.json','r')
#     dict1 = json.load(x)
#     dict1.update(dict2)
#     temp = open('C:/Users/HP/Documents/GitHub/main1/atrical_titles.json', 'w')
#     json.dump(dict1, temp)
#     file.close()

for temp in os.listdir('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/test/'):
    file = open('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/test/' + temp)
    articles = json.load(file)
    print(temp)
    y = 0
    # word_to_docs = {}
    # articles_titles = {}
    forward_index = {}
    lexicon_set = set()
    for article in articles:
        forward_index[article['id']] = {}
        # index = 1
        print(y, end=" ")
        tokenized_text = [stemmer.stem(word) for word in nltk.word_tokenize(article['content']) if
                          word not in stop_words]
        tokenized_text_set = set(tokenized_text)
        lexicon_set = lexicon_set.union(tokenized_text_set)
        for i in tokenized_text_set:
            forward_index[article['id']][i] = []
        for word in range(0, len(tokenized_text)):
            forward_index[article['id']][tokenized_text[word]].append(word)

        # print(forward_index)
        #     tempvar = word_to_docs.get(word, {}).get(article['id'],[0,index])
        #     tempvar = {article['id'] :tempvar+[index]}
        #     word_to_docs[word] = {**word_to_docs.get(word,{}),**tempvar}
        #     word_to_docs[word][article['id']][0] +=1
        #     index+=1
        #     # if word in tokenized_title:
        #     #     word_to_docs[word][article['id']][2] = 1
        y += 1
        # {docid: {word:[]}}

        # for word in tokenized_title:
        #     tempvar = word_to_docs.get(word, {}).get(article['id'],[0,0,0])
        #     tempvar[2]=1
        #     tempvar = {article['id']:tempvar}
        #     word_to_docs[word] = {**word_to_docs.get(word, {}), **tempvar}

        # print(word_to_docs['today'])
    # merge_indexing(word_to_docs)

    # merge_articals(articles_titles)
    inverted_index(forward_index,lexicon_set)
    break
# print(forward_index)


end_time = time.time()
run_time = end_time - start_time
print(f'Code run time: {run_time} seconds')
