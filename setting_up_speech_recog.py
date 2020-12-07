import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

while True: 
    r = sr.Recognizer()

    print(sr.Microphone.list_microphone_names())

    with sr.Microphone() as source:
        engine.say("Say something")
        engine.runAndWait()
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        engine.say("You said ")
        engine.runAndWait()
        engine.say(text)
        engine.runAndWait()

        # self.txt.setValue(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google speech recognition service; {0}".format(e))
