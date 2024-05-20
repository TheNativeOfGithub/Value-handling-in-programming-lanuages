class Commands:
    def __init__(self):
        self.int = "int"
        self.float = "float"
        self.str = "str"
        self.bool = "bool"

        self.add = "add"
        self.dec = "dec"
        self.mul = "mul"
        self.exp = "exp"

        self.cfor = "for"
        self.cdef = "def"


class Errors:
    def ValueNameError(self):
        print("ValueNameError, can't define the name of a value other types except str.(bool, int, float)")
    def UnknownCommand(self):
        print("UnknownCommand")
    def WrongValueName(self):
        print("WrongValueName")

tokenised = []

class Lexer:
    @staticmethod
    def tokeniser(input_string):
        global tokenised
        tokenised = input_string.split(' ')

class values:
    cached_int = {}
    cached_str = {}
    cached_float = {}
    cached_bool = {}
    
class Tokens:
    @staticmethod
    def valueCreator():
        if tokenised[0] == "str":
            if tokenised[2] == "=":
                name = tokenised[1]
                try:
                    if name == int(name) or name == float(name):
                        Errors.ValueNameError
                except ValueError:
                    values.cached_str[tokenised[1]] = str(tokenised[3])
            else:
                Errors.UnknownCommand
        
        if tokenised[0] == "int":
            if tokenised[2] == "=":
                name = tokenised[1]
                try:
                    if name == int(name) or name == float(name):
                        Errors.ValueNameError
                except ValueError:
                    values.cached_int[tokenised[1]] = int(tokenised[3])    
            else:
                Errors.UnknownCommand

        if tokenised[0] == "float":
            if tokenised[2] == "=":
                name = tokenised[1]
                try:
                    if name == int(name) or name == float(name):
                        Errors.ValueNameError
                except ValueError:
                    values.cached_float[tokenised[1]] = float(tokenised[3])
            else:
                Errors.UnknownCommand

        if tokenised[0] == "bool":
            if tokenised[2] == "=":
                name = tokenised[1]
                try:
                    if name == int(name) or name == float(name):
                        Errors.ValueNameError
                except ValueError:
                    values.cached_bool[tokenised[1]] = bool(tokenised[3])
            else:
                Errors.UnknownCommand


values.cached_str.clear
values.cached_int.clear
values.cached_float.clear
values.cached_bool.clear

while True:
    user_input = input(">>> ")
    Lexer.tokeniser(user_input)
    if user_input == "valuedebug":
        print(f"int {values.cached_int} float {values.cached_float} str {values.cached_str} bool {values.cached_bool}")
    Tokens.valueCreator()
