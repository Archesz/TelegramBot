# Librarys

import requests
import time
import json
import os
import random

# Create Bot

# Criando o bot do Telegram
class TelegramBot:
    def __init__(self):
        token = '1339507062:AAHJ_aShRUAYtMCHnWKEoV0azTx4Anz2Q4s'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    first_name = dado["message"]["from"]["first_name"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem, first_name)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem, first_name):
        respostas = ['Desculpe, eu acho que você pode ter digitado errado, poderia dizer novamente?',
                     'Certo, eu não entendi, poderia digitar novamente?', 
                     'Confira se digitou certo, por favor.', 
                     'Talvez devesse conferir sua resposta.']
                
        if eh_primeira_mensagem == True or mensagem in ('Olá'):
            return f'''Bom dia {first_name}, Sou o Arch, um Bot iniciante no momento. Como posso ajudar?.
            (digite o número):
            1 - Quem te criou?
            2 - Qual sua função?
            3 - Updates
            '''

        elif mensagem == '1':
          return '''
          Por enquanto apenas Arch.
          '''
        
        elif mensagem == '2':
          return '''
          No momento, estou apenas no berço, mas minhas funções a longo prazo são formas de ajudar estudantes.
          Pretendo tirar dúvidas simples e medianas de alunos nas matérias do ensino médio, disponibilizar livros em PDF, video aulas, monitorias e mentorias com professores na graduação, alertar de datas importantes sobre vestibulares e muito mais.
          Além do Telegram, estaremos disponíveis no Whatsapp, Facebook, Instagram, Twitter, Youtube e em nosso blog (www.archnerd.com.br).
          '''
        
        elif mensagem == '3':
          return '''
          Próximos updates:
          22/09 - Inclusão das matérias de exatas no Bot.
          26/09 - Adicionando respostas para as matérias de exatas de nível 01.
          30/09 - Adicionando livros de matemática do Ensino médio no Bot.
          02/10 - Adicionando o Bot Chloe como assistente de Química.
          04/10 - Extendendo o Bot para o Whatsapp.
          05/10 - Nova logo e Design do Arch.
          08/10 - Teste com público do Ensino Médio (230/400 alunos).
          '''

        elif mensagem == '0':
          '''
          (digite o número):
          1 - Estudo
          2 - Dicas
          3 - Mídias 
          0 - Voltar
          Você pode digitar 0 a qualquer momento.
          '''

        else:
            return f'{respostas[random.randrange(0, 3)]}'

        

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()