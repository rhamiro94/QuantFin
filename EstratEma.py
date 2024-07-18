import pandas as pd
tickers = ["GGAL", "BMA", "BBAR", "PAM", "TEO", "CRESY","YPF","EDN","TGS","TX","TS","SUPV","IRS","CEPU"]
for ticker in tickers:
    data = yf.download(ticker, period='10y')
    ret=data["Adj Close"].to_frame()
    ret.columns= ['AdjClose']
    ret['Yield']=(ret['AdjClose']/ret['AdjClose'].shift(1)-1)*100

ret.dropna(axis=0, how='any', inplace=True)

import pandas as pd
tickers = ["GGAL", "BMA", "BBAR", "PAM", "TEO", "CRESY","YPF","EDN","TGS","TX","TS","SUPV","IRS","CEPU"]
for ticker in tickers:
    data = yf.download(ticker, period='10y')
    ret=data["Adj Close"].to_frame()
    ret.columns= ['AdjClose']
    ret['Yield']=(ret['AdjClose']/ret['AdjClose'].shift(1)-1)*100

ret.dropna(axis=0, how='any', inplace=True)

def getYields(data, fromEMA, toEMA):
   yields =[] , timeIn=[]
   for i in range(fromEMA, toEMA+1):
    key = 'EMA' + str(i)
    data[key] = data['Adj Close'].ewm(span=i).mean()
    data['comprado']=data['Adj Close'].shift()<data[key].shift()
    data['vendido']=data['Adj Close'].shift()>data[key].shift()
    allIn=data.loc[data['comprado']==True]['Yield']
    allOut=data.loc[data['vendido']==True]['Yield']
    qin=allIn.count()
    qout=allOut.count()
    qtot= qin +  qout
    yields.append((allIn.mean()*qin-allOut.mean()*qtot)/qtot)
    timeIn.append(100*qin/qtot)

    return(yields, timeIn)

from shutil import which
def Graficar(tickers,fromEMA, toEMA):
  ejeX= [i for i in range(fromEMA, toEMA+1)]
  fig, (ax1,ax2)=plt.subplots(figsize=(10,10),nrows=2)
  r, yieldsMedios= [], []
  for ticker in tickers:
    data = yf.download(ticker, period='10y')
    ret=data["Adj Close"].to_frame()
    ret.columns= ['AdjClose']
    ret['Yield']=(ret['AdjClose']/ret['AdjClose'].shift(1)-1)*100
    ret.dropna(axis=0, how='any', inplace=True)
    yields,timeIn=getYields(ret, fromEMA, toEMA)
    ax1.plot(ejeX,yields,lw=1, label=ticker)
    ax2.plot(ejeX,timeIn, lw=1,label=ticker)
    r.append(yields)
    yieldsMedios.append(sum(yields)/len(yields))

  yieldsTotal=[(x+y+z/3) for x,y,z in zip(r[0], r[1], r[2])]
  ax1.plot(ejeX,yieldsTotal, lw=1, label='total')

  ax1.legend()
  ax1.set_ylabel('rendimiento % medio diario rueda')
  ax1.grid(which='major', axis='both',alpha=0.15)
  ax2.legend()
  ax2.set_xlabel('Ruedas de la media movil')
  ax2.set_ylabel('porcentaje del tiempo comprado')
  ax2.grid(which='major', axis='both',alpha=0.15)
  fig.subplots_adjust(hspace=0.5)
  return plt, yieldsMedios

tickers=["GGAL", "BMA", "BBAR", "PAM", "TEO", "CRESY","YPF"]
plt, yields = Graficar(tickers, 5, 400)
plt.show()
for i in range(len(tickers)):
  print(tickers[i], yields[i])

import matplotlib.pyplot as plt
import yfinance as yf

def getYields(data, fromEMA, toEMA):
    yields = []
    timeIn = []
    for i in range(fromEMA, toEMA + 1):
        key = 'EMA' + str(i)
        data[key] = data['Adj Close'].ewm(span=i).mean()
        data['comprado'] = data['Adj Close'].shift() < data[key].shift()
        data['vendido'] = data['Adj Close'].shift() > data[key].shift()
        allIn = data.loc[data['comprado'] == True]['Yield']
        allOut = data.loc[data['vendido'] == True]['Yield']
        qin = allIn.count()
        qout = allOut.count()
        qtot = qin + qout
        yields.append((allIn.mean() * qin - allOut.mean() * qtot) / qtot)
        timeIn.append(100 * qin / qtot)

    return yields, timeIn

def Graficar(tickers, fromEMA, toEMA):
    ejeX = [i for i in range(fromEMA, toEMA + 1)]
    fig, (ax1, ax2) = plt.subplots(figsize=(10, 10), nrows=2)
    r = []
    yieldsMedios = []
    for ticker in tickers:
        data = yf.download(ticker, period='10y')
        ret = data["Adj Close"].to_frame()
        ret.columns = ['Adj Close']
        ret['Yield'] = (ret['Adj Close'] / ret['Adj Close'].shift(1) - 1) * 100
        ret.dropna(axis=0, how='any', inplace=True)
        yields, timeIn = getYields(ret, fromEMA, toEMA)
        ax1.plot(ejeX, yields, lw=1, label=ticker)
        ax2.plot(ejeX, timeIn, lw=1, label=ticker)
        r.append(yields)
        yieldsMedios.append(sum(yields) / len(yields))

    yieldsTotal = [(x + y + z / 3) for x, y, z in zip(r[0], r[1], r[2])]
    ax1.plot(ejeX, yieldsTotal, lw=1, label='total')

    ax1.legend()
    ax1.set_ylabel('rendimiento % medio diario rueda')
    ax1.grid(which='major', axis='both', alpha=0.15)
    ax2.legend()
    ax2.set_xlabel('Ruedas de la media movil')
    ax2.set_ylabel('porcentaje del tiempo comprado')
    ax2.grid(which='major', axis='both', alpha=0.15)
    fig.subplots_adjust(hspace=0.5)
    plt.show()

    return yieldsMedios

tickers = ["GGAL", "BMA", "BBAR", "PAM", "TEO", "CRESY","YPF"]
yields = Graficar(tickers, 5, 400)
print("Yields medios:", yields)
