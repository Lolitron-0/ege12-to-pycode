out = "s = \"\"\n"


def equals_ignore_case(a, b):
    return a.upper() == b.upper()


def line_commands(arr):
    global out
    for i in range(len(arr)):
        command = arr[i]
        if "нашлось" in command:
            try:
                arg = command.split('(')[1][:-1]
            except:  # has spaces
                arg = arr[i + 1][1:-1]
            out += "\"" + arg + "\"" + " in s "
        elif equals_ignore_case(command, "или"):
            out += "or "
        elif equals_ignore_case(command, "и"):
            out += "and "
        elif "заменить" in command:
            try:
                arg1 = command.split('(')[1][:-1]
                arg2 = arr[i + 1][:-1]
            except:  # has spaces
                arg1 = arr[i + 1][1:-1]
                arg2 = arr[i + 2][:-1]
            out += "s = s.replace(" + "\"" + arg1 + "\"" + ", " + "\"" + arg2 + "\"" + ", 1)"


if __name__ == "__main__":
    TAB = " " * 2

    print("Paste pseudo here, type q end")
    lines = []
    while True:
        ln = input()
        if ln == "q":
            break
        lines.append(ln)
    lines = lines[1:-1]

    tabcount = 0

    for line in lines:
        parsed = line.split('\t')[-1].split()
        out += TAB * tabcount
        if parsed[0] == "ПОКА":
            out += "while "
            line_commands(parsed[1:])
            out += ":\n"
            tabcount += 1
        elif parsed[0] == "ЕСЛИ":
            out += "if "
            line_commands(parsed[1:])
            tabcount += 1
            out += ":\n"
        elif parsed[0] == "КОНЕЦ":
            out = out[:-len(TAB) * tabcount]
            tabcount -= 1
        elif parsed[0] == "ИНАЧЕ":
            out = out[:-len(TAB)]
            out += "else: "
            tabcount += 1
            out += "\n"
        else:
            line_commands(parsed)
            out += "\n"
    print(out)
