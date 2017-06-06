from datetime import datetime
import subprocess
path=   str(datetime.now().date())
def copy2_path():
    card="cp card %s"%(path)
    card_mode="cp card_mode %s"%(path)
    subprocess.Popen(card.split())
    subprocess.Popen(card_mode.split())
def copy2_Nfile(NPfile):
    card="mv card %s"%(NPfile)
    card_mode="mv card_mode %s"%(NPfile)
    subprocess.Popen(card.split())
    subprocess.Popen(card_mode.split())
