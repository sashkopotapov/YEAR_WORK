from newsapi import NewsApiClient

api = NewsApiClient(api_key='1c448f71905e45e08f142fbd882f4809')
s = api.get_top_headlines(sources='bbc-news')
print(s)