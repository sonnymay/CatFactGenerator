import requests
from tkinter import Tk, Label

def get_cat_fact():
    response = requests.get('https://cat-fact.herokuapp.com/facts/random')
    fact = response.json()
    return fact['text']

def show_fact():
    fact = get_cat_fact()
    window = Tk()
    window.title('Random Cat Fact')
    lbl_fact = Label(window, text=fact, wraplength=400)
    lbl_fact.pack()
    window.mainloop()

show_fact()
