import requests
import json


def send_Message(text1)->str:
    url = "https://api.telegram.org/bot5162058688:AAFaViJ22ZgxQ0RCpBHbb-etMdT2Y53T0_Y/sendMessage"
    keys = {'chat_id':1219709167, 'text':text1}
    r = requests.get(url, params=keys)
    x = r.json()
    return x

def get_update():
    url2 = 'https://api.telegram.org/bot162058688:AAFaViJ22ZgxQ0RCpBHbb-etMdT2Y53T0_Y/getUpdates'
    m = requests.get(url2)
    if m.status_code == 200:
        data1 = m.json()['result'][-1]
        text2 = data1['message']['text']
    else:
        print(f'error: {m.status_code}')
    return text2

while True:
    url1 = 'https://api.telegram.org/bot162058688:AAFaViJ22ZgxQ0RCpBHbb-etMdT2Y53T0_Y/getUpdates'
    l = requests.get(url1)
    if l.status_code == 200:
        data = l.json()['result'][-1]
        text1 = data['message']['text']
        
        if text1 == get_update():
            print(0)
            
        else:
            send_Message(get_update())
            print(1)
            
    else:
        print(f'error: {l.status_code}')

