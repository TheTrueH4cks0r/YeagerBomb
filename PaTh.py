

import os,errno
import CoPy
from datetime import datetime

path=   str(datetime.now().date())
per=    datetime.now()
per_h=  str(per.hour)
per_m=  str(per.minute)
timeit= str("%s:%s"%(per_h,per_m))

#ADFN=Airodump File Name
#NPfile=(Near Perfect)file


def PaTh(file_name):
    NPfile=  str("%s-%s"%(file_name,timeit))                 
    try:
        os.makedirs(path)
        CoPy.copy2_path()
        os.chdir(path)
        os.makedirs(NPfile)
        CoPy.copy2_Nfile(NPfile)
        os.chdir(NPfile)
    except OSError:
        CoPy.copy2_path()
        os.chdir(path)
        os.makedirs(NPfile)
        CoPy.copy2_Nfile(NPfile)
        os.chdir(NPfile)
    return NPfile


