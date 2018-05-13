from examples.queue import  *
from newsapi import NewsApiClient

def get_urls(**kwargs):
    methods = {'q': None, 'country': None, 'language': 'en', 'sources': None, 'category': None}
    for key, value in kwargs.items():
       if key in methods: methods[key] = value

    # Init
    newsapi = NewsApiClient(api_key='1c448f71905e45e08f142fbd882f4809')

    top_headlines = newsapi.get_top_headlines (**methods)

    return [i['url'] for i in top_headlines['articles']]

if __name__=='__main__':
    news_queue = LinkedQueue()
    for i in get_urls(q='trump'):
        news_queue.add(i)
