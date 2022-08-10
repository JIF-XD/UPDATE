import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;91m\x1b[1;43m\033[1;31m LAHORE - KARACHI & ISLAMABAD \x1b[0m\x1b[1;97m\x1b[1;41m IS MY DREAM BEB :( \x1b[0m ")
    print("\n\x1b[1;92m Congratulations Beb Your Device Support This Tool\033[1;37m")
    print("          \033[1;91mUse Vpn If Tool Run Error!") 
    from JIF import login
    login()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Beb Your Mobile Not Support This Tool\x1b[1;93m")
    print("Because Your Device Is Old Version 32bit and This Tool Is Work On 64bit Devices - Please Change Your Device and Try Again.\n\x1b[1;92mThanku For Using our Tool\x1b[1;97m") 
