# 📚 AI-Powered Book Recommendation System

A smart AI-driven book recommendation system that personalizes suggestions based on your reading tastes, favorite genres, and past reads.  
Uses a multi-agent approach with **Cohere LLMs** to deliver accurate, diverse, and explainable book recommendations.

---

## 🚀 Features
- 🎯 **Personalized AI Recommendations** based on user preferences and reading history  
- 🤖 **Multi-Agent Architecture** using CrewAI  
- 🌐 **Streamlit Web Interface** for easy interaction  
- 📊 **Explainable Suggestions** with reasoning behind each recommendation  

---

## 🛠 Tech Stack
- **Python 3.10+**
- **Cohere API**
- **CrewAI (Multi-Agent Framework)**
- **Streamlit** for UI
- **Python-Decouple** for environment variables

---
## 🔑 Environment Setup
Create a .env file in the root:

COHERE_API_KEY=your_cohere_api_key_here

⚠ Important: Never commit your .env file to GitHub.

---
## 🖥 Usage

Open the Streamlit web interface

Enter favorite genres, writing style, themes, and optionally book history

Click "Get Recommendations"

Receive 5+ AI-generated book suggestions with explanations
---
## 💡 Example Input

User Preferences JSON:
```
{
  "favorite_genres": ["Fantasy", "Adventure"],
  "style": "Fast-paced and immersive",
  "themes": ["Courage", "Friendship"]
}

```
Book History JSON:
```
{
  "history": [
    {"title": "The Hobbit", "rating": 5},
    {"title": "Harry Potter", "rating": 4}
  ]
}
```
---
## ▶️ Run the Application
```
streamlit run brmain.py
```
---
## 📸 Screenshots
![book recommendation system](https://github.com/user-attachments/assets/b0b9aad2-b07d-4fe1-9d3b-0d454cf28686)





