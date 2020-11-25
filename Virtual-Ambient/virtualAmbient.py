from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot',methods=['POST'])

def bot():
    incoming_message = request.values.get('Body','').lower()
    response = MessagingResponse()
    mensage = response.message()
    responded = False
    f = open("infos.txt","a")

    if "cadastrar" in incoming_message:
        mensage.body('Bem vindo ao BOT do Fanto \nPor Favor digite seu nome na seguinte estrutura: \n\nnome:Felipe de Almeida')
        responded = True
    if "nome:" in incoming_message:
        text = incoming_message.split(":")
        name = text[1].title()
        f.write(name)
        mensage.body('Seu nome é {} \n\nAgora digite sua data de nascimento na seguinte estrutura: \n\ndata:26/04/1996'.format(name))
    if "data:" in incoming_message:
        text = incoming_message.split(":")
        age = text[1].split("/")
        day = age[0]
        month = age[1]
        year = age[2]
        age_calc = 2020 - int(year)
        f.write(str(age_calc))
        f.write(day)
        f.write(month)
        f.write(year)
        mensage.body('Sua idade é {} e você nasceu dia {} do mês {} de {}\n\nAgora digite seu e-mail para entrarmos em contato na seguinte estrutura:\n\nemail:coloque seu email aqui'.format(age_calc,day,month,year))
    if "email" in incoming_message:
        text = incoming_message.split(":")
        email = text[1]
        f.write(email)
        mensage.body('Seu E-mail é {} Muito Obrigado por entrar em contato'.format(email))
    return str(response)

if __name__ == '__main__':
    app.run()