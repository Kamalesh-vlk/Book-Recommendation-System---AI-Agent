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
<img width="1366" height="625" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/fa1b82a3-0efb-4be3-a0af-e9a8e5b841fe" />
<img width="1366" height="617" alt="Screenshot (16)" src="https://github.com/user-attachments/assets/6c92ddc5-b7a6-49ca-9040-95b9ed7a1eab" />
<img width="1366" height="606" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/d2bea921-42c4-4f99-b842-328d4f233771" />
<img width="1366" height="617" alt="Screenshot (18)" src="https://github.com/user-attachments/assets/7bfdd408-c494-4500-b89a-c88472345c97" />




