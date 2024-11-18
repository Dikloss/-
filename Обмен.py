import  requests
import json
from tkinter import *
from tkinter import messagebox as mb



window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")


Label(text="ВВедите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=excheng).pack(padx=10, pady=10)


window.mainloop()


'''import pprint

result = requests.get("https://open.er-api.com/v6/latest/USD")
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)

p.pprint(data)'''