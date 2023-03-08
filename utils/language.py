import json

def getLanguage(lang):
    with open(f'languages\{lang}.json', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data
