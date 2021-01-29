import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

#setting voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):

    engine.say(text)
    engine.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)


    except:
        pass
    return command


talk('hey boss, how you doing?')

def run_alexa():
    command = take_command()
    #print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Now the time is' +time)

    elif 'who is    ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'how are you' in command:
        talk('I am good. Thanks for asking. What can I do for you?')

    elif 'love' in command:
        talk('That is so sweet, but I am quite shy!')

    elif 'you date' in command:
        print('So sweet of you, but I need to ask ashiq')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Sorry did not get that. Can you repeat it again?')




while True:
    run_alexa()