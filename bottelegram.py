import telebot
import requests
import re

CHAVE_API = ""
URL_API = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

bot = telebot.TeleBot(CHAVE_API)

def frequenciaPorNome(nome):
    periodos = {}
    req = requests.get(URL_API.format(nome=nome)).json()
    for dados in req[0]['res']:
        periodos[dados['periodo']] = dados['frequencia']
        periodo = max(periodos, key=periodos.get)
        quantidade = periodos[periodo]
    faixa = [ano for ano in re.findall('\d+', periodo)]
    msg = 'Seu nome foi mais comum entre os anos {} e {} com uma frequencia de {} vezes'.format(faixa[0], faixa[1], quantidade)
    return msg

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    nome = mensagem.text
    msg = frequenciaPorNome(nome)
    bot.reply_to(mensagem, msg)

bot.polling()