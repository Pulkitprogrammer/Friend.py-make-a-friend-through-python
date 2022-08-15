import pyttsx3 #pip install pyttsx3
while True:
    friend = pyttsx3.init()
    speech = (str(input("Say something : ")))
    friend.say(speech)
    friend.runAndWait()