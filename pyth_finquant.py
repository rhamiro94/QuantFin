

#Importo librerias
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
#Defino tickers de Adrs que voy a analizar

tickers = ["GGAL", "BMA", "BBAR", "PAM", "TEO", "CRESY","YPF","EDN","TGS","TX","TS","SUPV","IRS","CEPU"]
data = yf.download(tickers, period='10y')
#Inspecciono el dataframe

#Defino una función que grafique un heatmap para determinados argumentos
def graficaCorr(dfCorr, title=''):
  import matplotlib.pyplot as plt
  import numpy as np

  fig=plt.figure(figsize=(10,10))
  plt.matshow(dfCorr,fignum=fig.number,cmap='BuPu')
  plt.xticks(range(dfCorr.shape[1]), dfCorr.columns, fontsize=10, rotation=90)
  plt.yticks(range(dfCorr.shape[1]), dfCorr.columns, fontsize=10)

  cb=plt.colorbar(orientation='vertical', label= "Factor Correlación 'r'")
  cb.ax.tick_params(labelsize=10)
  plt.title(title, fontsize=10, y=1.2)

  ax=plt.gca()
  ax.set_xticks(np.arange(-.5, len(dfCorr),1),minor=True);
  ax.set_yticks(np.arange(-.5, len(dfCorr),1),minor=True);
  ax.grid(which='minor', color='w', linewidth=3)

  for i in range(dfCorr.shape[0]):
    for j in range(dfCorr.shape[1]):
      if dfCorr.iloc[i,j] >= 0.6:
          color = 'white'
      else:
          color = 'black'
      fig.gca().text(i,j,"{:.2f}".format(dfCorr.iloc[i,j]), ha='center', va='center', color=color,size="10")

  return(plt)

#Correlacion Volumenes
tabla=pd.DataFrame()
for ticker in tickers:
  data= yf.download(ticker, period='10y')
  tabla= pd.concat([tabla,data["Volume"]],axis=1)
tabla.columns= tickers

plt=graficaCorr(tabla.corr(), title="Heatmap Volumenes ADRs")
plt.show()

import pandas as pd
tickers = ["GGAL", "BMA", "BBAR", "PAM", "TEO", "CRESY","YPF","EDN","TGS","TX","TS","SUPV","IRS","CEPU"]
tabl_v=pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, period='10y')
    data["Variación"] = data["Adj Close"] / data["Adj Close"].shift(1) - 1
    data["Volatilidad"] = data["Variación"].rolling(window=0).std()
    tabl_v[ticker] = data["Volatilidad"]

data



tabl_v.dropna(axis=0, how='any', inplace=True)


plt=graficaCorr(tabl_v.corr())


