from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Linhas de 8 a 15 são do chatbot
portuguese_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer = ListTrainer(portuguese_bot)

trainer.train([
  "Oi",
  "Oi, estou bem e como vc está?"
])

trainer.train([
  "Eae",
  "Eaê, tudo tranquilo?"
])

trainer.train([
  "to bem",
  "Precisa de ajuda?"
])

trainer.train([
  "tranquilo",
  "Precisa de ajuda?"
])

trainer.train([
  "sim",
  "Como posso te ajudar?"
])

trainer.train([
  "duvida",
  "Qual a sua dúvida?"
])

# Linhas do Flask abaixo
@app.route("/")
def home():
  return render_template("index.html")


@app.route("/get")
def get_bot_response():
  userText = request.args.get("msg")
  return str(portuguese_bot.get_response(userText))


@app.route("/hello_rota")
def hello():
  return "Testando hgnfghnfhngf"

if __name__ == "__main__":
  app.run()
  