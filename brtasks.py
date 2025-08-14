# brtasks.py
from crewai import Task
from textwrap import dedent

class CustomTasks:
    def __tip_section(self):
        return "If you provide great recommendations, I'll gift you a lifetime supply of books!"

    def build_profile_task(self, agent, reading_history, user_preferences):
        return Task(
            description=dedent(f"""
                Analyze the user's reading history and preferences to create a
                structured reading profile with genres, themes, and styles.

                Reading History: {reading_history}
                Preferences: {user_preferences}

                {self.__tip_section()}
                Make sure to identify unique reading patterns and keyword themes.
            """),
            expected_output="A detailed reader profile in structured format (JSON or bullet list).",
            agent=agent,
        )

    def recommend_books_task(self, agent):
        return Task(
            description=dedent(f"""
                Take the reader profile from Task 1 and recommend at least 5 books
                that match the profile. Include book title, author, genre, and
                a short reason for each suggestion.

                {self.__tip_section()}
                Include at least one 'hidden gem' outside the primary genre.
            """),
            expected_output="Ranked list of book recommendations with reasons.",
            agent=agent,
        )
