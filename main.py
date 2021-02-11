from msvcrt import getch as _getch
from os import name
from sys import exit
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
    print('''Введите схему нормального алгоритма: (ввод заканчивается пустой строкой)

Примеры ввода:
... a b    ~   a -> b
... bc d   ~   bc -> d
... d .E   ~   d -> .E
''')
    lines = []
    while True:
        i = input('... ')
        if not i:
            break
        lines.append(i)
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
        opt = get_opt('>>> ')
        try:
            opts[opt]()
        except KeyError:
            pass
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f'{str(e)}:{e}')


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
