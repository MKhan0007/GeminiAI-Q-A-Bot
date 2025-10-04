# AI Q&A Bot

A simple **Python-based general Q&A bot** powered by **Google Gemini 2.5 Flash** model.  
This bot provides answers to general questions through a **Streamlit web interface**.

---

## 🚀 Features

- General Q&A using Gemini 2.5 Flash (free-tier model)
- Lightweight and easy to run
- Streamlit-based interactive UI
- Secure API key management via `.env`

---

## 📂 Project Structure

AI-Q-A-Bot/
│── app.py # Streamlit app
│── requirements.txt # Python dependencies
│── .gitignore # Files to ignore in Git
│── README.md # Project README
│── .env # Stores Gemini API key (not committed to GitHub)

## ⚙️ Setup

1. **Clone the repository**

```bash
git clone https://github.com/MKhan0007/AI-Q-A-Bot.git
cd AI-Q-A-Bot
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

Windows:
```bash
.\venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```
5. **Set up your Gemini API key**

Create a .env file in the project root:
GEMINI_API_KEY=your_api_key_here

6. **Run the Streamlit app:**

```bash
streamlit run app.py
```

## 🤖 Supported Model:

***Recommended: models/gemini-2.5-flash (free tier)***
***Optional: models/gemini-flash-latest or models/gemini-2.5-pro***

## 📦 Dependencies

***streamlit***
***python-dotenv***
***google-generativeai***

## 📜 License

***This project licensed under the MIT License***