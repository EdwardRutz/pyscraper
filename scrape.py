# Scrape Google stock data from Yahoo Finance and email it.

import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch'

# Adding a header will allow the bot to mimic a broswer
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/80.0.3987.116 Safari/537.36'
           }
html_page = requests.get(url, headers=headers)

# Print to test output
# print(html_page.content)

soup = BeautifulSoup(html_page.content, 'lxml')
#print(soup.title)

header_info = soup.find_all('div', id='quote-header-info')[0] # [0] is first item on list
stock_title = header_info.find('h1').get_text()
current_price = header_info.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)').find('span').get_text()
#title = soup.find('title').get_text()

# stock.append(stock_title)
# stock.append(current_price)
print(stock_title)
print(current_price)
#print(title)

table_info = soup.find_all('div', class_='D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) '
                                         'smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')[0].find_all('tr')

# Loop through stock data and print
for i in range(0,8):
    heading = previous_close_header = table_info[i].find_all('td')[0].get_text()
    value = previous_close_value = table_info[i].find_all('td')[1].get_text()

    print(heading + ' - ' + value)

# .get_text() extracts text
