from numpy import extract
import speech_recognition as sr
import nltk
import speakEngine
import re
import nltk
import re
speakEngine = speakEngine.SpeakEngine()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_duration(text):
    duration_regex = re.compile(r"""
    (?:(?P<hours>\d+)\s?(?:hours|hour|h))?  # Match optional hours 
    \s+                                     # Require whitespace between hours and minute sections
    ((?P<minutes>\d+)\s?(?:minutes|min|m)) # Match minutes 
""", re.IGNORECASE | re.VERBOSE) 


    match = duration_regex.search(text)

    if match:
        hours = int(match.group('hours')) if match.group('hours') else 0
        minutes = int(match.group('minutes')) if match.group('minutes') else 0
        total_minutes = (hours * 60) + minutes
        return total_minutes
    else:
        return None



def set_timer(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    
    if "set" in tokens and "timer" in tokens:
        duration = extract_duration(text)
        speakEngine.speak("Timer set for " + str(duration) + " minutes")
        print("Timer set for " + str(duration) + " minutes")
    else:
        speakEngine.speak("I'm sorry, I didn't understand that")
        print("I'm sorry, I didn't understand that")

# The output of this code is:
# Timer set for 10 minutes
