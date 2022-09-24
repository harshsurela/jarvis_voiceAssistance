import wikipedia  # pip install wikipedia
import webbrowser
import os
from playsound import playsound
import getpass
from data import wishMe, speak, takeCommand, stark, mypass, get_email_info, datetime, chrome
# import data
if __name__ == "__main__":
    c = 0
    speak("WELCOME TO STARK INDUSTRIES ,  please enter username and password to get access of jarvis")
    while c != 3:
        print("Enter Your Username: ")
        name = str(input())
        # print("Enter Password: ")
        login_password = (getpass.getpass(prompt='Enter Your Password :'))

        if name == stark and login_password == mypass:
            playsound("H:\\WORKSPACE\\Python\\JARVIS\\MUSIC\\jarvis_access.mp3")
            playsound("H:\\WORKSPACE\\Python\\JARVIS\\MUSIC\\home.mp3")
            wishMe()
            while True:
                # if 1:
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=15)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    speak("opening youtube sir ")
                    webbrowser.get(chrome).open_new("youtube.com")
                    continue

                elif 'open google' in query:
                    speak("opening Google sir ")
                    webbrowser.get(chrome).open_new("google.com")
                    continue

                elif 'open stackoverflow' in query:
                    speak("opening stack overflow sir ")
                    webbrowser.get(chrome).open_new("stackoverflow.com")
                    continue

                elif 'play music' in query or 'drop my needle' in query:
                    mylist = 'H:\\WORKSPACE\\Python\\JARVIS\\MUSIC'
                    songs = os.listdir(mylist)
                    print(songs)
                    os.startfile(os.path.join(mylist, songs[2]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in query:
                    codePath = "C:\\Users\\yashu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'open telegram' in query:
                    telegram_file = "C:\\Users\\yashu\\AppData\\Roaming\\Telegram Desktop\telegram.exe"
                    os.startfile(telegram_file)

                elif 'i want to send email' in query:
                    try:
                        get_email_info()
                    except Exception as e:
                        print(e)
                        speak("Sorry Mr.harsh. I am not able to send this email")
                elif 'who is your creator' in query or 'who mad you' in query:
                    speak(
                        "Mr.Harsh Is My Boss,He Created Me ,"
                        "And I am There For Mr.Harsh 7 Days A week And 24 hours In A Day ....Thank you")

                elif 'go for sleep' in query:
                    # speak(
                    #     "Okay sir ! it's always a great pleasure to watching you work...Bye have a good day sir")
                    playsound(
                        "H:\\WORKSPACE\\Python\\JARVIS\\MUSIC\\jarvis_shut_down.mp3")
                    quit()
                elif 'on youtube' in query:
                    speak("sure sir ")
                    webbrowser.get(chrome).open_new(
                        "https://www.youtube.com/watch?v=2xWkATdMQms")
                    continue
                elif 'open map' in query:
                    speak("What you want to locate Sir ?")
                    location = takeCommand()
                    webbrowser.get(chrome).open_new(
                        f"https://www.google.com/maps/dir/home/{location}")
                elif 'google search' in query:
                    speak("What YOu want to search sir?")
                    search = takeCommand()
                    webbrowser.get(chrome).open_new(
                        f"https://www.google.com/search?q={search}")
                elif 'close browser' in query:
                    speak("okay sir")
                    os.system("taskkill /im chrome.exe /f")
                else:
                    speak("I didn't Understand That sir ...i think i need more training and knowledge sorry sir !")

        else:
            playsound("H:\\WORKSPACE\\Python\\JARVIS\\MUSIC\\jarvis_beep.mp3")
            speak("Wrong Username or password")
            c = c+1
speak("Unauthorized access......sorry you can't try for login again")
