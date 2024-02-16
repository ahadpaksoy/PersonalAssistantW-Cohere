# Speech Recognition with Cohere

This project uses the `speech_recognition` and `pyttsx3` libraries for speech recognition and text-to-speech, and the `cohere` library for chatbot functionality.

## Files

- `CohereClient.py`: This script listens for speech input, recognizes it, sends it to the Cohere chatbot, and speaks the chatbot's response.
- `speechRecgonizer.py`: This script contains the `SpeechRecognizer` class, which encapsulates the speech recognition and text-to-speech functionality.

## Usage

1. Install the required libraries:

```bash
pip install speechrecognition pyttsx3 cohere
```
2. Run CohereClient.py:

```bash
python CohereClient.py
```

The script will listen for speech input, recognize it, send it to the Cohere chatbot, and speak the chatbot's response.

Note
Please replace 'api_key' with your actual Cohere API key in CohereClient.py.