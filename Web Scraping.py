import requests
from bs4 import BeautifulSoup as bs
from tkinter import *
from tkinter import messagebox
import random

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
root = Tk()
root.geometry("1000x800")
d1 = {"Sunny": ["“Ô, Sunlight! The most precious gold to be found on Earth.”", """“Keep your face always
            toward the sunshine and shadows will fall behind you.”""", """“If you spend your whole life
            waiting for the storm, you'll never enjoy the sunshine.”""", """“If you want to see the sunshine,
            you have to weather the storm.”"""""""“Clouds in the sky very much resembles the thoughts in our minds!
               Both changes perpetually from one second to another!”"""]
    , "Haze": ["“It is the dim haze of mystery that adds enchantment to pursuit.”", """“The farther reason looks
            the greater is the haze in which it loses itself ”""", """“Than smoke and mist who better could appraise
The kindred spirit of an inner haze?”"""],
      "Cloudy": [""""“Clouds in the sky very much resembles the thoughts in our minds!
               Both changes perpetually from one second to another!”""",
                 "“Never lose hope. The darkest clouds precede the loveliest rain!”",
                 "“No dark cloud can forever prevent the sun from shining!”"
                 ], "rando": ["“Bad weather always looks worse through a window.” ",
                              "“You are the sky. Everything else – it’s just the weather.”",
     """“Clouds in the sky very much resembles the thoughts in our minds! Both changes perpetually from one second to another!”"""]}
def showMsg():
    global T
    T = Text(root, height=15, width=50, font=("Agency FB", 20))

    def get_weather_data(url):
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE
        html = session.get(url)

        soup = bs(html.text, "html.parser")
        result = {}
        result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
        result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
        result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
        result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
        result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
        result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
        result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
        return result

    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather/" + w2.get()
    data = get_weather_data(URL)
    T.insert(END, "Weather for:" + data["region"] + "\n")
    T.insert(END, "Now:" + data["dayhour"] + "\n")
    T.insert(END, f"Temperature now: {data['temp_now']}°C" + "\n")
    T.insert(END, "Description:" + data['weather_now'] + "\n")
    T.insert(END, "Precipitation:" + data["precipitation"] + "\n")
    T.insert(END, "Humidity:" + data["humidity"] + "\n")
    T.insert(END, "Wind:" + data["wind"] + "\n" + "\n")
    for i in d1.keys():

        if i == data['weather_now']:
            T.insert(END, (random.choice(d1[i])) + "\n" + "\n")
            break
    else:
        T.insert(END, (random.choice(d1["rando"])) + "\n" + "\n")
    T.pack(side=TOP)
def res():
    T.destroy()
def game(p):
    global root2
    list_1 = ["Rock", "Paper", "Scissors"]
    w = random.choice(list_1)

    if p == "Rock":
        if w == "Rock":
            messagebox.showinfo("Result", "Its a Draw, close one!!")
        elif w == "Paper":
            messagebox.showinfo("Result", "You lost, good luck next time!!")
        else:
            messagebox.showinfo("Result", "You Won, Congrats!!!")
    if p == "Paper":
        if w == "Rock":
            messagebox.showinfo("Result", "You Won, Congrats!!!")
        elif w == "Paper":
            messagebox.showinfo("Result", "Its a Draw, close one!!")
        else:
            messagebox.showinfo("Result", "You lost, good luck next time!!")
    if p == "Scissors":
        if w == "Rock":
            messagebox.showinfo("Result", "You lost, good luck next time!!")
        elif w == "Paper":
            messagebox.showinfo("Result", "You Won, Congrats!!!")
        else:
            messagebox.showinfo("Result", "Its a Draw, close one!!")
def rps():
    global root2
    root2 = Tk()
    root2.geometry("550x400")
    k2 = Label(root2, text="Rock Paper Scissor", font=("Agency FB", 35))
    w6 = Button(root2, text="Rock", font=("corbel", 10), width=17, height=5, command=lambda: game(w6.cget("text")))
    w7 = Button(root2, text="Scissors", font=("corbel", 10), width=17, height=5, command=lambda: game(w7.cget("text")))
    w8 = Button(root2, text="Paper", font=("corbel", 10), width=17, height=5, command=lambda: game(w8.cget("text")))
    k2.grid(row=0, column=0, columnspan=3)
    w6.grid(row=1, column=0, pady=40, padx=30)
    w7.grid(row=1, column=1, pady=40, padx=30)
    w8.grid(row=1, column=2, pady=40, padx=30)
    root2.resizable(False, False)
    root2.mainloop()
w1 = Label(root, text="Weather", font=("Agency FB", 35))
w2 = Entry(root, width=22, font=("Agency FB", 28))
w5 = Button(root, text="Play the game", font=("corbel"), command=rps)
w4 = Button(root, text="Reset", font=("corbel"), command=res)
w3 = Button(root, text="Find", font=("corbel"), command=showMsg)
w1.pack(pady=20)
w2.pack()
w3.pack()
w4.pack()
w5.pack()
root.resizable(False, False)
root.mainloop()