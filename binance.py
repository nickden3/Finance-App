'''
Created on Dec 18, 2017
Fucking Prick!!!
@author: nick
'''
import requests

import alertMe
from scipy import stats
import time





header = {'X-MBX-APIKEY' : 'ToMFC8dPRS7bH4dXJ5HIT9eu60SwbhxuNqUD9dkQgZe4oOIigVb4fAcCVmockt2N'}


class binance(object):

    def __init__(self,ticker):
        self.trend = []
        self.ticker = ticker
        self.percentGain = 0
        self.alertedAt = 0
        self.alerted = False
        self.timeStamps = []
        self.getPrice()
        self.trackTrend()
        

    def alertText(self, message):
        
        self.alert = alertMe.mail(message)
        
    def trackTrend(self):
        if (len(self.trend) > 40):
            self.trend = self.trend[20:]
            self.timeStamps = self.timeStamps[20:]
        elif(len(self.trend) > 1):
            self.trend.append(float(self.getPrice()['price'] ) * 10000)
            self.timeStamps.append(int(time.time()))
            x = stats.linregress(self.timeStamps,self.trend)
            if(x.slope > .0001 and self.trend[-1] > self.peak24Hr and not self.alerted):
                self.percentGain = (self.trend[-1] - self.peak24Hr) / self.peak24Hr       
                self.alertText('XRP is trending up. Gain: %f%' %(self.percentGain))
                self.alerted = True
                self.trend = []
                self.timeStamps =[]
        
    def getHourlyUpdate(self):
        if(time.localtime(time.time()).tm_hour > 7 and time.localtime(time.time()).tm_hour < 23):
            self.xrpBtc=requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BCCETH').json()
            self.btcUsd=requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT').json()
            self.alertText('1 XRP = $%f' %(float(self.xrpBtc['price']) * float(self.btcUsd['price'])))
            
        
    def get24HrStats(self):
        self.stats24Hr = requests.get('https://api.binance.com/api/v1/ticker/24hr?symbol=XRPBTC').json()
        self.peak24Hr = float(self.stats24Hr['highPrice'])
        return self.stats24Hr
        
    def getPrice(self):
        self.xrpBtc=requests.get('https://api.binance.com/api/v3/ticker/price?symbol=%s' %(self.ticker)).json()
        return self.xrpBtc['price']
    
    def plot(self):
        
        return

