""" Given a path to an audio file, plays file """
import wave
import pyaudio

def play(sound_file):
    """ Play file """
    #define stream chunk
    chunk = 1024
    #open a wav format music
    sound = wave.open(sound_file, "rb")
    #instantiate PyAudio
    p_audio = pyaudio.PyAudio()
    #open stream
    stream = p_audio.open(format=p_audio.get_format_from_width(sound.getsampwidth()),
                          channels=sound.getnchannels(),
                          rate=sound.getframerate(),
                          output=True)
    #read data
    data = sound.readframes(chunk)

    #play stream
    while data:
        stream.write(data)
        data = sound.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p_audio.terminate()