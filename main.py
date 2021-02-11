from msvcrt import getch as _getch
from os import name
from sys import stdout
from colorama import init
from src import MarkovAlgorithm
from src.Substitution import Substitution

init()
g = globals()
alg: MarkovAlgorithm = None

__doc__ = """
Опции:
e:           редактировать схему алгоритма
p:           распечатать схему алгоритма
r:           применить алгоритм
h:           показать помощь
q:           выйти

"""


def getch() -> str:
    return _getch().decode()


def get_opt(compreply: str) -> str:
    print(compreply, end='')
    ret = getch()
    print(ret)
    return ret


def edit() -> None:
    print('\nВведите схему нормального алгоритма: (ввод заканчивается новой строкой)')
    lines = []
    t = ['', '']
    j = 0
    while True:
        stdout.write('\r')
        r = f'... {t[0]} -> {t[1]}'
        stdout.write(r)
        stdout.write('\r')
        stdout.write(r[:len(t[j]) + j*8 + 4])
        i = getch()
        if i == '\r':
            stdout.write('\u001b[0K')
            break
        elif i in ' ':
            if j == 0:
                j += 1
            else:
                lines.append('{} -> {}'.format(*t))
                t = ['', '']
                j = 0
                stdout.write('\n')
        else:
            t[j] += i

    g['alg'] = MarkovAlgorithm(lines)


def _print() -> None:
    if alg:
        print(alg, '\n')
    else:
        print('Схема алгоритма не задана\n')


def _help():
    print(__doc__)


def run():
    if not alg:
        edit()
        run()
    else:
        print('\nВведите слово:')
        word = input('... ')
        print('\nРезультат:', alg.apply(word, verbose=True))


opts = {
    'e': edit,
    'h': _help,
    'p': _print,
    'q': exit,
    'r': run
}


def main() -> None:
    _help()
    while True:
        try:
            opt = get_opt('>>> ')
        except UnicodeDecodeError:
            opt = ' '
            print()
        try:
            opts[opt]()
        except KeyError:
            pass
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()

# print(getch())
"""
a = MarkovAlgorithm(
    '''
a -> b
b -> c
c -> E
E -> .b
'''
)
# print(a.scheme, a.sigma)
print(a)
print()
print(a.apply('abbc', True))
"""
