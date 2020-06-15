import fire

from pygments.lexers.html import HtmlLexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.lexers import PygmentsLexer

from pygments.lexer import RegexLexer
from pygments.token import *

class DiffLexer(RegexLexer):
    name = 'Diff'
    aliases = ['diff']
    filenames = ['*.diff']

    tokens = {
        'root': [
            (r'var', Generic.SubHeading),
            (r'function', Generic.SubHeading),
            (r'if', Generic.SubHeading),
            (r'for', Generic.SubHeading),
            (r'while', Generic.SubHeading),
            (r'\d', Keyword),
            (r'(\".*?\")', Keyword),
        ]
    }
while True:
    text = prompt(">>> ", lexer=PygmentsLexer(DiffLexer))
    result, error = fire.run("<stdin>", text)

    if error: print(error.as_string())
    elif result: print(result)