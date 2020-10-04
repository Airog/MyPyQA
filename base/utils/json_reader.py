import json

with open('config/navigation.json') as conf_file:
    config = json.load(conf_file)

def getMainUrl():
    return config['page_inet_main']