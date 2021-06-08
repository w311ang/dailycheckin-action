import os

f=open('./config/config.json','rw')
raw=f.read()
raw.replace('$kgqq_cookie',os.getenv('kgqq_cookie'))
f.write(raw)
f.close()
