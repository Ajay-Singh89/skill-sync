---

## ✨ Features

- 📊 Track skills with proficiency levels  
- 💾 Persistent storage using database  
- ⚡ Fast REST APIs built with FastAPI  
- 🧠 Foundation for smart recommendations  

---

## 🛠️ Tech Stack

- **Backend:** FastAPI  
- **Database:** SQLite (SQLAlchemy)  
- **Language:** Python  

---

## 📂 Project Structure


skill-sync/
│
├── main.py # API routes
├── models.py # Database models
├── database.py # DB connection
├── requirements.txt
└── README.md


---

## 🚀 How to Run Locally

```bash
git clone https://github.com/Ajay-Singh89/skill-sync.git
cd skill-sync

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
uvicorn main:app --reload
```
---

📌 API Endpoints
Method	Endpoint	Description
GET	/	Check API status
POST	/add-skill	Add a new skill
GET	/skills	Get all skills
POST	/signup	Create user

---
📌 Future Improvements
🔐 JWT Authentication
🤖 Resume Analyzer (NLP-based)
💼 Job Application Tracking
📱 Mobile App Integration (Flutter)

---

👨‍💻 Author

Ajay Singh

---

⭐ Support

If you like this project, give it a ⭐ on GitHub!
