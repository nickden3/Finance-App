#! /usr/bin/python3


'''
Created on Dec 21, 2017

@author: nick
'''
from binance import binance as binance
import requests
import time
import json
import hmac
import alertMe
import schedule
from scipy import stats
import plotly
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import numpy as np
from plotly.graph_objs import *
import time
import datetime



plotly.tools.set_credentials_file(username='nickden3', api_key='EdObcsandhkICDPyYh8O', stream_ids = ['ehrzm09b5j', 'bqk6tb1x9a', 'ojqryggrhb', 'o8n7wp1ode', '2pautch4fw'] )
stream_tokens = tls.get_credentials_file()['stream_ids']
stream_id1 = dict(token=stream_tokens[0], maxpoints=500)
stream_id2 = dict(token=stream_tokens[1], maxpoints=500)
stream_id3 = dict(token=stream_tokens[2], maxpoints=500)
stream_id4 = dict(token=stream_tokens[3], maxpoints=500)
stream_id5 = dict(token=stream_tokens[4], maxpoints=500)



XRP = go.Scatter(x=[], y=[], stream=stream_id1, name='XRP', yaxis='Price (USD)', xaxis = 'Time')
BCC = go.Scatter(x=[], y=[], stream=stream_id2, name='BCC', yaxis='Price (USD)', xaxis = 'Time')
LTC = go.Scatter(x=[], y=[], stream=stream_id3, name='LTC', yaxis='Price (USD)', xaxis = 'Time')
ETH = go.Scatter(x=[], y=[], stream=stream_id4, name='ETH', yaxis='Price (USD)', xaxis = 'Time')
btc = go.Scatter(x=[], y=[], stream=stream_id5, name='BTC', yaxis='Price (USD)', xaxis = 'Time')
data = [ XRP, BCC, LTC, ETH,btc]
layout = go.Layout(
    title='Crypto Coin Comparisons',
    yaxis=dict(
        title='Price (USD)'
    )  
)


fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='multple-trace-axes-streaming', sharing = 'public')

s_1 = py.Stream(stream_id=stream_tokens[0])
s_2 = py.Stream(stream_id=stream_tokens[1])
s_3 = py.Stream(stream_id=stream_tokens[2])
s_4 = py.Stream(stream_id=stream_tokens[3])
s_5 = py.Stream(stream_id=stream_tokens[4])

s_1.open()
s_2.open()
s_3.open()
s_4.open()
s_5.open()

       
BTC = binance('BTCUSDT') 
XRPBTC = binance('XRPBTC')
ETHBTC = binance('ETHBTC')
BCCBTC = binance('BCCBTC')
LTCBTC = binance('LTCBTC')

print('Working...')


#schedule.every(3).seconds.do(test.trackTrend)
#schedule.every(5).minutes.do(test.getHourlyUpdate)
#schedule.every(24).hours.do(test.get24HrStats)

while True:
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(x)
    #print(LTCBTC.getPrice())
    btcPrice = float(BTC.getPrice())
    s_1.heartbeat()
    s_2.heartbeat()
    s_3.heartbeat()
    s_4.heartbeat()
    s_5.heartbeat() 
    
    s_1.write(dict(x=x,y=float(XRPBTC.getPrice()) * btcPrice))
    s_2.write(dict(x=x,y=float(BCCBTC.getPrice())* btcPrice))
    s_3.write(dict(x=x,y=float(LTCBTC.getPrice())* btcPrice))
    s_4.write(dict(x=x,y=float(ETHBTC.getPrice())* btcPrice))
    s_5.write(dict(x=x,y=btcPrice))
   
  
    
    time.sleep(5)

s_1.close()
s_2.close()
s_3.close()
s_4.close()       
s_5.close() 
