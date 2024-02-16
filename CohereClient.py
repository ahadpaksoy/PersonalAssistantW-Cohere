import speech_recognition as sr
import pyttsx3
import cohere
co = cohere.Client('api_key')

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

for i in range(10):
    with sr.Microphone() as source:
        print("Listening...")
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            response = co.chat(message=text)
            print("Bot said: " + response.text)
            speak(response.text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.WaitTimeoutError:
            print("Timeout error")