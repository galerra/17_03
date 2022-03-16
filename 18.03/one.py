x_all = "ABCDEFGH"
y_all = "12345678"

FORBIDDEN = {
    "G1": ["up"],
    "A2": ["right"],
    "B2": ["left"],
    "E2": ["up"],
    "G2": ["down"],
    "E3": ["down"],
    "D4": ["up"],
    "G4": ["right"],
    "H4": ["left"],
    "C5": ["up"],
    "D5": ["down"],
    "B6": ["up"],
    "C6": ["down"],
    "F6": ["right"],
    "G6": ["left"],
    "H6": ["up"],
    "B7": ["down"],
    "H7": ["down"],
    "E8": ["right"],
    "F8": ["left"],
}

def move(pos, direct):
    i = x_all.index(pos[0])
    j = y_all.index(pos[1])

    if direct == "left":
        if i > 0:
            return x_all[i - 1] + pos[1]

    elif direct == "right":
        if i < len(x_all) - 1:
            return x_all[i + 1] + pos[1]

    elif direct == "up":
        if j < len(y_all) - 1:
            return pos[0] + y_all[j + 1]

    elif direct == "down":
        if j > 0:
            return pos[0] + y_all[j - 1]

    return pos


def can_move(pos, direct):
    if pos[0] == "A" and direct == "left":
        return False

    elif pos[0] == "H" and direct == "right":
        return False

    elif pos[1] == "8" and direct == "up":
        return False

    elif pos[1] == "1" and direct == "down":
        return False

    rules = FORBIDDEN.get(pos, [])
    return direct not in rules


def execute(start):
    current = start
    while can_move(current, "right"):
        current = move(current, "right")

    while can_move(current, "down"):
        current = move(current, "down")

    while can_move(current, "left"):
        current = move(current, "left")

    while can_move(current, "up"):
        current = move(current, "up")

    return current


if __name__ == "__main__":
    result = []

    for x in x_all:
        for y in y_all:
            start = x + y
            finish = execute(start)
            if start == finish:
                result.append(start)

    print(len(result))
    print(", ".join(result))