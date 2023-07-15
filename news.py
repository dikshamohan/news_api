import requests
import tkinter as tk

def getNews():
    api_key = "32a339b76d364b72a039fc6e62958554"
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey="+api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = " "

    for article in articles:
        my_articles.append(article["title"])


    for i in range(10):                   # for top 10 news headlines
        my_news = my_news + str(i+1)+ " . " + my_articles[i] + "\n" " \n" 


    label.config(text = my_news)


canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font = 24, text ="Reload",command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left", bg="pink")
label.pack(pady = 20)

getNews()

canvas.mainloop()