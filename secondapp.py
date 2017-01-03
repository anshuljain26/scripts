import requests
from bs4 import BeautifulSoup
import pynotify
import re
from time import sleep
def popup(title, abc):
	pynotify.init("app")
	pop = pynotify.Notification(title, abc)
	pop.show()
	return


def get_update():
	url="http://www.espncricinfo.com/"
	r=requests.get(url)
	while r.status_code is not 200:
		r=requests.get(url)

	soup=BeautifulSoup(r.text,'html.parser')
	result=soup.find_all('ul',{'class':'scoreline-list international'})
	for res in result:
		update=res.find_all(href=re.compile('south-africa-v-sri-lanka'))[0].text
		break

	score_updates=update

	popup("Score Board:-", score_updates)
	sleep(30)



while True:
	get_update()

