import fire

while True:
    text = input(">>> ")
    result, error = fire.run(text)

    if error: print(error.as_string())
    else: print(result)