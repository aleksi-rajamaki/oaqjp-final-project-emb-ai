""" Initiates the Flask application of "NLP - Emotion Detection" on localhost:5000
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyser():
    """ Analyses given text. Returns scores for each emotion and dominant emotion. """

    text_to_analyse = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is"
        f" 'anger:' {response['anger']}"
        f" 'disgust': {response['disgust']}"
        f" 'fear': {response['fear']}"
        f" 'joy' : {response['joy']}"
        f" and 'sadness': {response['sadness']}."
        f" The dominant emotion is <b>{response['dominant_emotion']}</b>")

@app.route("/")
def render_index_page():
    """ Renders the index page for "NLP - Emotion Detection" application. """   
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    