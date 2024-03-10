import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
speech_engine = pyttsx3.init()
speech_engine.setProperty('rate', 150)  # Adjust the speaking rate

def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("You said: " + query + "\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble processing your request.")
        return ""

if __name__ == '__main__':
    speak("Hello there! I'm your assistant. How may I assist you?")

    while True:
        user_input = listen()

        if 'wikipedia' in user_input:
            speak("Searching Wikipedia...")
            user_input = user_input.replace("wikipedia", "")
            result = wikipedia.summary(user_input, sentences=2)
            speak("According to Wikipedia...")
            speak(result)
        elif 'who are you' in user_input:
            speak("I am your virtual assistant.")
        elif 'open' in user_input:
            if 'youtube' in user_input:
                speak("Opening YouTube...")
                webbrowser.open("https://www.youtube.com")
            elif 'google' in user_input:
                speak("Opening Google...")
                webbrowser.open("https://www.google.com")
            elif 'github' in user_input:
                speak("Opening GitHub...")
                webbrowser.open("https://github.com")
            elif 'stackoverflow' in user_input:
                speak("Opening Stack Overflow...")
                webbrowser.open("https://stackoverflow.com")
            elif 'spotify' in user_input:
                speak("Opening Spotify...")
                webbrowser.open("https://www.spotify.com")
            elif 'whatsapp' in user_input:
                speak("Opening WhatsApp...")
                os.startfile("C:\\Users\\your_username\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            elif 'music' in user_input:
                speak("Opening music...")
                webbrowser.open("https://www.spotify.com")
            elif 'disk' in user_input:
                if 'd' in user_input:
                    speak("Opening local disk D...")
                    os.startfile("D:\\")
                elif 'c' in user_input:
                    speak("Opening local disk C...")
                    os.startfile("C:\\")
                elif 'e' in user_input:
                    speak("Opening local disk E...")
                    os.startfile("E:\\")
        elif 'sleep' in user_input:
            speak("Goodbye!")
            break
