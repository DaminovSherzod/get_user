import requests
import json
def get_user(data:dict)->dict:
    user = dict()

    user['name'] = data['name']
    user['slug'] = data['slug']
    user['abbr'] = data['abbr']
    user['id'] = data['id']

    return user

user_data = {
    'data':[]
}

n = 1
users = []
while len(users)<n:
    r = requests.get('https://api-football-standings.azharimm.site/leagues')
    if r.status_code == 200:
        data = r.json()['data'][0]
        users.append(get_user(data))
        print(f'{len(users)}/{n}')
    else:
        print(f'Request error: {r.status_code}')

with open('users.json', 'w') as f:
    json.dump(users, f, indent=2)