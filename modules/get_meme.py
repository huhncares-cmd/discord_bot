from bs4 import BeautifulSoup as bs
import requests
import random

def get_meme(URL):
    memes = []

    soup = bs(requests.get(URL).content, 'html.parser')
    for img in soup.find_all("img"):
        if img.attrs.get("src").startswith('https://'):
            memes.append(img.attrs.get("src"))
    
    return random.choice(memes)

if __name__ == '__main__':
    meme = get_meme(URL = 'https://www.memedroid.com/')
    print(meme)