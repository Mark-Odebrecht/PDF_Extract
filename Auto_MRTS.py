from pandas_datareader import data as pdr
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import yfinance as yf
yf.pdr_override()
from datetime import timedelta
import plotly.express as px
import plotly.graph_objects as go
import os
from zipfile import ZipFile
import glob


# Date formating

date = dt.date.today()
year = str(date.year-2000)

if date.month < 10:
  month = str('0')+str(date.month)
else:
  month = str(date.day)

if date.day < 10:
  day = str('0')+str(date.day)
else:
  day = str(date.day)

str_time=str(year+month+day)
# print (str_time)

os.mkdir(str_time)

tickers = ["ABCB4", "ALPA4", "ABEV3", "ANIM3", "ARZZ3", 
           "AZUL4", "B3SA3", "BRSR6", "BBSE3", "BRML3",
           "BRPR3", "BBDC3", "BBDC4", "BRAP4", "BBAS3",
           "BRKM5", "BRFS3", "BPAC11", "CAML3", "CRFB3", 
           "CCRO3", "CMIG3", "CMIG4", "CIEL3", "CGAS5", 
           "CSMG3", "CPLE6", "CSAN3", "CPFE3", "CVCB3", 
           "CYRE3", "DIRR3", "ECOR3", "ELET3", 
           "ELET6", "EMBR3", "ENBR3", "ENEV3", "EGIE3", 
           "EQTL3", "EVEN3", "EZTC3", "FESA4", "FLRY3", 
           "GFSA3", "GGBR4", "GOAU4", "GOLL4", "GRND3", 
           "GUAR3", "HAPV3", "HBOR3", "HYPE3", "PARD3", 
           "MEAL3", "MYPK3", "IRBR3", "ITSA4", "ITUB3", 
           "ITUB4", "JBSS3", "KLBN11", "LIGT3", "RENT3", 
           "AMAR3", "LREN3", "MDIA3", "MGLU3", "POMO4", 
           "MRFG3", "LEVE3", "BEEF3", "MOVI3", "MRVE3", 
           "MULT3", "ODPV3", "PETR3", "PETR4", "PRIO3", 
           "PSSA3", "PTBL3", "QUAL3", "RADL3", "RAPT4", 
           "RAIL3", "SBSP3", "SAPR11", "SANB11", "STBP3", 
           "SMTO3", "SEER3", "CSNA3", "SLCE3", "SULA11", 
           "SUZB3", "TAEE11", "TGMA3", "TOTS3", "TRPL4", 
           "TUPY3", "UGPA3", "UNIP6", "USIM5", "VALE3", 
           "VLID3", "VULC3", "WEGE3", "WIZS3", "VIVA3", 
           "CEAB3", "YDUQ3", "COGN3", "BIOM3", "BPAN4", 
           "FHER3", "FRAS3", "FRTA3", "LPSB3", "AESB3",
           "LOGN3", "MILS3", "OFSA3", "OIBR3", "PFRM3", 
           "ROMI3", "PMAM3", "RSID3", "SCAR3", "SGPS3", 
           "SHOW3", "SLED3", "TCSA3", "TECN3", "TELB4", 
           "TEND3", "TPIS3", "TRIS3", "VIVR3", "VIVT3", 
           "NTCO3", "PCAR3"]



