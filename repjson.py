import os

with open('./config/config.json') as f:
  raw=f.read()
raw=raw.replace('$kgqq_cookie',os.getenv('kgqq_cookie'))
print(raw)
with open('./config/config.json','w') as f:
  f.write(raw)
