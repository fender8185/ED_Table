++++++


aaaaaa


ssssss


dddddd

import requests
from bs4 import BeautifulSoup

url='https://www.tdcc.com.tw/smWeb/QryStock.jsp?SCA_DATE=20180302&SqlMethod=StockNo&StockNo=1234&StockName=&sub=%ACd%B8%DF'

maxtime=300

while(maxtime):
	maxtime-=1
	print(maxtime)
	try:
		requests.get(url)
	except:
		print('fail')