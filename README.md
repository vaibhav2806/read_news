# read_news
pip install pywin32 - install this to make speak function work properly.
Created my own API from newsapi.org.
Used requests module and made an object 'news', used requests.get() to pull all the news from the particular url.
Used json module to get the loads news into variable news_json, we did this becaues news was a string so we can not do slicing, So to do slicing we made news_json. 
Then articles = news_json['articles'] runs perfectly.


