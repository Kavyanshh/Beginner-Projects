import pyttsx3


start=pyttsx3.init()

start.say("This voice typing is developed by Kavyansh Version 1.2")
start.runAndWait()
while True:
    voice=input("Enter your text: ")
    if voice=="q":
        start.say("Quitting bye")
        start.runAndWait()
        break
    start.say(voice)
    start.runAndWait()




    















