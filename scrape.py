# Scrape Google stock data from Yahoo Finance and email it.

import requests
from bs4 import BeautifulSoup
import time
import csv

# Web pages to search

urls = ['https://finance.yahoo.com/quote/IBM?p=IBM&.tsrc=fin-srch','https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch', 'https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch', 'https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch']
# url = 'https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch'

# Adding a header will allow the bot to mimic a browser
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/80.0.3987.116 Safari/537.36'}

## Exporting data to a csv file
csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'Day Range',
                     '52 Week Range', 'Volume', 'Avg. Volume'])

# Extract data from urls
for url in urls:
    stock = []  # Empty list to export data to csv
    html_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_page.content, 'lxml')   # Usxing lxml parser
    # print(html_page.content)   # Print to test output
    #print(soup.title)

    # Extract data: quote title, price, table info
    header_info = soup.find_all('div', id='quote-header-info')[0] # [0] is first item on list
    stock_title = header_info.find('h1').get_text()
    current_price = header_info.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)').find('span').get_text()
    #title = soup.find('title').get_text()

    stock.append(stock_title)
    stock.append(current_price)
    # print(stock_title)
    # print(current_price)
    #print(title)

    table_info = soup.find_all('div', class_='D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) '
                                             'smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')[0].find_all('tr')

    # Loop through stock data table and print
    for i in range(0,8):
        # heading = previous_close_header = table_info[i].find_all('td')[0].get_text()
        value = previous_close_value = table_info[i].find_all('td')[1].get_text()
        stock.append(value)
        # print(heading + ' - ' + value)

    print('---> ')

    csv_writer.writerow(stock )
    time.sleep(5)  # Pause each request so the site does not receive them all at once.
    csv_file.close()
# .get_text() extracts text
