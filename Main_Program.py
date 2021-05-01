import speech_recognition as sr
import wikipedia as wiki
import datetime
import pyttsx3
import pywhatkit
import pyaudio
import random
import Movie_Recommendation_Module

def speakText(sentance):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(sentance)
    engine.runAndWait()

def getInfo():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Please Speak Now ...")
            audio = listener.listen(source)
            info = listener.recognize_google(audio)
            print(info)
            return info.lower()
    except:
        speakText("error, please retry!")
        return ""
        pass

print("[Search Movie: Movie Recommendation]")

while True:
    audio = getInfo()
    recomArr = [
        "recommend",
        "de comment",
        "se comment",
        "re comment",
        "comment"
        ]
    if "terminate" in audio:
        repSpeak = [
            "exiting program, please wait",
            "closing session, please wait",
            "ending session, closing now"
            ]
        speakText(random.choice(repSpeak))
        break
    elif "tell me about" in audio or ( "mujhe" in audio and "batao" in audio ):
        try:
            searchWiki = ""
            if "mujhe" in audio and "movie" in audio:
                searchWiki = (audio.split("mujhe "))[1].split(" movie")[0] + " movie"
            else:
                searchWiki = (audio.split("tell me about "))[1].split('\0')[0]
            info = wiki.summary(searchWiki, 1)
            speakText(info)
        except:
            speakText(random.choice(["please retry", "error, retry please!", "some error has occured, please continue by retrying"]))
            continue
        continue
    elif any(item in audio for item in recomArr) and "movie" in audio:
        try:
            recomItem = ""
            if "mujhe" in audio and "karo" in audio:
                end = " jessie" if "jessie" in audio else " jaisi"
                recomItem = (audio.split("mujhe "))[1].split(end)[0]
            else:
                recomItem = (audio.split("like "))[1].split('\0')[0]
            info = wiki.summary(recomItem + " movie", 1)
            info = (info.split("is a "))[1].split(" ")[0]
            recomItem = recomItem.title() + " (" + info + ")"
            speakText("recommendations of " + recomItem + " are")
            print(recomItem)
            Movie_Recommendation_Module.movieRecomFun(recomItem)
            print("\n")
        except:
            speakText(random.choice(["please retry", "error, retry please!", "some error has occured, please continue by retrying"]))
            continue
        continue
    elif "time" in audio:
        time = datetime.datetime.now().strftime("%I %M %p")
        speakText(random.choice(["current time is ", "sir, time is ", "time is "]) + time)
        continue
    else:
        repSpeak = [
            "please repeat, listening",
            "i didn't understand, please repeat",
            "pardon please, didn't quiet understand"
            ]
        speakText(random.choice(repSpeak))
        continue

