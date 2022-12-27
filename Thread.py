# Optimized code
import time,nltk,json,string,threading,spacy
from concurrent.futures import ThreadPoolExecutor

from nltk.stem import snowball
# Opening JSON file
file = open('C:/Users/HP/PycharmProjects/pythonProject1/test/foreverconscious.json')
file1 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/iceagenow.json')
file2 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/shadowproof.json')
file3 = open('C:/Users/HP/PycharmProjects/pythonProject1/test/lifespa.json')
# file = open('C:/Users/HP/PycharmProjects/pythonProject1/test/abcnews.json')

stemmer = snowball.EnglishStemmer()
articles0 = json.load(file)
articles1 = json.load(file1)
articles2 = json.load(file2)
articles3 = json.load(file3)

words = set()
# word_to_docs = {}
stop_words = set(nltk.corpus.stopwords.words('english'))
nlp = spacy.load('en_core_web_sm')
forward_index = {}
def merge_indexing( dict2):
    x = open('C:/Users/HP/PycharmProjects/pythonProject1/file.json','r')
    dict1 = json.load(x)
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
    # i=0
    # start_time1 = time.time()
    word_to_docs = {}
    for article in articles:

        x = 0
        print(num, end="|")
        # tokenized_text = [stemmer.stem(word) for word in  nlp(article['content']) if  word.is_alpha() and word not in stop_words]

        tokenized_text = []

        # Tokenize the text
        doc = nlp(article['content'])
        print(doc)

        # Iterate over the tokens
        for token in doc:
            # Check if the token is an alpha word and not a stop word
            print(token)
            if token not in stop_words:
                # Stem the token and append it to the list
                stemmed_token = stemmer.stem(token)
                tokenized_text.append(stemmed_token)

        for word in tokenized_text:
            word_to_docs[word] = {article['id'] :  word_to_docs.get(word, {}).get(article['id'],[])+[x]}
            x+=1

    # temp_indexing = merge_indexing(word_to_docs)
    return word_to_docs
            # i += 1
        # print("time taken by thread", num, ":", time.time() - start_time1)
        # with lock:
        # temp1 = open('C:/Users/HP/PycharmProjects/pythonProject1/file.json', 'r')
        # temp_index = json.load(temp1)
        # temp1.close()
        # temp_index = merge(temp_index, word_to_docs)
        # return temp_index
    # word_to_docs.clear()

        # temp = open('C:/Users/HP/PycharmProjects/pythonProject1/file.json', 'w')
        # json.dump(temp_index, temp)
        # temp.close()
# arr = []
#
# for article in articles:
#     arr.extend([article])
#     if (len(arr) == 6):
#         thread1 = threading.Thread(target=indexes,args=(arr[0],0))
#         thread1.start()
#         thread2 = threading.Thread(target=indexes,args=(arr[1],1))
#         thread2.start()
#         thread3 = threading.Thread(target=indexes,args=(arr[2],2))
#         thread3.start()
#         thread4 = threading.Thread(target=indexes,args=(arr[3],3))
#         thread4.start()
#         thread5 = threading.Thread(target=indexes,args=(arr[4],4))
#         thread5.start()
#         thread6 = threading.Thread(target=indexes,args=(arr[5],5))
#         thread6.start()
#         arr = []

# json.dump(word_to_docs,temp)
# file.close()
start_time = time.time()

with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit tasks to the thread pool
    result1 = executor.submit(indexes, articles0,1)
    # result2 = executor.submit(indexes, articles1,2)
    # result3 = executor.submit(indexes,articles2,3)
    # result4 = executor.submit(indexes, articles3,4)

    # Wait for the tasks to complete and get the results
    result1_value = result1.result()
    # result2_value = result2.result()
    # result3_value = result3.result()
    # result4_value = result4.result()
    # print(result1_value)
    # print(result2_value)
    # print(result3_value)
    # print(result4_value)

end_time = time.time()
run_time = end_time - start_time
print(f'Code run time: {run_time} seconds')