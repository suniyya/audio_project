""" Sends a request to Watson Speech to Text API to segment sentence into words """
import os
import json
from watson_developer_cloud import SpeechToTextV1

#APIKEY = {import from credentials or externally}
URL = 'https://stream.watsonplatform.net/speech-to-text/api'

def get_words_from_audio(filename):
    # Invoke a Speech to Text method
    SPEECH_TO_TEXT = SpeechToTextV1(
        iam_apikey=APIKEY,
        url=URL
    )
    print filename
    with open(filename, 'rb') as audio_file:
        speech_recognition_results = SPEECH_TO_TEXT.recognize(
            audio=audio_file,
            content_type='audio/wav',
            timestamps=True,
            word_alternatives_threshold=0.9
        ).get_result()

    result = speech_recognition_results
    return result
