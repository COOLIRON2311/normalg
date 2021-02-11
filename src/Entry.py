from .Word import Word


class Entry:
    pref: Word
    stem: Word
    post: Word

    def __init__(self, pref: str, stem: str, post: str) -> None:
        self.pref, self.stem, self.post = map(Word, (pref, stem, post))

    def __repr__(self) -> str:
        return f'{self.pref} {self.stem} {self.post}'

    def concat(self, highlight = False) -> Word:
        if highlight:
            return Word(f'{self.pref.str}\u001b[31m{self.stem.str}\u001b[0m{self.post.str}')
        else:
            return Word(f'{self.pref.str}{self.stem.str}{self.post.str}')
