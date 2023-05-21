import time
import docker
import telegram
import telebot
from telegram.ext import (Updater, CommandHandler)

token = "5994239232:AAFrJATkMA2vLDztaOMTlYVWnPK6DUt5RWM"

id="1210950752"

bot = telegram.Bot(token)


cliente = docker.from_env()

def comprobar(contenedor):
    try:
        contenedor = cliente.containers.get(contenedor)

        if contenedor.status == 'running':
            mensaje = f"{contenedor.name} está funcionando"
            bot.send_message(text=mensaje, chat_id = id)
        else:
            mensaje = f"{contenedor.name} no está funcionando"
            bot.send_message(text=mensaje, chat_id = id)
    except docker.errors.NotFound:
        print(f"{contenedor.name} no se encuentra")

comprobar("b8b4379e0639")
    
while True:
    comprobar("b8b4379e0639")
    