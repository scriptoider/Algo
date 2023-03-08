import logging
import time 
import toml
from utils.color import color # ANSI colors for fancy output
from utils.generator import generateRandom # Pseudorandom number generator
from utils.handler import raiseError # Format error message
from utils.language import getLanguage # Localization, language may be customized in config.toml
from algorithms.number import Number
from algorithms.sorting import Sorting
from algorithms.sequence import Sequence
from algorithms.password import Password

def main():
    logging.basicConfig(level=logging.DEBUG, filename='debug.log', format="%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logging.info(__file__ + ' has been lauched')

    config = toml.load('config.toml')
    quitKeys = config['quitKeys']
    lang = getLanguage(config['language'])
    algorithms = lang['algorithms']

    with open('README.md') as f:
        logo = f.readlines()[:8] # Get ASCII art from README.md
        logo[0] = ' ' + logo[0] # Offset problem solver
        logo = ' '.join(i for i in logo)
        print(color['bold'] + logo + color['clear'])

    while True:
        out = (
            lang['chooseAlgo'].format(str(len(algorithms))) + '\n' +
            '\n'.join(color['blue' if (int(i) % 2) else 'purple'] + str(i) + ' - ' + j for i, j in algorithms.items()) + color['clear']
        )
        print(out)
        while True:
            try:
                n = int(input())
                break
            except Exception:
                print(lang['chooseAlgo'].format(str(len(algorithms))))

        if 1 <= n <= 4:
            algo = Number()
            if n == 1:
                while True:
                    s = input(lang['inputNumberAndItsBaseOfANumberSystemAndAnotherBaseOfANumberSystem']).lower()
                    if s in quitKeys:
                        quit()
                    n1, b1, b2 = list(map(int, s.split()))
                    sn1 = str(n1)
                    skip = False
                    for i in sn1:
                        if int(i) >= b1:
                            skip = True
                            break
                    if skip == True or n1 < 0 or b1 <= 0 or b1 >= 10 or b2 <= 0 or b2 >= 10:
                        raiseError(f"n1 >= 0 {lang['and']} 1 <= b1 <= 9 {lang['and']} 1 <= b2 <= 9")
                        continue
                    break
            if 2 <= n <= 3:
                while True:
                    s = input(lang['input2Numbers']).lower()
                    if s in quitKeys:
                        quit()
                    n1, n2 = list(map(int, s.split()))
                    if n1 <= 0 or n2 <= 0:
                        raiseError(f"n1 >= 1 {lang['and']} n2 >= 1")
                        continue
                    break
            elif n == 4:
                while True:
                    s = input(lang['inputNumber']).lower()
                    if s in quitKeys:
                        quit()
                    n1 = int(s)
                    if n1 < 0 :
                        raiseError("n1 >= 0")
                    break
            match n:
                case 1:
                    ans = str(algo.base(n1, b1, b2))
                case 2:
                    ans = str(algo.gcd(n1, n2))
                case 3:
                    ans = str(algo.gcd(n1, n2))
                case 4:
                    ans = algo.dividers(n1)
                    ans = ' '.join(str(i) for i in ans)
        elif 5 <= n <= 8:
            algo = Sorting()
            while True:
                s = input(lang['inputArrayLengthOrNumberSequence']).lower()
                if s in quitKeys:
                    quit()
                try:
                    lis = list(map(int, s.split()))
                except:
                    raiseError(lang['inputArrayLengthOrNumberSequence'])
                    continue
                if len(lis) == 1:
                    lis = generateRandom(lis[0])
                break
            match n:
                case 5:
                    ans = algo.bubble(lis)
                case 6:
                    ans = algo.insert(lis)
                case 7:
                    ans = algo.select(lis)
                case 8:
                    ans = algo.quick(lis)
            ans = ' '.join(str(i) for i in ans)
        elif n == 9:
            algo = Sequence()
            while True:
                s = input(lang['inputNthNumberOfFibonacci']).lower()
                if s in quitKeys:
                    quit()
                try:
                    n1 = int(s)
                except:
                    raiseError(lang['inputNthNumberOfFibonacci'])
                    continue
                break
            ans = str(algo.fibonacci(n1))
        elif 10 <= n <= 11:
            algo = Password()
            match n:
                case 10:
                    while True:
                        s = input(lang['inputLengthOfPassword']).lower()
                        if s in quitKeys:
                            quit()
                        n1 = int(s)
                        if n1 < 8:
                            raiseError(lang['passwordMustContain'])
                            continue
                        break
                    ans = algo.generatePassword(n)
                case 11:
                    while True:
                        s = input(lang['inputPassword'])
                        if s.lower() in quitKeys:
                            quit()
                        elif len(s.split()) > 1:
                            raiseError(lang['passwordMustNotContain'])
                            continue
                        break
                    ans = algo.checkPassword(s)
                    
        with open('answer.txt', 'w') as f:
            out = (
                "Input\n" +
                f"{s}\n\n" +
                "Output\n" +
                f"{ans}\n\n" +
                "Algorithm\n" +
                algorithms[str(n)]
            )
            f.write(out)
        print(color['green'] + ans + color['clear'])

        time.sleep(config['wait'])
        print('') # New line

if __name__ == "__main__":
    main()
