# PythonVA App
import wx
import wolframalpha
import wikipedia
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
engine.say("Welcome")
engine.runAndWait()


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | 
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDA")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
            label="Hello I am PyDA the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        engine = pyttsx3.init()


    def OnEnter(self, event):
        inp = self.txt.GetValue()
        inp = inp.lower()

        if(inp == ""):
            r = sr.Recognizer()
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
                self.txt.SetValue(r.recognize_google(audio))

                # self.txt.setValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google speech recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google speech recognition service; {0}".format(e))

        else:

            try:
                # wolframalpha
                
                app_id = "2KX35Q-66JJ87KHEX"
                client = wolframalpha.Client(app_id)
                res = client.query(inp)
                answer = next(res.results).text
                print(answer)
                engine.say("The answer is " + answer)
                engine.runAndWait()

            except: 
                # wikipedia 
                answer = wikipedia.summary(inp, sentences=3)
                print(answer)
                engine.say("The answer is " + answer)
                engine.runAndWait()


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()


