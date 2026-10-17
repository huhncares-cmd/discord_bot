# Discord Bot

A Python Discord bot with commands for COVID-19 statistics and random Reddit images.

## Features

- `&help` shows available commands.
- `&corona [country]` shows current COVID-19 stats (default: `Germany`).
- `&reddit [subreddit]` posts a random image post from a subreddit (default: `memes`).

## Requirements

- Python 3.8+
- A Discord bot token
- Reddit API credentials (for the Reddit command)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with:

```env
DISCORD_TOKEN=your_discord_bot_token
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_reddit_user_agent
```

## Run

```bash
python main.py
```

## Project structure

```text
main.py                       # Bot setup and command handlers
modules/corona_stats.py       # Scrapes COVID-19 data from worldometers
modules/search_reddit.py      # Fetches random Reddit image posts
```
