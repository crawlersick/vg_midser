#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import urllib.request
import base64
import os
folder=('/tmp/ovpnconf')
try:
    os.stat(folder)
except:
    os.mkdir(folder)
for root,dirs,files in os.walk(folder):
    for name in files:
        os.remove(os.path.join(root,name))
        print(os.path.join(root,name))
req=urllib.request.Request('http://192.3.67.204:8001/base64.txt')
f=urllib.request.urlopen(req)

#print(f.read())

base64text=f.read()
bincon=base64.b64decode(base64text)



with open(folder+'/tt1122.zip','wb') as out:
    out.write(bincon)
import zipfile
with zipfile.ZipFile(folder+'/tt1122.zip','r') as zo:
    zo.extractall(folder)


print("This is console module")
