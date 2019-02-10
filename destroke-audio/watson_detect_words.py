""" TO DO """
import os
import json
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import WatsonApiException
# should be an env variable
APIKEY = 'JaWmzATHSjKOv5gkKeXOyVuBjNsmT_aVCfc51FuBINqe'
URL = 'https://stream.watsonplatform.net/speech-to-text/api'
FILES = os.listdir('./audio_files')

for filename in FILES:
    print os.path.join('./audio_files/', filename)

    # Invoke a Speech to Text method
speech_to_text = SpeechToTextV1(
    iam_apikey=APIKEY,
    url=URL
)

for filename in FILES:
    with open(os.path.join('./audio_files/', filename), 'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav',
            timestamps=True,
            word_alternatives_threshold=0.5,
            keywords=['chair', 'cactus', 'glove', 'feather', 'key'],
            keywords_threshold=0.5
        ).get_result()

    print json.dumps(speech_recognition_results, indent=2)
