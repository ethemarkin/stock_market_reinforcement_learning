import matplotlib
import matplotlib.pyplot as plt
import os

from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

param = {
    'q': "ASELS", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "IST", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "3Y" # Period (Ex: "1Y" = 1 year)
}
asels = get_price_data(param)
#plt.title('Opening stock prices for IST: ASELS')
#plt.plot(asels['Open'])
#plt.show()

if not os.path.exists('data'):
    os.makedirs('data')
    
asels.to_csv('data/asels.csv', header=False)

param = {
    'q': "THYAO", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "IST", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "3Y" # Period (Ex: "1Y" = 1 year)
}
thy = get_price_data(param)
thy.to_csv('data/thyao.csv', header=False)

param = {
    'q': "ADNAC", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "IST", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "3Y" # Period (Ex: "1Y" = 1 year)
}
adnac = get_price_data(param)
adnac.to_csv('data/adnac.csv', header=False)

param = {
    'q': "ALYAG", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "IST", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "3Y" # Period (Ex: "1Y" = 1 year)
}
alyag = get_price_data(param)
alyag.to_csv('data/alyag.csv', header=False)
