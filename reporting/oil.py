import urllib
import time
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import re

def get_price():

    source_pag = 'http://tsw.forexprostools.com?&commodities=8833'
    webpage = urllib.urlopen(source_page).read()
    soup = BeautifulSoup(webpage)
    div = soup.find_all('div', id='mainSummaryDiv_8833')
    price = float(div[0].find_all('p', id='summaryLast')[0].string)

    if price != None:
        history = open('../history.txt', 'a')
        history.write(str(price) + ' - ' + time.strftime('%Y.%m.%d') + '_' + time.strftime('%H.%M.%S') + '\n')
        history.close()

def build_graph():

    prices = list()
    dates = list()

    history = open('../history.txt')
    for line in history:
        prices.append(float(re.findall('([0-9.]+) - ', line)[0]))
        dat = str(re.findall(' - ([0-9.]+)_', line)[0])
        tim = str(re.findall(' - [0-9.]+_([0-9.]+)', line)[0])
        dates.append(dat + '\n' + tim)

    history.close()

    plt.ylim(min(prices)-10, max(prices)+10)

    plt.title('Brent Oil prices')
    plt.xlabel('dates')
    plt.ylabel('$ price')
    graph = tuple(plt.plot(prices, 'r'))
    plt.xticks(range(len(dates)), dates, size='small')

    plt.legend((graph), ['Brent Oil price'])
    plt.show()


get_price()
build_graph()