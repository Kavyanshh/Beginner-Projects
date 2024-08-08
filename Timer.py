from playsound import playsound
import time

CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"
def alarm(seconds):
    time_elapsed=0
    print(CLEAR)

    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1
        
        time_left=seconds-time_elapsed
        minutes_left= time_left // 60
        seconds_left=time_left % 60
        print(CLEAR_AND_RETURN+f"{minutes_left:02d}:{seconds_left:02d}")
        
        if time_left==0:
            print(CLEAR_AND_RETURN+"Time's up!")
            playsound("mixkit-warning-alarm-buzzer-991.wav")

sec=int(input("Enter the no of seconds you want to set timer for: "))
alarm(sec)




















