# 🌌 AI Astrologer Agent

This is an AI-powered Astrologer Agent built with **Flask** and **Google Gemini API**.  
It takes user details (like birth date, time, and location), processes them using **Kerykeion**, and generates astrological insights.

---

## 🚀 Features
- Collects user details through a Flask form.
- Uses **Kerykeion** to generate astrological charts.
- Sends the processed data to **Google Gemini AI** for insights.
- Securely handles API keys with **python-dotenv**.
- Simple and extensible architecture.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

git clone https://github.com/your-username/astro-agent.git
cd astro-agent

### 2. Create virtual environment**
python -m venv venv

activate it
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Setup Environment Variables
GEMINI_API_KEY=your_api_key_here

### 5. Run the Flask app
python app.py

the app will run on
http://127.0.0.1:5000


### Project Structure
astro-agent/
│── app.py          # Flask application
│── agent.py        # Core agent logic
│── requirements.txt # Python dependencies
│── .env            # API key (not pushed to GitHub)
│── .gitignore      # Ignore venv & .env
│── README.md       # Project documentation


### Dependencies
Flask,
Kerykeion,
python-dotenv,
google-generativeai




