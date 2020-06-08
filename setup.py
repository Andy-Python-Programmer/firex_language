from cx_Freeze import setup, Executable

setup(name = "FireX",
    version = "0.1",
    description = "Finished Number Lexer",
    executables = [Executable("firex.py")])