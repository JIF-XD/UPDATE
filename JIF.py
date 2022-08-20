import os
if __name__ == "__main__":
   try:
        os.system("git pull")
       __import__("IG2").login_kamu()
   except Exception as e:
       exit(str(e))
