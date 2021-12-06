# import pandas as pd
# import requests


# url = 'https://bitscreener.com/?f=pfm_1m_lt_-5,pfm2_6m_gt_20&t=listview'

# header = {
#   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
#   "X-Requested-With": "XMLHttpRequest"
# }

# r = requests.get(url, headers=header)

# dfs = pd.read_html(r.text)

# btc = dfs

# print(btc)

# import websocket
# import json
# import threading
# import time

# def send_json_request(ws, request):
#   ws.send(json.dumps(request))

# def recieve_json_response(ws):
#   response = ws.recv()
#   if response:
#     return json.loads(response)

# def heartbeat(interval, ws):
#   print('heartbeat begin')
#   while True:
#     time.sleep(interval)
#     heartbeatJSON ={
#       "op": 1,
#       "d": "null"
#     }
#     send_json_request(ws, heartbeatJSON)
#     print('Heartbeat sent')

# ws = websocket.WebSocket()
# ws.connect("wss://gateway.discord.gg/?v=6&encording=json")
# event = recieve_json_response(ws)
# heartbeat_interval = event['d']['heartbeat_interval'] / 1000
# threading._start_new_thread(heartbeat, (heartbeat_interval,ws))

# token = "OTAyNDk1ODQ4Mzg5MzAwMjg0.YXujMA.qNI5ZiSoQas8bggGdeT-mjrHIOA"
# payload = {
#   "op": 2,
#   "d":{
#     "token" : token,
#     "intents": 513,
#     "properties": {
#       "$os": 'linux',
#         '$browser': 'chrome',
#         '$device': 'pc'
#     }

#   }
# }

# send_json_request(ws, payload)

# while True:
#   event = recieve_json_response(ws)
#   try: 
#     content = event['d']['content']
#     print(f"{content}")
#     op_code = event('op')
#     if op_code == 11:
#       print('heatbeat received')
#   except:
#     pass


import requests
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

url = "https://api.coinmarketcap.com/data-api/v3/map/all?listing_status=active,untracked&exchangeAux=is_active,status&cryptoAux=is_active,status&start=1&limit=1000"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

crypto_list = json.loads(response.text)

ratios = {}

def check_volume_ratio(coin):
  print(coin)

  # marketcap = html.findAll('div',{"class":"statsValue"})[0].decode_contents()
  # volume = html.findAll('div',{"class":"statsValue"})[2].decode_contents()
  try:
    html = urlopen("https://coinmarketcap.com/currencies/{}/".format(coin))
    html = BeautifulSoup(html,"html.parser")
    elem = 3
    name = html.findAll('div',{"class":"sc-16r8icm-0 cEbjrm statsLabel"})[3].decode_contents()
    #print(name)
    while name != 'Volume / Market Cap':
      elem += 1
      print(elem)
      name = html.findAll('div',{"class":"sc-16r8icm-0 cEbjrm statsLabel"})[elem].decode_contents()
    
    volume_ratio = html.findAll('div',{"class":"statsValue"})[elem].decode_contents()
    volume_ratio = float(volume_ratio)
  except:
    volume_ratio = None


  # print(f"marketcap: {marketcap}")
  # print(f"volume: {volume}")
  # print(f"volume_ra
  # 
  # tio: {volume_ratio}")
  return volume_ratio

times = 0

for i in range(1000):
  #print(crypto_list['data']['cryptoCurrencyMap'][i]['name'])
  times += 1
  if times == 10:
    time.sleep(20)
    times = 0
  coin = crypto_list['data']['cryptoCurrencyMap'][i]['name']
  coin = coin.replace(" ", "-")
  coin = coin.replace(".", "-")
  #print(coin)
  volume_ratio = check_volume_ratio(coin)
  ratios[coin] = volume_ratio

for key,val in dict(ratios).items():
  if val is None:
    del ratios[key]


sorted_list = sorted(ratios.items(), key=lambda x: x[1], reverse=True)
# print(sorted_list)
for i in range(20):
  print(sorted_list[i])



