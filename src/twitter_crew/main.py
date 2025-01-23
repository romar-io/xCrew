import os
from .crew import TwitterCrew
from dotenv import load_dotenv
from .tools import TwitterTools

def main():
    load_dotenv()
    
    # Initialize Twitter tools with credentials from environment variables
    twitter_tools = TwitterTools(
        api_key=os.getenv("TWITTER_API_KEY"),
        api_secret=os.getenv("TWITTER_API_SECRET"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    
    # Create and run the crew
    crew = TwitterCrew(twitter_tools)
    result = crew.run(topic="AI Technology")
    print(result)

if __name__ == "__main__":
    main() 