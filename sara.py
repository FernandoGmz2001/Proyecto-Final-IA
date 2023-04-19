import speech_recognition as sr
import pyttsx3


nombre = 'Sara'

listener = sr.Recognizer()
voiceSpeed = 150
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', voiceSpeed)
engine.say('Hola, como te puedo ayudar?')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        # Se ajusta al ruido ambiental
        listener.adjust_for_ambient_noise(source, duration=0.2)
        # Realiza la escucha
        listener.pause_threshold = 1
        listener.energy_threshold = 400
        print('Listening...')
        voice = listener.listen(source, timeout=5)
        # Reconoce el audio
        command = listener.recognize_google(voice, language='es-mx')
        command = command.lower()
        if nombre in command:
            command = command.replace(nombre, "")
        engine.say(command)
        engine.runAndWait()
except:
    pass
