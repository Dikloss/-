import  requests
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_c_label(event):
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)



def exchenge():
    code = combobox.get()

    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                c_name = cur[code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2F} {c_name}  за 1 доллар")
            else:
                mb.showerror("Ошибкка!",f"Валюта {code}не найдена")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


cur = {
        'RUB': 'Российский рубль',
        'EUR': 'Евро',
        'GBP': 'Британский фунт стерлингов',
        'JPY': 'Японская иена',
        'CNY': 'Китфйский юань',
        "KZT": 'Казахский тенге',
        "UZS": 'Узбекский сум',
        "CHF": 'Швейцарский франк',
        "AED": 'Дирхам ОАЭ',
        "CAD": 'Канадский доллар' }

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")


Label(text="Выберите код валюты").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchenge).pack(padx=10, pady=10)


window.mainloop()


'''import pprint

result = requests.get("https://open.er-api.com/v6/latest/USD")
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)

p.pprint(data)'''