import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine=pyttsx3.init()

def speak(audio):
      engine.say(audio)
      engine.runAndWait()

         

#speak("Hi i am Vinaykumar your virtual assistant")

def time():
     Time=datetime.datetime.now().strftime("%I:%M:%S")
     speak("The current time is ")
     speak(Time)

#time()
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("current date is")
    speak(date)
    speak(month)
    speak(year)

#date()
def wishme():
    speak("Welcome back sir!")
    #time()
    #date()
    hour=datetime.datetime.now().hour
    if hour>=6 and  hour<=12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir!")
    elif hour>=18 and hour<=24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("vinaykumar at your service. please tell me how can i help you?")

#wishme()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
           print("Recongnizing...")
           query=r.recognize_google(audio,language='en-in')
           print(query)

    except Exception as e:
          print(e)
          speak("say that thing again please...")
          return None
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('vishal100901@gmail.com','9860045813')
    server.sendmail('vishal100901@gmail.com',to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save(r"C:\Users\Vishal Dhongade\Pictures\ss.png")


def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

#y=takecommand()
#speak(y)
wishme()
     

if __name__ == "__main__":

    while True:
        query=str(takecommand()).lower()
        if 'time'in query:
             time()
 
        elif'date'in query:
             date()
        
        elif 'wikipedia'in query:
            speak("searching......")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'search in chrome'in query:
            speak("What should i search?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search=takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1 ")

        elif 'remember that' in query:
            speak("what should i remember?")
            data=takecommand()
            speak("you said me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("you said me to remember that"+remember.read())


        
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to='vishalilu1009@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent sucessfully")
            except Exception as e:
                print(e)
                speak("unable to send the email")

        elif 'play song' in query:
            song_dir=r'C:\Users\Vishal Dhongade\Music'
            songs=os.listdir()
            os.startfile(os.path.join(song_dir,songs[0]))



        elif 'offline' in query:
             quit()  
        
        elif 'screenshot'in query:
            screenshot()
            speak("screenshot has taken successfully")

        elif 'cpu'in query:
            cpu()

        elif 'joke'in query:
            jokes()

        




