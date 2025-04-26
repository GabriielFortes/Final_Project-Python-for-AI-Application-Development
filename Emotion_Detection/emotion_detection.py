'''
This module uses the embeddable Watson AI libraries to create an emotion detection application.
Emotion detection extends the concept of sentiment analysis by extracting more subtle emotions, 
such as happiness, sadness, anger, and so on, from statements rather than the simple polarity 
that sentiment analysis provides.
'''
import json
import requests

def emotion_detector(text_to_analyze):
    '''
    The function receives a parameter of type string and sends a 
    request to the Watson AI to analyze the string's emotions.
    '''
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
        )
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    dict_emotion = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=dict_emotion, headers=header, timeout=10)
    response_format = json.loads(response.text)

    emotions = response_format["emotionPredictions"][0]["emotion"]

    domination_emotion, domination_score = "", 0.0

    for emotion, score in emotions.items():
        if score > domination_score:
            domination_score = score
            domination_emotion = emotion

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "domination_emotion": domination_emotion
    }
