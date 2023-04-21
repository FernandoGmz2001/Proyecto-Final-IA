import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
from playsound import playsound
from src.configuration import *

# name
name = 'sara'

# attempts
attempts = 0

voiceSpeed = 178
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', voiceSpeed)
engine.setProperty('volume', 0.7)
engine.runAndWait()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def initialSound():
    playsound(soundPath)


def exitSound():
    playsound(exitsoundPath)


def getAudio():
    listener = sr.Recognizer()
    status = False

    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=0.2)
        initialSound()
        print(f"{green_color}({attempts}) Escuchando...{normal_color}")
        # Se ajusta al ruido ambiental
        # Realiza la escucha
        listener.pause_threshold = 1
        listener.energy_threshold = 400
        voice = listener.listen(source, timeout=5)
        command = ""
        # Reconoce el audio

        try:
            command = listener.recognize_google(
                voice, language='es-mx').lower()
            if name in command:
                command = command.replace(f"{name} ", "").replace("á", "a").replace(
                    "é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True
                print(command)
            else:
                print(f"Vuelte a intentarlo , no reconozco {command}")
        except:
            pass
        return {'text': command, 'status': status}


while True:
    rec_json = getAudio()
    query = rec_json['text']
    status = rec_json['status']

    if status:
        if 'estas ahi' in query:
            speak('Si, estoy aquí')

        elif 'hola' in query or 'saludame' in query or 'como estas' in query:
            speak("¡Hola!, como le puedo ayudar.")

        elif 'reproduce' in query:
            music = query.replace('reproduce', '')
            speak(f'Reproduciendo {music}')
            pywhatkit.playonyt(music)
            break

        elif 'gracias' in query or 'cancelate' in query or 'adios' in query or 'basta' in query:
            exitSound()
            break

        elif 'en youtube' in query or 'un video' in query or 'el video' in query:
            speak("Esto es lo que encontré en youtube")
            query = query.replace('Busca a en youtube', '').replace(
                'Abre un video', '').replace('Busca el video', '').replace('Busca un video de', '').replace('Pon un video de', '').replace('ponme un video de', '').replace('ponme un video del', '')
            webSearch = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(webSearch)
            speak("Listo")
            break

        elif 'en google' in query or 'que es' in query or 'que pasaria si' in query or 'que significa' in query or 'que necesito para' in query or 'cuando' in query or 'quien' in query or 'como' in query or 'donde' in query or 'por que' in query or 'definicion' in query or 'porque' in query or 'cual' in query or 'quien' in query or 'busca' in query:

            speak("Esto es lo que encontré:")
            query = query.replace("busca", "").replace("en google", "")
            pywhatkit.search(query)
            break

        else:
            print(f"Vuelve a intentarlo, no reconozco: {query}")
        attempts = 0
    else:
        attempts += 1
