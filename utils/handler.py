from utils.color import color

def raiseError(message):
    out = color['red'] + message + color['clear']
    print(out)
