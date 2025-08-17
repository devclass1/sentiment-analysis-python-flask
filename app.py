from flask import Flask, render_template, request, jsonify
from sentiment_model import SentimentAnalyzer
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
analyzer = SentimentAnalyzer()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('feedback-text', '')
        if text.strip():
            sentiment, scores = analyzer.analyze(text)
            return render_template('index.html', 
                                text=text,
                                sentiment=sentiment,
                                vader_score=scores['vader'],
                                textblob_score=scores['textblob'],
                                show_result=True)
    
    return render_template('index.html', show_result=False)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    if text.strip():
        sentiment, scores = analyzer.analyze(text)
        return jsonify({
            'sentiment': sentiment,
            'vader_score': scores['vader'],
            'textblob_score': scores['textblob']
        })
    
    return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
