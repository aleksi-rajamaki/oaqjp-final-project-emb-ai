from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyser():
    text_to_analyse = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyse)

    return (f"For the given statement, the system response is"
        f" 'anger:' {response['anger']}"
        f" 'disgust': {response['disgust']}"
        f" 'fear': {response['fear']}"
        f" 'joy' : {response['joy']}"
        f" and 'sadness': {response['sadness']}."
        f" The dominant emotion is <b>{response['dominant_emotion']}</b>")

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


