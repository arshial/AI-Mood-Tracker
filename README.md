# 🧠 AI Mood Tracker

An **AI-powered journal sentiment tracker** built with Python.  
It analyzes your daily text entries, classifies your mood (positive / neutral / negative), stores them in a local database, and visualizes trends over time.  
The app supports both a **rule-based** model and a **Hugging Face transformer** for multilingual contextual sentiment analysis.

---

## 🚀 Features

✅ **Dual backend** — switch between `rule` or `hf` (Hugging Face)  
✅ **FastAPI REST API** — lightweight, clean, and extendable  
✅ **Streamlit Dashboard** — visual mood tracking  
✅ **SQLite storage** — persistent history of your mood  
✅ **Matplotlib visualization** — auto-generated trend chart  
✅ **Multilingual support** — English + others via transformer  

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| Language | Python 3.10+ |
| NLP | Hugging Face Transformers (`distilbert-base-multilingual-cased`) |
| API | FastAPI |
| UI | Streamlit |
| Database | SQLite |
| Visualization | Matplotlib |

---

## ⚙️ Quickstart

### 1️⃣  Setup Environment
```bash
git clone https://github.com/arshial/ai-mood-tracker.git
cd ai-mood-tracker
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### 2️⃣ Configure
edit .env.example:
```bash
MODEL_BACKEND=rule   # or hf
DB_PATH=data/mood.db
```
### 🧠 Run the CLI (MVP)
```bash
python scripts/run_mvp.py
```
Example session:
```bash
== AI Mood Tracker MVP ==
Enter text (or 'q' to quit): I feel happy today
→ label=positive score=1.00 meta={'pos_hits': 1, 'neg_hits': 0, 'total_hits': 1}
✓ Trend plot updated: data/processed/daily_trend.png
```
---
## 🧠 Switching Between Backends
| Backend | Description                        | Env Setting          |
| ------- | ---------------------------------- | -------------------- |
| `rule`  | Fast keyword-based analysis        | `MODEL_BACKEND=rule` |
| `hf`    | Transformer model via Hugging Face | `MODEL_BACKEND=hf`   |

---
## 🧰 Development Notes
- Persistent storage: every analysis entry is stored in data/mood.db
- Visualization: daily average sentiment score plotted automatically
- HF model caching: loaded once and reused across sessions
- Testable design: each module can be tested independently
---
## 🧑‍💻 Author
### Arshia Lashgari

📍 Naples, Italy 

🚀 Computer Science Student @ Federico II

💡 Passionate about AI, Python, and full-stack development

---
## 🧾 License

This project is licensed under the MIT License

