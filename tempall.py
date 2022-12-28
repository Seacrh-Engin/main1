
# Optimized code
import time,nltk,json,spacy,os

from nltk.stem import snowball
start_time = time.time()
# Opening JSON file
# file = open('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/newsdata/abcnews.json')
stemmer = snowball.EnglishStemmer()
nlp = spacy.load('en_core_web_sm')
text = ""
words = set()

stop_words = set(nltk.corpus.stopwords.words('english'))
forward_index = {}
def merge_indexing( dict2):
    x = open('C:/Users/HP/PycharmProjects/pythonProject1/filexyz.json','r')
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
def merge_articals( dict2):
    x = open('C:/Users/HP/Documents/GitHub/main1/atrical_titles.json','r')
    dict1 = json.load(x)
    dict1.update(dict2)
    temp = open('C:/Users/HP/Documents/GitHub/main1/atrical_titles.json', 'w')
    json.dump(dict1, temp)
    file.close()

for temp in os.listdir('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/test/'):
    file = open('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/test/'+temp)
    articles = json.load(file)
    print(temp)
    y = 0
    word_to_docs = {}
    articles_titles = {}
    for article in articles:
        index = 1
        print(y, end=" ")
        tokenized_text = [stemmer.stem(word) for word in  nltk.word_tokenize(article['content']) if  word not in stop_words]
        for word in tokenized_text:
            tempvar = word_to_docs.get(word, {}).get(article['id'],[0,index])
            word_to_docs[word] = {article['id'] :  tempvar+[index-tempvar[-1]]}
            word_to_docs[word][article['id']][0] +=1
            index+=1
        y+=1
        tokenized_title = [stemmer.stem(word) for word in  nltk.word_tokenize(article['title']) if  word not in stop_words]
        for word in tokenized_title:
            articles_titles[word] = articles_titles.get(word,[])+[article['id']]

    merge_indexing(word_to_docs)
    merge_articals(articles_titles)

    break

end_time = time.time()
run_time = end_time - start_time
print(f'Code run time: {run_time} seconds')