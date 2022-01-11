import asyncpraw
import os
import random
from dotenv import load_dotenv

load_dotenv()
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

async def generate_meme(subreddit='memes'):
    reddit = asyncpraw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT, username=REDDIT_USERNAME, password=REDDIT_PASSWORD)
    subreddit = await reddit.subreddit(subreddit)
    
    memes = []
    memes_selection = subreddit.top(limit=50)

    async for meme in memes_selection:
        memes.append([meme.title, meme.url, f"https://www.reddit.com{meme.permalink}"])
    
    await reddit.close()
    return random.choice(memes)