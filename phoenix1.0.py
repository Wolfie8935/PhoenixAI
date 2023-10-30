import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speech_recognition and calling it as "sr"

import datetime #obviously for date and time

engine = pyttsx3.init() #initializing

def speak(audio):    
    engine.say(audio) #function through which we can ask what to say
    engine.runAndWait() #Function which waits first to complete excecution and when
                        #it is completed then only it will continue till then wait

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #for 24 hr clock (%H for 12 hr)
    speak("Time would be,") #the speak functions says the stufff mannnnn
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("Today's Date is, well you guessed it")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Partner!")
    time_()
    date_()

    #greetings at different timings using vohi if else
    hour = datetime.datetime.now().hour #storing hour value in variable
    if hour >= 0 and hour <= 4:
        speak("A beautiful late night isn't it partner... I am sure you must be working on a beautiful masterpiece")
    elif hour > 4 and hour <= 6:
        speak("A very good morning partner. An early start to the day will definately help you.")
    elif hour > 6 and hour < 12:
        speak("Good Morning Partner. Let's win this day together!")
    elif hour >= 12 and hour <= 18:
        speak("Good Evening Partner. How are you doing?")
    elif hour > 18 and hour <=24:
        speak("Good Evening Partner. How are you doing?")
    else:
        speak("YOU HAVE REACHED A BUG WHICH SHOULD NOT HAPPEN")
    
    speak("Phoenix at your service... How can I assist you today?")

def TakeCommand():
    r = sr.Recognizer() # its a playable function which recognizes the voice
    with sr.Microphone() as source: #microphone is also a playable function 
        print("Listening.....")
        r.pause_threshold = 1 #how long it will wait for user to command
        audio = r.listen(source) #it will listen and recognise and will store in the variable source

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en-US")
        print(query)

    except Exception as e:
        print(e)
        print("Can you repeat it for me... there was a bug irritating me so couldn't hear")
        return "None"
    return query

if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower() #we did this because we want to store everything in
                                    #lowercase so its easy to work on
        
        if "date" in query: #tell the date
            date_()

        if "time" in query: #tell the time
            time_()