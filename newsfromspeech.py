import requests
from bs4 import BeautifulSoup
import pyttsx3

# Getting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)

# got all the news.

# Play the news

engine = pyttsx3.init() # get the player engine

for news in toi_news:
    engine.say(news)


# run and wait method, it processes it
engine.runAndWait() 
