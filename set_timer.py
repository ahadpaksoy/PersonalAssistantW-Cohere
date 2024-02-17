# Description: This file contains the class set_timer which is used to set a timer for a given duration.
import nltk
import speakEngine
import timer

class set_timer:
    def __init__(self,text):
        self.speakEngine = speakEngine.SpeakEngine()
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')

    def set_timer(self, text):
        tokens = nltk.word_tokenize(text)

        if "set" in tokens and "timer" in tokens:
            minutes = timer.extract_duration(text)
            speak_engine = speakEngine.SpeakEngine()  # Create an instance of the SpeakEngine class
            speak_engine.speak("Timer set for " + str(minutes) + " minutes")  # Call the speak method on the speak_engine instance, passing the text parameter
            print("Timer set for " + str(minutes) + " minutes")
        else:
            speak_engine = speakEngine.SpeakEngine()
            speak_engine.speak("I'm sorry, I didn't understand that")
            print("I'm sorry, I didn't understand that")
