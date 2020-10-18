# Problem Statement:-
# The task you have to perform is to read the news using python. 
# Build a program that will give you daily top 10 latest news. 
# For that, you have to check the website  https://newsapi.org/ which gives the news API. 
# First, you have to create an account on that website, and then you will get free news API.

import requests
import json

def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == "__main__":
    i = 0
    speak("Today's headlines are....")
    url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=356e5f3c0a314f218efbdeae951547d8'
    news = requests.get(url).text
    # So news is a string so we can't do slicing, to do so we will convert it into python obj using JSON
    news_json = json.loads(news)
    articles = news_json['articles']
    # print(news_json['status'])
    for article in articles:
        print(f"{i+1}. {article['title']}")
        speak(article['title'])
        if i <8:
            speak("Moving on to the next news.")
        elif i == 8:
            speak("Our last news is.")
        else:
            break
        i=i+1
    speak("Thank you for listening.")


        
            
            
    

