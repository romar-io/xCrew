import tweepy
from typing import Optionalnal

class TwitterTools:
    def __init__(self, api_key: str, api_secret: str, access_token: str, access_token_secret: str):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.client = tweepy.API(auth)

    def post_tweet(self, content: str) -> str:
        try:
            self.client.update_status(content)
            return f"Successfully posted tweet: {content}"
        except Exception as e:
            return f"Error posting tweet: {str(e)}" 