import speech_recognition as sr
import pyttsx3
import webbrowser
import Sites
import google.generativeai as genai
import json


# Initialize the recognizer and speaker
rec= sr.Recognizer()
mic=sr.Microphone()


def listen():
    while True:
     with mic as source:
        try:
            audio=rec.listen(source)
            data=rec.recognize_google(audio)
            return data
        except:
            print("Sorry, I couldn't understand you.")
    

 
def speak(data):
    engine=pyttsx3
    engine.speak(data)

def AI(data):
    #Configuring the model
    genai.configure(api_key="AIzaSyAM2F2XCZNRLT6_c-O5203m7OE38NKVjlo")
    generative_config= {"temperature":0.9,"top_p":1,"top_k":1,"max_output_tokens":2048}
    
    #Initializing the model
    model=genai.GenerativeModel(model_name="gemini-pro",generation_config=generative_config,safety_settings=False)
    response=model.generate_content(data)
    result= response.text
    result=result.replace("*","")
    return result
    
    
    
    
    
  
if __name__=="__main__":
    speak("Jarvis developed by Kavyansh")
    while True:
        print("Listening...")
        query=listen()
        speak(query)
        if query.lower() in Sites.sites :
            speak(f"opening {query}")
            print(f"opening {query}")
            webbrowser.open(f"https://www.{query}.com")
        elif "google".lower() in query.lower():
            query_main=query.lower().split("google")[1].strip()
            speak(f"Searching {query_main} on google")
            print(f"Searching {query_main} on google")
            webbrowser.open(f"https://www.google.com/search?q={query_main}")
        elif "exit".lower() in query.lower():
            speak("quitting the program")
            print("Quitting the program")
            break
        else:
            response=AI(query)
            print(response)
            speak(response)
            
            













































































































