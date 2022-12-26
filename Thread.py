# Optimized code
import time,nltk,json,string,threading
from nltk.stem import snowball
start_time = time.time()
# Opening JSON file
file = open('C:/Users/HP/PycharmProjects/pythonProject1/test/foreverconscious.json')
file1 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/iceagenow.json')
file2 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/shadowproof.json')
file3 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/lifespa.json')


stemmer = snowball.EnglishStemmer()
articles0 = json.load(file)
articles1 = json.load(file1)
articles2 = json.load(file2)
articles3 = json.load(file3)

words = set()
# word_to_docs = {}
stop_words = set(nltk.corpus.stopwords.words('english'))
forward_index = {}
def merge(dict1, dict2):
    for word, articles in dict2.items():
        if word in dict1:
            dict1[word].update(articles)
        else:
            dict1[word] = articles
    return dict1

# temp1 = open('C:/Users/HP/PycharmProjects/pythonProject1/file.json','r')
# temp = open('C:/Users/HP/PycharmProjects/pythonProject1/file.json','w')
lock = threading.Lock()
def indexes(articles,num):
    i=0
    start_time1 = time.time()
    for article in articles[:334]:
        word_to_docs = {}
        x = 0
        # print(num,",",i, end="|")
        tokenized_text = [stemmer.stem(word) for word in  nltk.word_tokenize(article['content']) if  word not in stop_words]
        for word in tokenized_text:
            word_to_docs[word] = {article['id'] :  word_to_docs.get(word, {}).get(article['id'],[])+[x]}
            x+=1
        i += 1
    print("time taken by thread", num, ":", time.time() - start_time1)
    with lock:
        temp1 = open('C:/Users/HP/PycharmProjects/pythonProject1/file.json', 'r')
        temp_index = json.load(temp1)
        temp1.close()
        temp_index = merge(temp_index, word_to_docs)
    # word_to_docs.clear()

        temp = open('C:/Users/HP/PycharmProjects/pythonProject1/file.json', 'w')
        json.dump(temp_index, temp)
        temp.close()
        # print("time taken by thread",num,":",time.time()-start_time1)

    # temp = open('C:/Users/HP/PycharmProjects/pythonProject1/file.json', 'w')
    # json.dump(temp_index,temp)
    # temp.close()
    # end_time1 = time.time()
    # run_time1 = end_time1 - start_time1
    # print(f'Code run time: {run_time1} seconds')



thread1 = threading.Thread(target=indexes,args=(articles0,0))
thread1.start()
thread2 = threading.Thread(target=indexes,args=(articles1,1))
thread2.start()
thread3 = threading.Thread(target=indexes,args=(articles2,2))
thread3.start()
thread4 = threading.Thread(target=indexes,args=(articles3,3))
thread4.start()

# json.dump(word_to_docs,temp)
# file.close()
end_time = time.time()
run_time = end_time - start_time
print(f'Code run time: {run_time} seconds')