from datetime import datetime

path=   str(datetime.now().date())
per=    datetime.now()
per_h=  str(per.hour)
per_m=  str(per.minute)
timeit= str("%s:%s"%(per_h,per_m))

def Final(file_name):
    NPfile=  str("%s-%s"%(file_name,timeit))
    A_Dump= "airodump-ng wlan0 -w "
    ADFN=   A_Dump+NPfile
    return ADFN
