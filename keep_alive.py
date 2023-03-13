from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Ante algún problema, en la ventana Shell digita: kill 1"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()