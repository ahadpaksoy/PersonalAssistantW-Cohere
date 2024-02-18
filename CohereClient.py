import speech_recognition as sr
import pyttsx3
import cohere
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\recognizer\\recognizer.json"

co = cohere.Client('api_key')

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

chat_history = []

for i in range(10):
    with sr.Microphone() as source:
        print("Listening...")
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=30)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google_cloud(audio)
            print("You said: " + str(text))
            response = co.chat(message=str(text), temperature=0.8, chat_history=chat_history)
            answer = response.text  # Fix: Pass text as a string argument
            print("Bot said: " + answer)
            speak(response.text)

            user_message = {
                "user_name": "User",
                "text": text
            }
            bot_message = {
                "user_name": "Bot",
                "text": answer
            }
            chat_history.append(user_message)
            chat_history.append(bot_message)
            chat_history.append(user_message)
            chat_history.append(bot_message)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.WaitTimeoutError:
            print("Timeout error")