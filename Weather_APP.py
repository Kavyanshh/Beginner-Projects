import requests
import pyttsx3

print("DEVELOPED BY KAVYANSH SHARMA V 1.1\n********************Weather*************************")

voice=pyttsx3.init()
while True:
    response=input("Enter the area you want to search: ")

    if response.lower()=="q" or response=="quit":
        print("Exiting the program.....")
        break

    url=f"https://api.weatherapi.com/v1/current.json?key=5ae29bbb837a40688d5130834241607&q={response}"

    datas=requests.get(url).json()

    for key,values in datas.items():
        for k,v in values.items():
            if k=="condition":
                print(k,":\n",end="")
                voice.say(k)
                voice.runAndWait()
                for i,r in v.items():
                    print(i,":",r)
                    voice.say(i)
                    voice.say(v)
                    voice.runAndWait()
            else:
                print(k,":",v)
                voice.say(k)
                voice.say(v)
                voice.runAndWait()




































































