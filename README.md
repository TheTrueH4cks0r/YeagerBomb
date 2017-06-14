# YeagerBomb Version 1.2.0

YeagerBomb is a project in the development stage. The goal of the project is to combine a fast wifi(WPA,WEP,WPA2) cracker, and
  enumerate the network. It is possible that the project will later to a vulnerability assessment, or pentest. This project
  is for **EDUCATIONAL PURPOSES ONLY**. 

**Yeagerbomb 1.2.0 will:**

-use your EXTERNAL wireless card in promiscuous mode to cpature APs(Access Points) and routers **Note: YAY! You don't have to tell the script which wireless interface you are using **

-create a folder with the current capture date, with you(the user) creating subfolders where all the data will be stored

-the captured information and put it into two customized capture files, as well as the airodump-ng captured information



**Installation Instructions:**
1) Download the repository
2) In your terminal:

cd Yeagerbomb

sudo su

./configure <----THIS WILL DOWNLOAD PYTHON 3 & will set permissions for the code to run. Without this, the code will fail.

3) Plug your wireless card in <---- Does not matter the interface name, but the first one plugged in will be the one used
4) In your terminal:

python3 YeagerBomb.py


Want to get updates and see where this project is going? Well I've started a blog here-http://yeagerbomb.kinja.com/. More code
will be coming. About every week YeagerBomb will be updated.
