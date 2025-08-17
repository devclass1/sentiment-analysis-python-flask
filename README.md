# Sentiment Analysis Web App

A **Flask-based web application** that analyzes the sentiment of user-provided text using both **VADER** and **TextBlob** sentiment analysis tools.

---

## 🚀 Features
- Sentiment analysis of user-provided text  
- Results classified as **Positive, Negative, or Neutral**  
- Detailed sentiment scores from **VADER** and **TextBlob**  
- Clean, responsive, and modern UI  
- Real-time analysis with both **form submission** and **API endpoint** support  
- Visual representation of sentiment scores  
- Mobile-friendly with error handling and loading states  

---

## 🛠 Technologies Used
- Python 3  
- Flask  
- TextBlob  
- NLTK VADER  
- HTML5, CSS3, JavaScript  
- Font Awesome Icons  

---
-------
# Project Structure
```
sentiment-analysis-app/
├── static/
│ ├── css/
│ │ └── style.css
│ └── js/
│ └── script.js
├── templates/
│ └── index.html
├── app.py
├── requirements.txt
├── README.md
└── sentiment_model.py
```
-------
## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app

# Sentiment Analysis Application

## 🚀 Getting Started

### Create and activate a virtual environment
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  

### Install dependencies
pip install -r requirements.txt  
python -m textblob.download_corpora  

### Run the application
python app.py  

### Open in browser
http://localhost:5000  

---

## 🌐 Deployment

### Run with Gunicorn
gunicorn app:app  

### Deployable on:
- Heroku  
- PythonAnywhere  
- AWS Elastic Beanstalk  
- Google App Engine  
- Any other WSGI-compatible hosting  

---

## 📡 API Endpoint

### Request
POST /analyze  
Content-Type: application/json  

{
    "text": "Your text to analyze here"
}

### Response
{
    "sentiment": "Positive",
    "vader_score": 0.1234,
    "textblob_score": 0.5678
}

---

## 📸 Screenshots
*(Add screenshots here)*

---

## 📜 License
This project is licensed under the **MIT License**.

