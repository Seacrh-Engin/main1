import os
import time, nltk, json

from nltk.stem import snowball

# Opening JSON file
start_time = time.time()

stemmer = snowball.EnglishStemmer()
# articles = json.load(file)
x = 0
id = 0
word_ids = {}
inverded_indexing = {}
forward_index = {}
stop_words = nltk.corpus.stopwords.words('english')
for temp in os.listdir("./test/"):
    articles = open("./test/" + temp, "r")
    articles = json.load(articles)
    for article in articles:  # for each article in the json file (there are 100 articles) we will extract the text and add it to the text variable
        article_words = []
        print(x, end=" ")
        tokenized_text = nltk.word_tokenize(article['content'])
        for word in tokenized_text:
            word = stemmer.stem(word)
            if word not in stop_words and word.isalpha():
                if word not in word_ids:
                    word_ids[word] = id
                    inverded_indexing[id] = [article['id']]
                    id += 1
                else:
                    inverded_indexing[word_ids[word]] = inverded_indexing[word_ids[word]] + [article['id']]
                article_words.append(word_ids[word])
        x += 1
        forward_index[article["id"]] = article_words
        if x == 1000:
            break
lexicon = open('C:/Users/HP/PycharmProjects/pythonProject1/lexicon.json', 'w')
json.dump(word_ids, lexicon)
lexicon.close()
invert = open('C:/Users/HP/PycharmProjects/pythonProject1/inverded_indexing.json', 'w')
json.dump(inverded_indexing, invert)
invert.close()
forward = open('C:/Users/HP/PycharmProjects/pythonProject1/forward_index.json', 'w')
json.dump(forward_index, forward)
forward.close()
end_time = time.time()
run_time = end_time - start_time

print(f'Code run time: {run_time} seconds')
