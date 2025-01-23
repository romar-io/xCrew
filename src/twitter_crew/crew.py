from typing import List
from crewai import Crew, Task
from .tools import TwitterTools
from .agents import create_agents

class TwitterCrew:
    def __init__(self, twitter_tools: TwitterTools):
        self.agents = create_agents(twitter_tools)
        self.researcher = self.agents[0]
        self.writer = self.agents[1]
        self.publisher = self.agents[2]
        self.analyzer = self.agents[3]
        
    def create_tasks(self, topic: str) -> List[Task]:
        research_task = Task(
            description=f"""Research the latest trending information about {topic}. 
            Focus on:
            1. Current viral discussions and hashtags
            2. Key influencers talking about this topic
            3. Related trending subtopics
            4. Audience sentiment and engagement patterns
            5. Potential viral angles or hooks
            
            Provide specific examples and data points that could make tweets more engaging.""",
            agent=self.researcher
        )

        writing_task = Task(
            description="""Using the research insights, create a series of engaging tweets.
            Requirements:
            1. Create 3-5 tweet variations
            2. Include relevant hashtags
            3. Optimize for virality and engagement
            4. Stay within 280 characters
            5. Consider thread potential
            
            Format each tweet with engagement hooks and proper spacing.""",
            agent=self.writer
        )

        publishing_task = Task(
            description="""Review and optimize the tweets for publishing.
            Steps:
            1. Check compliance with Twitter guidelines
            2. Verify hashtag optimization
            3. Assess timing for maximum engagement
            4. Review for potential sensitive content
            5. Publish the best performing variation
            
            Provide publishing metrics and initial engagement data.""",
            agent=self.publisher
        )

        analysis_task = Task(
            description="""Analyze the published tweet's performance and provide insights.
            Include:
            1. Initial engagement metrics
            2. Audience response patterns
            3. Hashtag performance
            4. Recommendations for future tweets
            5. Trend alignment analysis
            
            Suggest optimizations for future content.""",
            agent=self.analyzer
        )

        return [research_task, writing_task, publishing_task, analysis_task]

    def run(self, topic: str):
        crew = Crew(
            agents=self.agents,
            tasks=self.create_tasks(topic),
            verbose=True,
            process_type="sequential"
        )
        
        return crew.kickoff() 