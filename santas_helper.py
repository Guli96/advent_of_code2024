def get_input_lines(day: int, part: int, demo = False):
    filepath = f"input\\{str(day).rjust(2, '0')}_{str(part)}"
    print(filepath)
    if demo:
        filepath += "_d"
    file = open(filepath)
    output = file.read().splitlines()
    file.close()
    return output
