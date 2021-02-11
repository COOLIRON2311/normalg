class Word:
    end: bool
    __value: str
    EMPTY: str = 'E'

    def __init__(self, value: str) -> None:
        if not value:
            value = self.EMPTY
        self.__value = value

    def __repr__(self) -> str:
        return self.__value

    @property
    def str(self) -> str:
        return self.__value if self.__value != self.EMPTY else ''
