import requests,os,random
tok="2070396364:AAFntHYVqCjMP2q62qRAmJUaOFwjL3KpLow"
s=int(input("[?] number of characters : "))
os.system('cls' if os.name == 'nt' else 'clear')#DOOM
try:
	tl=requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=Hi")
except:
	print("[!] ERROR")
	input("")
	exit()
x=0
y=0
chars2 =  "1234567890qwertyuiopasdgfhjklzxcvbnm_1234567890qwertyuiopasdgfhjklzxcvbnm_1234567890qwertyuiopasdgfhjklzxcvbnm_"
for password in range(99999999):
	   p = ''
	   for item in range(s):
	   	p+=random.choice(chars2)
	   dom=requests.get(f"https://tellonym.me/{p}",headers={'Host': 'tellonym.me','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document'}).status_code
	   if dom == 200:
	   	print(f"\033[0;33m[\033[0;35m$\033[0;33m]\033[0;31m {p} | BAD\033[0;37m")
	   elif dom == 404:
	   	print(f"\033[0;33m[\033[0;35m$\033[0;33m]\033[0;32m {p} | GOOD\033[0;37m")
	   	tel=requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=NEW TELLONYM USER\n→{p}")
	   else:
	   	print(f"\033[0;33m[\033[0;35m$\033[0;33m]\033[0;31m {p} | ERROR\033[0;37m")
