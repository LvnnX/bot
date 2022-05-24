from email import message
import discord
from random import *
import yfinance as yf
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.graph_objs as go
import kaleido
token = 'OTc4NDY4OTQyMjg2ODQ4MDUx.Gaka8M.szNKKez_fFxDrur4KZw3xHDcbW3kHpmCN0iWgo'

client = discord.Client()


@client.event
async def on_ready():
    print('Login Success {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    #Ruang turu 978448938430509067
    #Test serv 952848717952741386
    hai = ['hello','hai','hi','halo','ngikngok']
    sedih = ['sedih','sad','mengsad','mengsedih']
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == 'ping':
        await message.channel.send('pong! {0}ms'.format(round(client.latency,1)))
        return

    if user_message.lower() in hai:
        choice = ['hello_donkey.jpg','hello_donkey2.jpg','hello_ngikngok.jpg']
        await message.channel.send(f'Hai bang {username}')
        await message.channel.send(file=discord.File(choice[randint(0,len(choice)-1)]))
        return

    if user_message.lower() in sedih:
        rand = randint(0,1)
        if(rand==1):
            await message.channel.send('Janji gak nangis?')
        choice = ['sedih.jpeg','sad_donkey1.gif','sad_donkey2.gif','sad_donkey3.jpg','sad_donkey4.jpg']
        pil = randint(0,len(choice)-1)
        await message.channel.send(file=discord.File(choice[pil]))
        return

    if user_message.lower() == 'kamu siapa?':
        choice = ['hello_ngikngok.jpg','ngikngok.png','sad_donkey4.jpg']
        await message.channel.send('Akulah ngikngok!')
        await message.channel.send(file=discord.File(choice[randint(0,len(choice)-1)]))
        return

    if user_message == '<@978468942286848051>':
        choice = ['hello_ngikngok.jpg','ngikngok.png','sad_donkey4.jpg']
        await message.channel.send('Iya ngikngok?')
        await message.channel.send(file=discord.File(choice[randint(0,len(choice)-1)]))
        await message.channel.send('Menu ngikngok\n>> Hello\n>> Sedih\n>> Kamu Siapa?\n>> @Ngikngok\n>> Info\n')
        return

    if user_message.lower() == 'info':
        kurs = 14650
        data = yf.download(tickers='LUNA1-USD',period ='1d', interval='15m')
        data.reset_index(inplace=True)
        tot = data['Datetime'].count()-20
        datafix = data[tot::]
        stock = yf.Ticker("LUNA1-USD")
        price = stock.info['regularMarketPrice']
        price = price * kurs
        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=datafix['Datetime'],
                        open=datafix['Open']*kurs,
                        high=datafix['High']*kurs,
                        low=datafix['Low']*kurs,
                        close=datafix['Close']*kurs, name = 'market data'))
        fig.update_layout(
            title='Luna live share price (UST time)',
            yaxis_title='Harga (Rp)')
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        fig.write_image("dia.png")
        await message.channel.send(f'Harga Luna sekarang {datetime.now().strftime("%D  %H:%M")}\n Rp.{price}')
        await message.channel.send(file=discord.File("dia.png"))
        return

client.run(token)
