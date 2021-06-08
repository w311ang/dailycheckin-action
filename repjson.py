import os

with open('./config/config.json') as f:
  raw=f.read()
raw.replace('$kgqq_cookie',os.getenv('kgqq_cookie'))
with open('./config/config.json','w') as f:
  f.write(raw)
