import  requests
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)

def update_sb_label(event):
    code = sb_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def exchenge():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    sb_code = sb_combobox.get()

    if t_code and b_code and sb_code:
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")
            response.raise_for_status()
            data = response.json()
            if t_code in data["rates"]:
                exchange_rate = data["rates"][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                sb_name = cur[sb_code]
                mb.showinfo("Курс обмена", f"Курс:\n {exchange_rate:.2F} {t_name} за 1 {b_name}\n {exchange_rate:.2F} {t_name} за 1 {sb_name}")
            else:
                mb.showerror("Ошибкка!",f"Валюта {t_code}не найдена")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


cur = {
        'RUB': 'Российский рубль',
        'EUR': 'Евро',
        'GBP': 'Британский фунт стерлингов',
        'JPY': 'Японская иена',
        'CNY': 'Китайский юань',
        "KZT": 'Казахский тенге',
        "UZS": 'Узбекский сум',
        "AED": 'Дирхам ОАЭ',
        "CAD": 'Канадский доллар',
        "USD": 'Американский доллар'}

window = Tk()
window.title("Курсы обмена валют")
window.geometry("280x450")


Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)


Label(text="Целевая валюта").pack(padx=10, pady=10)
sb_combobox = ttk.Combobox(values=list(cur.keys()))
sb_combobox.pack(padx=10, pady=10)
sb_combobox.bind("<<ComboboxSelected>>", update_sb_label)
sb_label = ttk.Label()
sb_label.pack(padx=10, pady=10)


Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)
t_label = ttk.Label()
t_label.pack(padx=10, pady=10)


Button(text="Получить курс обмена", command=exchenge).pack(padx=10, pady=10)


window.mainloop()

