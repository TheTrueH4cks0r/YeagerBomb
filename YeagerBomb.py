#Jordan Kirkwood
'''
Description:
	This takes the csv file from airodump-ng and seperates the data into 2 files. One file puts all the information about the router and only contains
	information pertaining to the bssid(s).The other file will parse out which devices are talking to the bssid.
'''
import time,os,csv,argparse,subprocess,collections
import NaMe,PaTh
import FiLe_AD as AD
from datetime import datetime

################################
bssidchecker=[]
bssidchecker2=[]
WPA=[]
Open=[]
WPA2=[]
checker=set()
checker2=set()
CheckOPEN=set()
################################
file_name=NaMe.FiLe()
file_name_new=PaTh.PaTh(file_name)
file_AD=AD.Final(file_name)
################################
time.sleep(2)
try :
        wait_time=int(input("How many minutes woud you like to scan?\t"))
except ValueError:
        wait_time=1
with open("card","a") as card:
    card.write(file_AD)
    wait__time=int(wait_time) *60
    card.write("&\nwait(%d)\nexit"%((wait__time)))

AD_start=subprocess.Popen("./card")
################################
print("============================================================================================================================================")
print("starting Airodump capture")
time.sleep(8)
readit="%s-01.csv"%(file_name_new)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Starting the YeagerBomb parser.....please wait\n**If an error occurs, make sure that your wireless card is plugged in**\n")

time.sleep(2)
###############################################################################################################################################################################################################################

'''
--output2.csv is to export all of the data from the airodump-ng. This specific file only displays the information about the AP.
--output3.csv is which client(device) the router is talking to.
--bssidchecker is the array in which the bssid will be checked through to see if there is a match. If there is not it is supposed
        to be added to this array.
-- AirodumpOutput.csv is the output of airodump-ng.
'''



with open(readit,"r") as csvfile:
        while wait__time > 0:
                with open("Output1-APS.csv","a+") as Parsed:
                        readit =csv.reader(csvfile,delimiter=',',skipinitialspace='true')
                        with open("Output2-Clients_Connected.csv","a+") as Parsed2:
                                for line in readit:
                                 if len(line) >= 10:
                                        channel=str(line[3]).strip()
                                        bssid=str(line[0]).strip()
                                        encryption=str(line[5]).strip()
                                        power=str(line[8]).strip()
                                        essid=str(line[13]).strip()
                                        '''
--The strip function extracts the position of the line of the csv file. In the csv file the line[2].strip will extract the information that is
in the third column of every row of the file. The csv file treats each row as an array.
                                        '''
                                        if bssid != '00:00:00:00:00:00':
                                            if bssid != 'BSSID':
                                                        if bssid not in checker:
                                                                bssidchecker.append(bssid)
                                                                checker.add(bssid)
                                                                parsed_output1=(bssid,encryption,channel)
                                                                writer=csv.writer(Parsed)
                                                                writer.writerow(parsed_output1)
                                                                if essid=="":
                                                                        essid="ESSID-Unknown"
                                                                if len(essid) >20:
                                                                        essid="ESSID-Hidden/Unknown"
                                                                bssid_essid="%s==%s"%(bssid,essid)
                                                                if encryption=='OPN':
                                                                        Open.append(bssid)
                                                                        CheckOPEN.add(bssid)
                                                                if encryption=='WPA2':
                                                                        WPA2.append(bssid_essid)
                                                                if encryption=='WPA2 WPA':
                                                                        WPA2.append(bssid_essid)
                                                                        '''
--Parsed_output1 formats all of the information that only pertains to Access points.
--writer sets up the writing proccess to print to a csv file. This is output2.csv but in the loop is affiliated with Parsed
--writer.writerow() actually writes to the file
                                '''
                                        
                                 if (len(line) < 10 ) & ( len(line) > 2):
                                         line
                                         #print(line)
                                         client_mac=str(line[0].strip())
                                         bssid2=str(line[5].strip())
                                         essid2=str(line[6].strip())
                                         if bssid2 not in CheckOPEN:
                                                 if bssid2 != 'BSSID':
                                                         if client_mac not in checker2:
                                                                 bssidchecker2.append(bssid2)
                                                                 checker2.add(client_mac)
                                                                 parsed_output2=(client_mac,bssid2,essid2)
                                                                 writer2=csv.writer(Parsed2)
                                                                 writer2.writerow(parsed_output2)
                                                 '''
--This does the same thing as up but this displays the output to the file. 
                                                         '''

                connectedclients=collections.Counter(bssidchecker2)
                print("============================================================================================================================================")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("Time left on Airodump capture: %d seconds\n"%(wait__time))
                print("These are all of the networks in range:\n")
                print (bssidchecker)
                print("\nbssids : #clients connected\n")
                print(connectedclients)
                print("=========================================================================================================\n=\t=\t=\t=\t=\t=\t=\t=\t=\t=\t=\t=\t=\t=\n=========================================================================================================\n=\t=\t=\t=\t=\t=\t=\t=\t=\t=\t=\t=\t=\t=\n=========================================================================================================")
                print("\nBSSIDs using WPA2 encryption:\n")
                print(WPA2)
                print("\nBSSIDs using No encryption:\n")
                print(Open)
                csvfile.seek(0)
                time.sleep(15)
                wait__time=wait__time-15
print("=========================================================================================================\n\t==This data is in a Folder named:\t",file_name,"==\n=========================================================================================================\n")
killit="killall airodump-ng"
subprocess.Popen(killit.split())
