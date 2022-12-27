import json

file = open('C:/Users/HP/Downloads/dataverse_files/json/json/nela-gt-2021/newsdata/abcnews.json')
articals = json.load(file)
https_dict = {}
http_read = open('C:/Users/HP/Documents/GitHub/main1/https.json')
http_data = json.load(http_read)
x=0
for artical in articals:
    https_dict.update({artical['id']: artical['url']})
    x+=1
    print(x)
print(type(https_dict))
http_data.update(https_dict)
https = open('C:/Users/HP/Documents/GitHub/main1/https.json','w')
json.dump(http_data,https)
https.close()