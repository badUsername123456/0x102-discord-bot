from tokens import tokens as _tokens
from token_cls import jplToken
from parser import jplParser
import re


class jplLexer:
    def __init__(self) -> None:
        self.tokens: list[jplToken] = []
        self.line: int = 0

    def tokenize(self, code: str) -> list:
        self.tokens = []
        self.line = 0

        last: jplToken = None
        inStr: bool = False
        string: str = ""
        wrd: str = ""

        for idx, char in enumerate(code):
            if char == "\n":
                self.line += 1
                wrd = ""

            elif char in ("'", '"') and not inStr:
                inStr = True
                string = char
                continue

            elif char in ("'", '"'):
                string += char

                self.tokens.append(jplToken(string, "string", self.line, idx))
                last = self.tokens[-1]

                inStr = False
                string = ""
                continue

            elif inStr:
                string += char
                continue

            elif char in [
                " ",
                "}",
                "]",
                ",",
                ";",
                "=",
                ":",
                "(",
                ")",
                "{",
                "[",
                "<",
                ">",
                "+",
                "-",
                "*",
                "/",
                "%",
                "!",
                "+",
                "-",
            ]:
                self.tokens.append(self.identify(wrd, idx))

                last = self.identify(char, idx)
                self.tokens.append(last)

                wrd = ""

            else:
                wrd += char

        self.tokens.append(self.identify(wrd, idx))

        self.tokens = self.clean()

        return self.tokens

    def clean(self) -> list[jplToken]:
        tok: list[jplToken] = []
        las: jplToken = None

        for token in self.tokens:
            if token is None:
                continue

            elif token.name == "eq":
                if las.raw == "=":
                    tok.pop()
                    tok.append(jplToken("==", "eqeq", self.line, token.idx))
                    continue

                elif las.raw == "!":
                    tok.pop()
                    tok.append(jplToken("!=", "ne", self.line, token.idx))
                    continue

                elif las.raw == ">":
                    tok.pop()
                    tok.append(jplToken(">=", "ge", self.line, token.idx))
                    continue

                elif las.raw == "<":
                    tok.pop()
                    tok.append(jplToken("<=", "le", self.line, token.idx))
                    continue

                else:
                    tok.append(token)

            if las:
                if las.name == "add" and token.name == "add":
                    tok.pop()
                    tok.append(jplToken("++", "inc", self.line, token.idx))
                    continue

                elif las.name == "sub" and token.name == "sub":
                    tok.pop()
                    tok.append(jplToken("--", "dec", self.line, token.idx))
                    continue

            las = token
            tok.append(token)

        return tok

    def identify(self, wrd: str, idx: int) -> jplToken:
        if wrd == " ":
            return None

        for rgx, name in _tokens.items():
            if re.match(rgx, wrd):
                return jplToken(wrd, name, self.line, idx)