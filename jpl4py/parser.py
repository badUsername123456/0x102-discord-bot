from handlers.h_for import hFor
from handlers.h_fnc import hFnc


class jplParser:
    def __init__(self) -> None:
        self.tokens: list = []
        self.tree: list[any] = []

    def parse(self, tokens_: list) -> None:
        self.tokens = tokens_

        for idx, token in enumerate(self.tokens):
            print(token)

            if token.name == "for":
                print(self.get_nested_content(self.tokens[idx:], hFor))

            elif token.name in ["jf", "cf", "pf"]:
                print("here")
                print(self.get_nested_content(self.tokens[idx:], hFnc))

    def get_nested_content(self, tokens: list, cls: object) -> None:
        nest_level: int = 0
        inner: list = []

        for t in tokens:
            if t.name == "lbrace":
                nest_level += 1

            elif t.name == "rbrace":
                nest_level -= 1
                if nest_level == 0:
                    inner.append(t)
                    break

            inner.append(t)

        return cls(inner)