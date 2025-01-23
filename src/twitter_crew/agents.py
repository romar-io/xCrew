from typing import List
from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun

class AgentFactory:
    def __init__(self, twitter_tools):
        self.twitter_tools = twitter_tools
        self.search_tool = DuckDuckGoSearchRun()

    def create_researcher(self) -> Agent:
        return Agent(
            role='Social Media Researcher',
            goal='Research and analyze trending topics to identify viral content opportunities',
            backstory="""You are an elite social media researcher and trend analyst with 
            years of experience identifying viral content before it peaks. You have a deep 
            understanding of what makes content spread on Twitter and can spot emerging 
            trends early. You combine data analysis with cultural awareness to find the 
            most engaging topics.""",
            tools=[self.search_tool],
            allow_delegation=True,
            verbose=True,
            memory=True,
            max_iterations=3,
            max_rpm=10
        )

    def create_writer(self) -> Agent:
        return Agent(
            role='Twitter Content Strategist',
            goal='Craft viral, engaging tweets that drive maximum engagement',
            backstory="""You are a master of Twitter engagement, having crafted viral 
            tweets for major brands and influencers. You understand the psychology of 
            what makes people retweet and engage. You know how to use humor, timing, 
            and cultural references to create tweets that resonate. You're an expert 
            in Twitter's best practices and engagement patterns.""",
            tools=[self.search_tool],
            allow_delegation=True,
            verbose=True,
            memory=True,
            max_iterations=2,
            max_rpm=10
        )

    def create_publisher(self) -> Agent:
        return Agent(
            role='Twitter Publishing Manager',
            goal='Ensure tweets are optimized for maximum impact and compliance',
            backstory="""You are a seasoned social media manager who understands 
            Twitter's guidelines inside and out. You know the best times to post, 
            how to optimize hashtags, and how to ensure content meets community 
            standards while maximizing reach. You've managed high-profile accounts 
            and know how to time posts for maximum engagement.""",
            tools=[self.twitter_tools.post_tweet],
            allow_delegation=False,
            verbose=True,
            memory=True,
            max_iterations=1,
            max_rpm=5
        )

    def create_engagement_analyzer(self) -> Agent:
        return Agent(
            role='Engagement Analyst',
            goal='Analyze tweet performance and provide optimization insights',
            backstory="""You are an expert in social media analytics with a 
            specialization in Twitter metrics. You understand engagement patterns,
            audience behavior, and can provide data-driven insights to improve 
            tweet performance. You know how to interpret metrics to optimize future 
            content.""",
            tools=[self.search_tool],
            allow_delegation=True,
            verbose=True,
            memory=True,
            max_iterations=2,
            max_rpm=10
        )

def create_agents(twitter_tools) -> List[Agent]:
    """Create and return all agents needed for the Twitter crew"""
    factory = AgentFactory(twitter_tools)
    return [
        factory.create_researcher(),
        factory.create_writer(),
        factory.create_publisher(),
        factory.create_engagement_analyzer()
    ] 