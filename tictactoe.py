import re


def sum_chars(s, ch):
    m = [0 for c in s]
    for i in range(3):
        for j in range(3):
            if s[i * 3 + j] == ch:
                m[i] += 1
                m[j + 3] += 1
                if i == j:
                    m[6] += 1
                if j == 2 - i:
                    m[7] += 1
    return m

def draw(s):
    k = 0
    line = "---------\n"
    for i in range(3):
        line += "| "
        for j in range(3):
            line += f"{s[k]} "
            k += 1
        line += "|\n"
    line += "---------"
    print(line)

def analyze(s):
    ch_x = sum_chars(t, 'X')
    ch_o = sum_chars(t, 'O')
    cnt_x = ch_x[0] + ch_x[1] + ch_x[2]
    cnt_o = ch_o[0] + ch_o[1] + ch_o[2]
    is_x_win = 3 in ch_x
    is_o_win = 3 in ch_o
    if abs(cnt_x - cnt_o) > 1 or is_x_win and is_o_win:
        print("Impossible")
    elif is_x_win:
        print("X wins")
    elif is_o_win:
        print("O wins")
    elif cnt_x + cnt_o == 9:
        print("Draw")
    else:
        print("Game not finished")


t = input("Enter cells: ")
draw(t)
while True:
    digs = input("Enter the coordinates: ")
    if not re.match("[1-9] [1-9]", digs):
        print("You should enter numbers!")
    elif not re.match("[1-3] [1-3]", digs):
        print("Coordinates should be from 1 to 3!")
    else:
        row, col = digs.split()
        k = 3 * (int(row) - 1) + int(col) -1
        if t[k] == '_':
            t = t[:k] + 'X' + t[k + 1:]
            break
        else:
            print("This cell is occupied! Choose another one!")
# analyze(t)
draw(t)
