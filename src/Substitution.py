from .Entry import Entry, Word


class Substitution:
    SPLIT: str = '->'
    pair: 'list[Word]'
    final: bool

    def __init__(self, value: str) -> None:
        self.final = '.' in value
        self.pair = []
        for i in value.split(self.SPLIT):
            self.pair.append(Word(i.strip(' .')))

    def __repr__(self) -> str:
        return f'{self.pair[0]} -> {"." if self.final else ""}{self.pair[1]}'

    def find_entry(self, word: str) -> 'Entry | None':
        if self.pair[0].str in word:
            i = word.find(self.pair[0].str)
            if i >= 0:
                l = len(self.pair[0].str)
                b = word[:i]
                e = word[i+l:]
                return Entry(b, self.pair[0].str, e)

    def apply(self, entry: Entry) -> 'Entry | None':
        entry.stem = self.pair[1]
        return entry

