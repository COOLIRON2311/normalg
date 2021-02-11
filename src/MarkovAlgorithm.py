from .Substitution import Substitution, Word


class SigmaError(Exception):
    pass


class MarkovAlgorithm:
    scheme: 'list[Substitution]'
    sigma: 'set[str]'
    MAXITER = 100

    def __init__(self, value: 'list | str') -> None:
        self.scheme = []
        self.sigma = set()
        if isinstance(value, str):
            value = (i for i in value.splitlines() if i)
        for i in value:
            _s = Substitution(i)
            self.scheme.append(_s)
            self.sigma.update(set(_s.pair[0].str))
            self.sigma.update(set(_s.pair[1].str))

    def __repr__(self) -> str:
        ret = ['╭']
        for i in self.scheme:
            ret.append(f'╎ {i}')
        ret.append('╰')
        ret.append(f'Σ = {self.sigma}')
        return '\n'.join(ret)

    def apply(self, word: 'str | Word', verbose=False) -> Word:
        if isinstance(word, str):
            word = Word(word)
        for i in word.str:
            if i not in self.sigma:
                raise SigmaError(f'letter {i} not in sigma')
        _it = 1
        while True:
            e = None
            _sub: Substitution
            for i in self.scheme:
                e = i.find_entry(word.str)
                if e:
                    _sub = i
                    break
            if not e:
                return word
            else:
                if verbose:
                    print(f'{_it})', e.concat(highlight=True), '->', end=' ')
                    e = _sub.apply(e)
                    print(e.concat(highlight=True))
                else:
                    e = _sub.apply(e)
                word = e.concat()
                if _sub.final:
                    return word
                _it += 1
                if _it > self.MAXITER:
                    raise StopIteration('maximum iteration count exceeded')