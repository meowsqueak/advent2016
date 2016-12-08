width = 50
height = 6

class Row(object):
    def __init__(self):
        self.pixels = [ False ] * width

    def count_lit(self):
        return self.pixels.count(True)

    def __getitem__(self, x):
        return self.pixels[x]

    def __setitem__(self, x, value):
        self.pixels[x] = value

    def rotate(self, n):
        self.pixels = self.pixels[-n:] + self.pixels[:-n]

class Display(object):
    def __init__(self):
        self.rows = [Row() for x in range(height)]

    def count_lit(self):
        sum = 0
        for row in self.rows:
            sum += row.count_lit()
        return sum

    def execute(self, ins):
        if ins.startswith("rect"):
            x, y = ins.split()[1].split('x')
            self.do_rect(int(x), int(y))
        elif ins.startswith("rotate column"):
            tokens = ins.split()
            x = int(tokens[2].split("=")[1])
            a = int(tokens[4])
            self.do_rotate_column(x, a)
        elif ins.startswith("rotate row"):
            tokens = ins.split()
            y = int(tokens[2].split("=")[1])
            a = int(tokens[4])
            self.do_rotate_row(y, a)

    def set(self, x, y, v):
        self.rows[y][x] = v

    def do_rect(self, x, y):
        print("do_rect {0} {1}".format(x, y))
        for i in range(y):
            for j in range(x):
                self.set(j, i, True)

    def do_rotate_column(self, x, a):
        print("do_rotate_column {0} {1}".format(x, a))
        column = [ self.rows[y][x] for y in range(height) ]
        column = column[-a:] + column[:-a]
        for y in range(height):
            self.rows[y][x] = column[y]

    def do_rotate_row(self, y, a):
        print("do_rotate_row {0} {1}".format(y, a))
        self.rows[y].rotate(a)

    def describe(self):
        result = ""
        for y in range(height):
            for x in range(width):
                result += "O" if self.rows[y][x] else "-"
            result += "\n"
        return result

d = Display()

for ins in open("8.input"):
    print(ins.strip())
    d.execute(ins.strip())
    print(d.describe())

print(d.count_lit())

