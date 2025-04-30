from flask import Flask, request
from telegram import Bot
from telegram.ext import CommandHandler, Updater

app = Flask(__name__)

# Defina o token do seu bot
TOKEN = "7841443022:AAEOKPA4b0h5ZVMcvkl7zLHsgO_C45U07ZM"
bot = Bot(token=TOKEN)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()  # Recebe os dados da requisição

    chat_id = data['chat_id']
    message = data['message']

    bot.send_message(chat_id=chat_id, text=message)  # Envia a mensagem

    return {'status': 'success'}

if __name__ == "__main__":
    app.run(port=5000)  # A API vai rodar na porta 5000