for ticker in tickers:
    ticker = ticker+'.SA'
    PATH = str_time
    TOTAL_DAYS = 560
    end = dt.datetime.now() # get current time
    d1 = end - dt.timedelta(days=TOTAL_DAYS)
    start = d1.strftime('%Y-%m-%d') # start date

    df = pdr.DataReader(ticker, start= start, end= end)[['Close']].reset_index()
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    df.sort_values('Date', inplace=True)

  # df = get_symbols(tickers, start, end)

    df=df.set_index(['Date'])

    def get_sma(prices, rate):
        return prices.rolling(rate).mean()

    def get_bollinger_bands(prices, rate=20):
        sma = get_sma(prices, rate)
        std = prices.rolling(rate).std()
        b_up = sma + std * 2 # Calculate top band
        b_down = sma - std * 2 # Calculate bottom band
        return b_up, b_down

    df['b_up'], df['b_down'] = get_bollinger_bands(df['Close'])

    # function to define SMA
    def SMA (data, period=30, column = 'Close'):
      return data[column].rolling(window=period).mean()

    # build and show the data set
    df['SMA20'] = SMA(df, 20)
    df['SMA50'] = SMA(df, 50)
    df['SMA100'] = SMA(df, 100)
    df['SMA200'] = SMA(df, 200)
    df['Simple_Returns'] = df.pct_change(1)['Close']
    df['Log_Returns'] = np.log(1+df['Simple_Returns'])
    df['Ratios'] = df['Close'] / df['SMA200']

    df['price_change'] = df['Close'].pct_change()
    df['upmove'] = df['price_change'].apply(lambda x: x if x > 0 else 0)
    df['downmove'] = df['price_change'].apply(lambda x: abs(x) if x < 0 else 0)
    df['avgup'] = df['upmove'].ewm(span=19).mean()
    df['avgdown'] = df['downmove'].ewm(span=19).mean()

    df = df.dropna()

    df['RS'] = df['avgup']/df['avgdown']
    df['RSI'] = df['RS'].apply(lambda x: 100-(100/(x+1)))

    percentiles = [3, 15, 20, 50, 80, 85, 97]

    # removing any NaN values from Ratios and storing them into a new column called ratios
    ratios = df['Ratios'].dropna()

    # geting the values of the percentiles
    percentile_values = np.percentile(ratios, percentiles)

    sell = percentile_values[6] # 99th perdentile threshold were I want to sell
    buy = percentile_values[0] # 1st percentile threshold were I wnat to buy

    # Creating column 'Positions' to add -1 where the ratio is greater the 85th percentile (sell) and NaN otherwise
    df['Positions'] = np.where(df['Ratios'] > sell, -1, np.nan)

    # Adding 1 where the ratio is less than the 15th percentile (buy) and put the current value otherwise
    df['Positions'] = np.where(df['Ratios'] < buy, 1, df['Positions'])

    # Bollinger band signals

    df['P_bol'] = np.where(df['Close']<df['b_down'], 1, np.nan)

    df['P_bol'] = np.where(df['Close']>df['b_up'], -1, df['P_bol'])

    df['Buy'] = np.where(df.Positions == 1, df['Close'], np.nan)
    df['Sell'] = np.where(df.Positions == -1, df['Close'], np.nan)
    df['Bollinger_buy'] = np.where(df.P_bol == 1, df['Close'], np.nan)
    df['Bollinger_sell'] = np.where(df.P_bol == -1, df['Close'], np.nan)


    plt.figure(figsize=(24, 12))
    plt.xlabel('Date')
    plt.xticks(fontsize=16)
    plt.ylabel('Close Price')
     
    ax1 = plt.subplot(211)
    ax1.set_title('Close Price w/ Buy & Sell Signals for '+ticker+' on '+day+'/'+month+'/'+year)
    ax1.plot(df.Close, alpha = 0.7, label = 'Close', color='gray')
    ax1.plot(df.b_up, alpha=0.5, label = 'Bollinger up', color='darkorange')
    ax1.plot(df.b_down, alpha=0.5, label = 'Bollinger up', color='darkorange')
    ax1.plot(df.SMA20, alpha = 0.5, label = 'SMA20', color='green')
    ax1.plot(df.SMA50, alpha = 0.5, label = 'SMA50', color='red')
    ax1.plot(df.SMA200, alpha = 0.5, label = 'SMA200', color='blue')
    ax1.scatter(df.index, df.Buy, color = 'yellow', label = 'Buy Signal',
    marker = 'o', alpha = 1, s=300)
    ax1.scatter(df.index, df.Sell, color = 'red', label = 'Sell Signal', 
    marker = 'o', alpha = 1, s=300)
    ax1.scatter(df.index, df.Bollinger_buy, color = 'cornflowerblue', 
    label = 'Bollinger buy signal', marker = '2', alpha = 1, s=200)
    ax1.scatter(df.index, df.Bollinger_sell, color = 'lime', 
    abel = 'Bollinger sell signal', marker = '1', alpha = 1, s=200)
    # ax1.legend()

    ax2 = plt.subplot(212, sharex=ax1)
    ax2.set_title('RSI')
    ax2.plot(df.index, df['RSI'], color = 'limegreen')
    ax2.axhline(30, linestyle='--', alpha=0.5, color='gray')
    ax2.axhline(70, linestyle='--', alpha=0.5, color='gray')
    ax2.axhline(50, alpha=0.7, color='dodgerblue')
    ax2.grid(False)

    plt.savefig(PATH+ticker+' - '+str_time+'.png')


with ZipFile(str_time+'.zip', 'w') as f:
    for file in glob.glob(PATH+'/*.png'):
        f.write(file)

# files.download (str_time+'.zip')