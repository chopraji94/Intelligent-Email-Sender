import pyttsx3
import speech_recognition as sr #Speech recognition module
import smtplib #SMTP Module

engine = pyttsx3.init('sapi5') #google api to get voices 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #inbuilt voices from pc

#speak functionality in the function speak()
def speak(audio):
    engine.setProperty('rate',180) #set the rate of speed for engine
    engine.say(audio)
    engine.runAndWait()

#Taking command from user functionality in the function takeComand()
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 #The time to response to your voice
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google engine to convert to speech to text
        print("User said: ",query)

    except Exception as e:
        #print(e)
        print("Say that again")
        return "None"
    return query

#Send Email functionality in the function sendEmail()
def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com', 587) #Using smtp module with 587 port number for message submissions by mail clients to mail servers.
     server.ehlo()
     server.starttls()
     server.login('senderEmail@gmail.com','password') #senderEmail -> from whom you want to send email
     server.sendmail('senderEmail@gmail.com', to,content)
     server.close()

#main
if __name__ == '__main__':
    speak("I am your personal assistant how may i help you")
    query = takeCommand().lower()
    if "send email" in query:
        speak("please tell the email Id")
        while True:
            query = takeCommand().lower()
            if "that is it" in query:
                break
            else:
                emailString = query.replace(" ","")
                try:
                    speak("What should i write sir")
                    content = takeCommand()
                    to = emailString
                    sendEmail(to,content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    print("Not able tosend email")
