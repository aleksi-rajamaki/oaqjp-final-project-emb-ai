import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input_json, headers = header)   
    formatted_response = response.json()

    if response.status_code == 400: 
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
        return emotions
    
    else:
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        saddness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

        emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
            'fear': fear_score,
        'joy': joy_score,
        'sadness': saddness_score
        }

        emotions["dominant_emotion"] = max(emotions, key=emotions.get)

        return emotions








