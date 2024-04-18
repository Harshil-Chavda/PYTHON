import win32com.client

speaker = win32com.client.Dispatch("SAPI.Spvoice")

while 1:
    print("enter the word you want to speak it out by computer")
    s = input()
    speaker.Speak(s)