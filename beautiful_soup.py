from bs4 import BeautifulSoup

import requests

r  = requests.get("https://www.mygov.in/covid-19/?target=webview&type=campaign&nid=0")

src=r.content

soup=BeautifulSoup(src,'lxml')

div=soup.find_all('span',class_='icount')

tags=['Active Cases','Cured/Discharged','Deaths','Migrated']

state_names=soup.find_all('span',class_='st_name')
state_number=soup.find_all('span',class_='st_number')
state_conf=soup.find_all('div',class_='tick-confirmed')
state_active=soup.find_all('div',class_='tick-active')
state_disc=soup.find_all('div',class_='tick-discharged')
helpline=soup.find_all('span',class_='help-no')

for i in range(0,len(state_names)):
  state_names[i]=state_names[i].text
  state_number[i]=state_number[i].text
  state_conf[i]=state_conf[i].text
  state_active[i]=state_active[i].text
  state_disc[i]=state_disc[i].text
  helpline[i]=helpline[i].text
# for i in range(0,len(state_names)):
#   print(state_names[i],"",state_number[i],"\n\t",state_conf[i],"\n\t",state_active[i],"\n\t",state_disc[i])
