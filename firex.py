import fire

while True:
    text = input(">>> ")
    result, error = fire.run("<stdin>", text)

    if error: print(error.as_string())
    elif result: print(result)