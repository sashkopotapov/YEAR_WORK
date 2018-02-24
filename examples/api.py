import requests


#Shows breaking news
url = ('https://newsapi.org/v2/top-headlines?'
       'q=obama&'
       'apiKey=1c448f71905e45e08f142fbd882f4809')
response = requests.get(url)
print(response.json())



#Shows articles from specific source, BBC for example
url1 = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=1c448f71905e45e08f142fbd882f4809')
response2 = requests.get(url1)
print(response2.json())

#Shows articles filtred by a specific keyword, 'apple' for example
url2 = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2018-02-24&'
       'sortBy=popularity&'
       'apiKey=1c448f71905e45e08f142fbd882f4809')

response3 = requests.get(url2)
print(response3.json())
