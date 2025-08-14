# brmain.py
import os
import json
import streamlit as st
from decouple import config
from crewai import Crew
from bragent import CustomAgents
from brtasks import CustomTasks

# --- Load Cohere API Key (from .env or environment) ---
os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY", config("COHERE_API_KEY", default=""))

# --- Streamlit Page Setup ---
st.set_page_config(page_title="📚 Cohere Book Recommender", layout="wide")
st.title("📚 Cohere + CrewAI: Book Recommendation System")
st.caption("Two-Agent setup: Reader Profile Builder → Smart Book Recommender")

# --- Helper to pretty print recommendations if they look like JSON ---
def try_parse_json(text: str):
    try:
        return json.loads(text)
    except Exception:
        return None

# --- Sample placeholders to help the user start ---
DEFAULT_PREFERENCES = {
    "genres": ["Fantasy", "Sci-Fi"],
    "writing_style": "Fast-paced, immersive worldbuilding",
    "favorite_authors": ["Brandon Sanderson", "N. K. Jemisin"],
    "length": "Series preferred",
    "language": "English"
}
DEFAULT_HISTORY = [
    {"title": "Mistborn", "author": "Brandon Sanderson", "rating": 5, "completed": True},
    {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "rating": 5, "completed": True},
    {"title": "Dune", "author": "Frank Herbert", "rating": 4, "completed": False}
]

# --- Sidebar: API Key status ---
with st.sidebar:
    st.subheader("🔐 API")
    if os.environ.get("COHERE_API_KEY"):
        st.success("Cohere API key loaded")
    else:
        st.error("Missing COHERE_API_KEY. Add it to your .env or environment.")

    st.markdown("---")
    st.markdown("**How it works**")
    st.write(
        "- Agent 1 builds a structured reader profile from your inputs.\n"
        "- Agent 2 recommends books using content & collaborative signals."
    )

# --- Inputs ---
st.header("1) Your Reading Preferences")
prefs_text = st.text_area(
    "JSON or short description",
    value=json.dumps(DEFAULT_PREFERENCES, indent=2),
    height=180
)

st.header("2) Your Reading History")
history_text = st.text_area(
    "JSON (list of books with ratings/completion) or plain text",
    value=json.dumps(DEFAULT_HISTORY, indent=2),
    height=220
)

col1, col2 = st.columns([1, 1])
with col1:
    run_btn = st.button("🚀 Generate Recommendations", type="primary")
with col2:
    clear_btn = st.button("🧹 Clear")

if clear_btn:
    st.experimental_rerun()

if run_btn:
    # Parse inputs permissively (JSON → dict/list; else keep as string)
    try:
        user_preferences = json.loads(prefs_text)
    except Exception:
        user_preferences = {"description": prefs_text}

    try:
        reading_history = json.loads(history_text)
    except Exception:
        reading_history = {"history": history_text}

    st.info("Running CrewAI agents…")

    try:
        # Init agents & tasks
        agents = CustomAgents()
        tasks = CustomTasks()

        agent_profile = agents.reader_profile_builder()
        agent_reco = agents.smart_book_recommender()

        task1 = tasks.build_profile_task(agent_profile, reading_history, user_preferences)
        task2 = tasks.recommend_books_task(agent_reco)

        crew = Crew(
            agents=[agent_profile, agent_reco],
            tasks=[task1, task2],
            verbose=False
        )

        result = crew.kickoff()

        st.success("Done!")

        st.header("✅ Final Output")
        # CrewAI often returns a string; try to parse JSON if possible
        parsed = try_parse_json(result) if isinstance(result, str) else None

        # If it looks like a structured object with recommendations, render “cards”
        if parsed and isinstance(parsed, (dict, list)):
            # try common shapes:
            candidates = []
            if isinstance(parsed, dict):
                # possibles: {"profile": {...}, "recommendations": [...]}
                if "recommendations" in parsed and isinstance(parsed["recommendations"], list):
                    candidates = parsed["recommendations"]
                else:
                    # if dict isn’t standard, just show it:
                    st.json(parsed)
            elif isinstance(parsed, list):
                candidates = parsed

            if candidates:
                st.subheader("📖 Recommendations")
                for i, item in enumerate(candidates, 1):
                    # expected fields (best-effort)
                    title = item.get("title") if isinstance(item, dict) else str(item)
                    author = item.get("author") if isinstance(item, dict) else ""
                    reason = item.get("reason") if isinstance(item, dict) else ""
                    genre = item.get("genre") if isinstance(item, dict) else ""

                    with st.container():
                        st.markdown(f"**{i}. {title}**" + (f" — *{author}*" if author else ""))
                        meta = []
                        if genre: meta.append(f"Genre: {genre}")
                        if meta:
                            st.caption(" • ".join(meta))
                        if reason:
                            st.write(f"**Why:** {reason}")
                        st.markdown("---")
            else:
                # show whatever structured object we got
                st.json(parsed)
        else:
            # fallback: just show the text result nicely
            st.code(result if isinstance(result, str) else str(result))

        # Expanders to show intermediate context if Crew returns it
        with st.expander("🔎 Raw Result (debug)"):
            st.write(result)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
        st.stop()

# --- Footer ---
st.markdown("---")
st.caption("Built with Cohere + CrewAI • Reader Profile Builder → Smart Book Recommender")
