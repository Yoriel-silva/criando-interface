from tkinter import *#importa a biblioteca tkinter

import requests #importa a biblioteca requests
import json #importa a biblioteca json

#comando que será executado
def cotaçao():
    cotaçoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotaçoes = cotaçoes.json()
    cotaçoes_dolar = cotaçoes['USDBRL']['bid']

    texto = (f'O valor do dolar é {cotaçoes_dolar} reais')#define uma variavel

    texto_orientaçã02['text'] = texto #coloca a variavel dentro do texto quando o comando roda

janela = Tk() #criar janela
janela.title('Tela De App') # titulo da janela

texto_orientaçã0 = Label(janela, text = 'Clique aqui')#cria um texto
texto_orientaçã0.grid(column=0,row=0)#diz a posição do texto na janela

botao = Button(janela, text='Ativar', command = cotaçao)#cria um botão e define qual comando ele vai rodar
botao.grid(column=0,row=1)#diz a posição do butão na janela

texto_orientaçã02 = Label(janela, text = '')#cria um texto
texto_orientaçã02.grid(column=0,row=2)#diz a posição do texto na janela

janela.mainloop() #mantém a janela