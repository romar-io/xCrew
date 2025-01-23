import tweepy
from typing import List
from crewai import Agent, Task, Crew
from langchain_community.tools import DuckDuckGoSearchRun

# Twitter API credentials
TWITTER_API_KEY = "your_api_key"
TWITTER_API_SECRET = "your_api_secret"
TWITTER_ACCESS_TOKEN = "your_access_token"
TWITTER_ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Initialize Twitter client
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_client = tweepy.API(auth)

class TwitterTools:
    def post_tweet(self, content: str) -> str:
        try:
            twitter_client.update_status(content)
            return f"Successfully posted tweet: {content}"
        except Exception as e:
            return f"Error posting tweet: {str(e)}"

# Initialize tools
search_tool = DuckDuckGoSearchRun()
twitter_tools = TwitterTools()

# Create Agents
content_researcher = Agent(
    role='Content Researcher',
    goal='Research trending topics and gather relevant information',
    backstory="""You are an expert content researcher with a keen eye for trending 
    topics and viral content. You know how to identify engaging subjects that will 
    resonate with Twitter audiences.""",
    tools=[search_tool],
    verbose=True
)

content_writer = Agent(
    role='Content Writer',
    goal='Create engaging tweets based on research',
    backstory="""You are a skilled social media copywriter who knows how to craft 
    compelling tweets that drive engagement. You understand Twitter's best practices 
    and how to write viral content.""",
    verbose=True
)

tweet_publisher = Agent(
    role='Tweet Publisher',
    goal='Review and publish tweets',
    backstory="""You are responsible for reviewing tweets for compliance with 
    Twitter's guidelines and publishing them at optimal times.""",
    tools=[twitter_tools.post_tweet],
    verbose=True
)

# Create Tasks
def create_twitter_tasks(topic: str) -> List[Task]:
    research_task = Task(
        description=f"""Research the latest trending information about {topic}. 
        Identify key points that would be interesting to Twitter audiences.""",
        agent=content_researcher
    )

    writing_task = Task(
        description="""Create an engaging tweet based on the research provided. 
        Ensure it's within 280 characters and uses appropriate hashtags.""",
        agent=content_writer
    )

    publishing_task = Task(
        description="""Review the tweet for compliance and publish it if appropriate.
        Provide feedback if any changes are needed.""",
        agent=tweet_publisher
    )

    return [research_task, writing_task, publishing_task]

# Create and Run Crew
def run_twitter_crew(topic: str):
    crew = Crew(
        agents=[content_researcher, content_writer, tweet_publisher],
        tasks=create_twitter_tasks(topic),
        verbose=True
    )
    
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    topic = "AI Technology"
    result = run_twitter_crew(topic)
    print(result)
