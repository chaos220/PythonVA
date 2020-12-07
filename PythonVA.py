# PythonVA App
import wx
import wolframalpha
import wikipedia

app_id = "2KX35Q-66JJ87KHEX"
client = wolframalpha.Client(app_id)

# lang = "en" // lang = "fr" 
# wikipedia.set_lang(lang)

while(True):
    inp = input("Q: ")
    try:
        # wolframalpha
        res = client.query(inp)
        answer = next(res.results).text
        print(answer)

    except: 
        # wikipedia 
        print(wikipedia.summary(inp, sentences=3))


