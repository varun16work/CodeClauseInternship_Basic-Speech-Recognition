from django.shortcuts import render
from django.http import JsonResponse
import speech_recognition as sr
import pyttsx3
def index(request):
    recognized_text = ""
    if request.method == "POST":
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source, timeout=5)
            try:
                recognized_text = recognizer.recognize_google(audio_data)
                text_to_speech(recognized_text)
            except sr.UnknownValueError:
                recognized_text = "Could not understand audio. Speak loud and clear!!!!"
            except sr.RequestError:
                recognized_text = "Could not request results!"
        return JsonResponse({'recognized_text': recognized_text})
    return render(request, 'index.html', {'recognized_text': recognized_text})
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()