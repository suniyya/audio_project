""" A simple UI to input and display """
from Tkinter import *
from play_clip import play
import compare_speech as speech
from watson_segment_sentence import get_words_from_audio

window = Tk()
window.title('Speech Assessment')
label = Label(window, text='DeStroke Speech Demo', font=('Arial Bold', 20))
label.grid(column=1, row=1)
window.geometry('700x300')
PATH = './sentence_files/'

## Label and input box for first sound file
sublabel = Label(window, text='Baseline Recordings:')
sublabel.grid(column=1, row=3)
baseline_file = Entry(window, width=15)
baseline_file.insert(0, 'home_normal_1.wav')
baseline_file.grid(column=1, row=4)
## Label and input box for second sound file
second_sublabel = Label(window, text='Test Recordings:')
second_sublabel.grid(column=1, row=7)
compare_file = Entry(window, width=15)
compare_file.insert(0, 'home_stroke_2.wav')
compare_file.grid(column=1, row=8)

label_result = Entry(window, width=75, bg="pink")
label_result.grid(column=1, row=10)
label_result.insert(0, "A score close to 1 is normal, close to 0 is indicative of a complete mismatch, i.e. high risk for stroke.")
result = Entry(window, font=('Arial Bold', 16), fg="blue", width=55)
result.grid(column=1, row=16)

def play_both():
    print 'Baseline Sentence Recording...'
    play(PATH+baseline_file.get())
    print 'Test Sentence Recording...'
    play(PATH+compare_file.get())

def stroke_score():
    baseline_data = speech.initialize(get_words_from_audio(PATH+baseline_file.get()))
    print baseline_data
    current_data = speech.initialize(get_words_from_audio(PATH+compare_file.get()))
    print current_data
    word_match = speech.wordsEquality(current_data, baseline_data)
    length_match = 'YES' if speech.lengthTest(baseline_data, current_data) == 1 else 'NO'

    if word_match == 0:
        result.insert(0, 'HIGH RISK: WORDS DID NOT MATCH')
    elif word_match == 1:
        result.insert(0, 'SPEED OF SPEECH MATCH: '+ length_match)
    else:
        result.insert(0, 'WORD MATCH: '+str(word_match*100)+ '%')


## Buttons
play_button = Button(window, text="Play", command=play_both)
play_button.grid(column=1, row=12)
assess_speech_button = Button(window, text="Compare Speech", command=stroke_score)
assess_speech_button.grid(column=1, row=14)

window.mainloop()