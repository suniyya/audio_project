""" TO DO """
import speech_recognition as speech_recog
#from pocketsphinx import AudioFile

RECOGNIZER = speech_recog.Recognizer()

for i in range(2, 22):
    word = speech_recog.AudioFile('./audio_files/sample_'+ str(i)+'.wav')
    with word as source:
        audio = RECOGNIZER.record(source)
    print 'sphinx ', RECOGNIZER.recognize_sphinx(audio)
