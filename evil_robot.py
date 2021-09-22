
import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener= sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty("voices")

rate= engine.getProperty("rate")
engine.setProperty('rate',145)
engine.setProperty("voice",voices[0].id)
engine.say("Hey I am Evil Robot, what can I do for you?")
engine.say("I am here to help?")

engine.runAndWait()

# def talk(text):

#     engine.say(text)
#     engine.runAndWait()


# def take_command():
#     try:
#         with sr.Microphone() as source:
#             voice= listener.listen(source)
#             command= listener.recognize_google(voice).lower()
#             if "evil robot" in command:
#                 command= command.replace("Evil Robot","")
#                 talk(command)
#                 print(command)

#     except:
#         pass
#     return command


# def run_evilRobot():
#     command= take_command()
#     if "play" in command:
#         command= command.replace("Evil Robot","")
#         command= command.replace("play","")
#         command=command.replace("can you play","")
#         song = command.replace("can you play", "")
#         song=command.replace("play","")
#         talk('I will play the song you asked for, sir!. I will start playing'+ song +"and I will search the song lyrics for you!")
#         pywhatkit.playonyt(song)
#         pywhatkit.search(song+" lyrics")
#     elif "time" in command:
#         time  = datetime.datetime.now().strftime("%H:%M")
#         talk("It is now "+time+" sir")
#         print("It is now "+time+" sir")
#     elif "who is " or "what is" in command:
#         person = command.replace("who is ",'')
#         info = wikipedia.summary(person,1)
#         print("Quoting form the wikipedia page "+ info)
#         talk("Quoting form the wikipedia page "+ info)

        
# while True:
#     run_evilRobot()