# │ normalg │

# Установка:
Дистрибутив программы можно скачать в разделе [Releases](https://github.com/COOLIRON2311/normalg/releases)
<br></br>

# Архитектура:
Все логические единицы программы реализованы в виде [классов](src/), а исходный код может быть легко использован для создания других приложений, работающих с [нормальными алгоритмами Маркова](https://ru.wikipedia.org/wiki/Нормальный_алгоритм).
<br></br>

# Использование:

Принцип работы программы - эмуляция интерпретатора. Пользователю доступны следующие команды:

```
 e:           редактировать схему алгоритма
 p:           показать схему алгоритма
 r:           применить алгоритм к слову
 s:           сохранить схему алгоритма
 l:           загрузить схему алгоритма
 m:           установить лимит итераций
 h:           показать помощь
 q:           выйти из программы
```
Выполнение команды начинается сразу после нажатия соответствующей клавиши.
<br></br>

# Пример использования программы:
В дистрибутиве программы содержится демонстрационная схема [demo](alg/demo.alg).
```
                       ~ Опции ~
 e:           редактировать схему алгоритма
 p:           показать схему алгоритма
 r:           применить алгоритм к слову
 s:           сохранить схему алгоритма
 l:           загрузить схему алгоритма
 m:           установить лимит итераций
 h:           показать помощь
 q:           выйти из программы


>>> l

Введите имя схемы:
... demo

Схема загружена
╭
╎ a -> b
╎ b -> c
╎ c -> E
╰
Σ' = {'c', 'b', 'a'}

>>> r

Введите слово:
... aabbcc
1) aabbcc -> babbcc
2) babbcc -> bbbbcc
3) bbbbcc -> cbbbcc
4) cbbbcc -> ccbbcc
5) ccbbcc -> cccbcc
6) cccbcc -> cccccc
7) cccccc -> ccccc
8) ccccc -> cccc
9) cccc -> ccc
10) ccc -> cc
11) cc -> c
12) c ->

Результат: E
>>>
```