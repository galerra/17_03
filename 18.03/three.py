x_all = "ABCDEFGH"
y_all = "12345678"

FORBIDDEN = {
    "C2": ["up"],
    "H2": ["up"],
    "B3": ["up"],
    "C3": ["down"],
    "F3": ["right"],
    "G3": ["left"],
    "H3": ["down"],
    "A4": ["up"],
    "B4": ["down"],
    "A5": ["down"],
    "E5": ["right"],
    "F5": ["left"],
    "G5": ["right"],
    "H5": ["left"],
    "B6": ["right"],
    "C6": ["left"],
    "F6": ["up"],
    "E7": ["up"],
    "F7": ["down"],
    "B8": ["right"],
    "C8": ["left"],
    "E8": ["down"],
    "F8": ["right"],
    "G8": ["left"],
}

def move(position, direction):
    i = x_all.index(position[0])
    j = y_all.index(position[1])

    if direction == "left":
        if i > 0:
            return x_all[i - 1] + position[1]

    elif direction == "right":
        if i < len(x_all) - 1:
            return x_all[i + 1] + position[1]

    elif direction == "up":
        if j < len(y_all) - 1:
            return position[0] + y_all[j + 1]

    elif direction == "down":
        if j > 0:
            return position[0] + y_all[j - 1]

    return position


def can_move(position, direction):
    if position[0] == "A" and direction == "left":
        return False

    elif position[0] == "H" and direction == "right":
        return False

    elif position[1] == "8" and direction == "up":
        return False

    elif position[1] == "1" and direction == "down":
        return False

    rules = FORBIDDEN.get(position, [])
    return direction not in rules


def execute(start):
    current = start
    while can_move(current, "down"):
        current = move(current, "down")

    while can_move(current, "right"):
        current = move(current, "right")

    while can_move(current, "up"):
        current = move(current, "up")

    while can_move(current, "left"):
        current = move(current, "left")

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