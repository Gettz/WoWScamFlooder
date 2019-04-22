import requests
from time import sleep
import os
import random
import string
import json
i = 0
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1337))

url = 'http://www.us-warcraft.net/login.asp?a=ok'

names = json.loads(open('names.json').read())
emails = ['@gmail.com', '@mail.com', '@yahoo.com', '@aol.com', '@live.com', '@hotmail.com']
nameArray = random.sample(names, len(names))
while True:
    for name in nameArray:
        name_add = ''.join(random.choice(string.digits))
        username = name.lower() + name_add + emails[random.randint(0, 5)]
        passw = ''.join(random.choice(chars) for i in range(8))

        requests.post(url, allow_redirects=False, data={
            'accountName': username,
            'password': passw
        })
        i = i + 1
        print('%s sending username %s and password %s' % (str(i), username, passw))
        sleep(.2)