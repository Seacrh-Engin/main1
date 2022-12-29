# Optimized code
import time, nltk, json, spacy, os,threading

from nltk.stem import snowball
# import concurrent.futures

start_time = time.time()
# Opening JSON file
# file = open('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/newsdata/abcnews.json')
stemmer = snowball.EnglishStemmer()
lexicon_set = set()
# title_lexicon = set()
stop_words = set(nltk.corpus.stopwords.words('english'))
# def https(articals):
httpfile = open('C:/Users/HP/Documents/GitHub/main1/https.json','a')


def forward_indexing(articles):
    y = 0
    forward_index = {}
    for article in articles[:1000]:
        articleid = article['id'].replace('"','')
        forward_index[articleid] = {}
        print(y, end=" ")
        tokenized_title = [stemmer.stem(word) for word in nltk.word_tokenize(article['title']) if
                               word.isalpha() and word not in stop_words]
        tokenized_text = [stemmer.stem(word) for word in nltk.word_tokenize(article['content']) if
                           word.isalpha() and word not in stop_words]+tokenized_title
        # print(tokenized_title)
        tokenized_title = set(tokenized_title)
        tokenized_text_set = set(tokenized_text).union(tokenized_title)

        global lexicon_set
        lexicon_set = (lexicon_set.union(tokenized_text_set)).union(tokenized_title)
        for i in tokenized_text_set:
            forward_index[articleid][i] = [0]
        for word in range(0, len(tokenized_text)):
            forward_index[articleid][tokenized_text[word]].append(word+1)
            if tokenized_text[word] in tokenized_title:
                forward_index[articleid][tokenized_text[word]][0] = 1
        httpfile.write(',"'+articleid+'":"'+article['url']+'"')
        if('abcnews--2021-02-07--Chicago mayor: Schools, teachers union reach "tentative" deal over COVID-19 protections, potentially' in article['id']):
            print(article)
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
    temp.close()

def indexing(filename):
    file = open('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/test/' + filename)
    articles = json.load(file)
    forward_index = forward_indexing(articles)
    inverted_index = inverted_indexing(forward_index, lexicon_set)
    merge_indexing(inverted_index)


array =[]
for temp in os.listdir('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/test/')[:4]:
    array.append(temp)
    indexing(temp)
    break


# print(array)
# threads = []
# for i in range(4):
#   thread = threading.Thread(target=indexing, args=(array[i],))
#   thread.start()
#   threads.append(thread)
# for thread in threads:
#   thread.join()


# with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
#         # Submit the task to the thread pool
#     future0 = executor.submit(indexing, array[0])
#     future1 = executor.submit(indexing, array[1])
#     future2 = executor.submit(indexing, array[2])
#     future3 = executor.submit(indexing, array[3])
#     result0 = future0.result()
#     result1 = future1.result()
#     result2 = future2.result()
#     result3 = future3.result()

    # indexing(temp)



end_time = time.time()
run_time = end_time - start_time
print(f'Code run time: {run_time} seconds')
