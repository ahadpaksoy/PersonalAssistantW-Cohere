# Personal Assistant with Cohere

This project uses the `speech_recognition`, `nltk` and `pyttsx3` libraries for speech recognition, natural language processing and text-to-speech, and the `Cohere` for chatbot functionality.

## Files

- `CohereClient.py`: This script listens for speech input, recognizes it, sends it to the Cohere chatbot, and speaks the chatbot's response.
- `speechRecgonizer.py`: This script contains the `SpeechRecognizer` class, which encapsulates the speech recognition and text-to-speech functionality.
- `nlp_tagging.py`: This script will extract the duration from the text and convert it to minutes.

## Usage

1. Install the required libraries: 

```bash
pip install speechrecognition pyttsx3 cohere
pip install nltk
```
2. Run main.py:

```bash
python CohereClient.py
# or
python main.py
```
Note
Please replace 'api_key' with your actual Cohere API key in CohereClient.py.
