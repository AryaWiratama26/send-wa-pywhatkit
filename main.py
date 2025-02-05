import pywhatkit as pwht
from datetime import datetime

hari = datetime.now()
jam = hari.hour
minute = hari.minute + 2

tlpn_num = input("Number > ")
mess = input("Message > ")

try:
    pwht.sendwhatmsg(tlpn_num,mess,jam,minute,30)
except:
    print("Gagal kirim pesan")