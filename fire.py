# Fire Authors
# If you are contributing to this language please comment the source code as much as possible as it would be hard to figure out stuff

########################################################
# Tokens ( The Language source is commented also :) )
########################################################

# Constants for the token class
# If you are contributing to this language please keep the constants upper case as python does not have a final method so it helps us to know which is a var and which is a const of final

DIGITS = "0123456789"

TT_INT = "TT_INT" # Integer
TT_FLOAT = "FLOAT" # Float
TT_PLUS = "PLUS" # Plus
TT_MINUS = "MINUS" # Minus
TT_MUL = "MUL" # Multiply 
TT_DIV = "DIV" # Divide
TT_LPAREN = "LPAREN" # Left Paren (
TT_RPAREN = "RPAREN" # Right Paren )

# For information TT stands for token type so if you are adding a token add TT_ and the token name.
# The acutal token class

class Token:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f"{self.type}:{self.value}"
        return f"{self.type}"

########################################################
# Errors ( The Language source is commented also :) )
########################################################

# The acutal errors class

class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f"{self.error_name}: {self.details}"
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__("Illegal Character", details)

########################################################
# Lexer ( The Language source is commented also :) )
########################################################

# The acutal lexer class

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self): # pos += 1 ( Just move to the second character )
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in "\t":
                self.advance()

            elif self.current_char in DIGITS:
                tokens.append(self.make_number())

            elif self.current_char == "+":
                tokens.append(Token(TT_PLUS))
                self.advance()

            elif self.current_char == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()

            elif self.current_char == "*":
                tokens.append(Token(TT_MUL))
                self.advance()

            elif self.current_char == "/":
                tokens.append(Token(TT_DIV))
                self.advance()
            
            elif self.current_char == "(":
                tokens.append(Token(TT_LPAREN))
                self.advance()

            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN))
                self.advance()

            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError('"' + char + '"')

        return tokens, None

    def make_number(self): # Function that tells if the current char is a number and is it a int or a float
        num_str = ""
        dot_count = 0 # Dot is a float !

        while self.current_char != None and self.current_char in DIGITS + ".":
            if self.current_char == ".":
                if dot_count == 1: break

                dot_count += 1
                num_str += "."

            else:
                num_str += self.current_char

                self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))

        else:
            return Token(TT_FLOAT, float(num_str))

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error