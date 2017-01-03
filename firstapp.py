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



def get_updates():
	url="http://www.cricbuzz.com/live-cricket-scores/16872/ind-vs-eng-5th-test-england-tour-of-india-2016-17"
	r=requests.get(url)
	while r.status_code is not 200:
		r=requests.get(url)
	soup=BeautifulSoup(r.text,'html.parser')
	Temp1_name=soup.find_all('div',{'class':'cb-text-gray cb-font-16'})[0].text
	Temp2_name=soup.find_all('div',{'class':'cb-min-bat-rw'})[0].text
	rx=soup.find_all('div',{'class':'cb-text-stump'})[0].text
	if len(Temp1_name)>0:
		Team1_name=re.sub( '\s+', ' ', Temp1_name ).strip()
	else:
		Team1_name='Yet to Bat'
		
	if len(Temp2_name)>0:
	    Team2_name=re.sub( '\s+', ' ', Temp2_name ).strip()
	else:
	     Team2_name='Yet to Bat'    
	if len(rx)>0:
	    stumps=re.sub( '\s+', ' ', rx ).strip()    
	else:
	     stumps='Match in Progress'  

	Match_status=str(Temp1_name)+"\n\n\n\n"
	Match_status=Match_status+str(Temp2_name)+"\n\n\n\n"
	Match_status=Match_status+str(stumps)+"\n\n\n\n"+"\n"
	popup('Score Board:-',Match_status)

	sleep(30)




while True:
	get_updates()


	

	
	


	
get_updates()