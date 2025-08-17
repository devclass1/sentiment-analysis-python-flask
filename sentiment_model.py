from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()
    
    def analyze_textblob(self, text):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0:
            return "Positive", polarity
        elif polarity < 0:
            return "Negative", polarity
        else:
            return "Neutral", polarity
    
    def analyze_vader(self, text):
        scores = self.sid.polarity_scores(text)
        compound = scores['compound']
        
        if compound >= 0.05:
            return "Positive", compound
        elif compound <= -0.05:
            return "Negative", compound
        else:
            return "Neutral", compound
    
    def analyze(self, text):
        vader_result, vader_score = self.analyze_vader(text)
        textblob_result, textblob_score = self.analyze_textblob(text)
        
        # Simple voting system
        if vader_result == textblob_result:
            return vader_result, {"vader": vader_score, "textblob": textblob_score}
        else:
            if abs(vader_score) > abs(textblob_score):
                return vader_result, {"vader": vader_score, "textblob": textblob_score}
            else:
                return textblob_result, {"vader": vader_score, "textblob": textblob_score}
