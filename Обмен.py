import  requests
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def exchenge():
    code = combobox.get()

    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2F} {code}  за 1 доллар")
            else:
                mb.showerror("Ошибкка!",f"Валюта {code}не найдена")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")


Label(text="Выберите код валюты").pack(padx=10, pady=10)
cur = ['RUB', 'EUR', 'GBP', 'JPY', 'CNY', "KZT", "UZS", "CHF", "AED", "CAD"]


combobox = ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchenge).pack(padx=10, pady=10)


window.mainloop()


'''import pprint

result = requests.get("https://open.er-api.com/v6/latest/USD")
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)

p.pprint(data)'''