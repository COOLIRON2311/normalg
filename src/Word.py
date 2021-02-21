class Word:
    end: bool
    __value: str
    EMPTY: str = 'E'

    def __init__(self, value: str) -> None:
        self.__value = value.replace(self.EMPTY, '')

    def __repr__(self) -> str:
        return self.__value if self.__value else self.EMPTY

    @property
    def str(self) -> str:
        return self.__value
