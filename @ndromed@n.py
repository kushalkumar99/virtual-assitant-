
import speech_recognition as sr
import pyttsx3 #for speak
import datetime
import wikipedia


engine = pyttsx3.init('sapi5') # Microsoft speech API --> uses in-built voices
voices = engine.getProperty('voices') # voices of male and female are available
#print(voices[1].id)
engine.setProperty('voice',voices[0].id) # '0' for male... '1' for female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hr = int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("good morning")

    elif hr>=12 and hr<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("I am kristel stanfia. you can call me kristy. how may i help you")  

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1 # time taken by kristy for listening
         audio = r.listen(source)

    try:
        print("Recognizing...")   
        query =  r.recognize_google (audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as   e:
        #print(e)
        print("say that again...")  
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower() #takecommand voice to text

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

