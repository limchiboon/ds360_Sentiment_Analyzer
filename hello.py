from flask import Flask, request, render_template

#import natural language toolkit
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('senti.html')
#def hello_world():
#    return "<p>Hello, World!</p>"

@app.route("/sentiment")
def analyze():
    #s = "Today is voting day, i am so excited to vote"

    args = request.args
    s = args.get("s")

    analyze = SentimentIntensityAnalyzer()
    score = analyze.polarity_scores(s)
    return score