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
                       ~ Опции ~
 e:           редактировать схему алгоритма
 p:           показать схему алгоритма
 r:           применить алгоритм к слову
 s:           сохранить схему алгоритма
 l:           загрузить схему алгоритма
 m:           установить лимит итераций
 h:           показать помощь
 q:           выйти из программы

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

(символ "->" зарезервирован)
''')
    lines = []
    while True:
        i = input('... ')
        if '->' in i:
            print('Некорректный ввод\n')
            return
        if not i:
            break
        lines.append(i)
    g['alg'] = MarkovAlgorithm(lines)


def _print() -> None:
    if alg:
        print(alg, '\n')
    else:
        print('Схема алгоритма не задана\n')


def _setm() -> None:
    if alg:
        print(f'''Введите новое максимальное количество итераций:
(текущее - {alg.MAXITER}, 0 - неограниченно)''')
        n = input('... ')
        alg.MAXITER = int(n)
    else:
        print('Схема алгоритма не задана\n')


def _help() -> None:
    print(__doc__)


def save() -> None:
    print('\nВведите имя схемы: ')
    _name = input('... ')
    if alg:
        try:
            with open('alg/'+_name+'.alg', 'w') as f:
                for i in alg.scheme:
                    f.write(f'{i}\n')
        except Exception:
            print('Ошибка')
        else:
            print('\nСхема сохранена')
    else:
        print('Схема алгоритма не задана\n')


def load() -> None:
    print('\nВведите имя схемы: ')
    _name = input('... ')
    try:
        with open('alg/'+_name+'.alg', 'r') as f:
            t = f.read()
        g['alg'] = MarkovAlgorithm(t, sep='->')
    except Exception:
        print('Ошибка')
    else:
        print('\nСхема загружена')
        _print()


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
    'm': _setm,
    'p': _print,
    's': save,
    'l': load,
    'q': exit,
    'r': run
}


def main() -> None:
    _help()
    while True:
        try:
            opt = get_opt('>>> ')
        except UnicodeDecodeError:
            print()
            continue
        try:
            opts[opt]()
        except KeyError:
            continue
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    main()
