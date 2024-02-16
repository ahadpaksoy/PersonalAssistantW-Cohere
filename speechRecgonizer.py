import speech_recognition as sr
import pyttsx3

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

        
    def listen(self, timeout = 5):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout = timeout)
            try:
                print("Recognizing...")
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                return None
            except sr.WaitTimeoutError:
                print("Timeout error")
                return None