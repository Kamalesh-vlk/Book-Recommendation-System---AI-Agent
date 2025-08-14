# bragent.py
from crewai import Agent
from textwrap import dedent
from langchain_cohere import ChatCohere
import os

# Load Cohere API Key from environment
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

class CustomAgents:
    def __init__(self):
        # Using Cohere's Command R+ model for conversational tasks
        self.cohere_llm = ChatCohere(
            model="command-r-plus",
            temperature=0.7,
            cohere_api_key=COHERE_API_KEY
        )

    def reader_profile_builder(self):
        return Agent(
            role="Reader Profile Builder",
            backstory=dedent("""
                You are an expert literary analyst and reading preference profiler.
                You collect and analyze the user's reading preferences such as genre,
                style, length, tone, language, and authors.
                You also analyze book history to extract common themes and keywords.
            """),
            goal=dedent("""
                Build a structured reader profile including genres, themes,
                styles, and unique reading habits based on provided data.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.cohere_llm,
        )

    def smart_book_recommender(self):
        return Agent(
            role="Smart Book Recommender",
            backstory=dedent("""
                You are a master book curator who finds perfect matches
                based on a user's reading profile.
                You combine content-based and collaborative filtering
                to suggest books that match interests while introducing novelty.
            """),
            goal=dedent("""
                Provide a ranked list of book recommendations with
                a brief reason for each suggestion, including 'hidden gems'
                beyond the user's typical genre.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.cohere_llm,
        )
