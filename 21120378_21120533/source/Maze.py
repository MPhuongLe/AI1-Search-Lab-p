# referenced function read_file of notebook https://colab.research.google.com/drive/1ejLc4LkrmjpbcRYC3W2xjfA0C0o1PWTp?usp=sharing

class Maze:
    bonus_points = None
    pickup_points = None
    teleporters = {}
    matrix = None
    start = None
    goal = None
    height = None
    width = None

    def is_teleporter(self, i, j):
        if ('a' <= self.matrix[i][j][0] <= 'z' and self.matrix[i][j][0] != 'x'):
            return 1
        return 0

    def get_tele_dest(self, tele_label, i, j):
        arr = self.teleporters[tele_label]
        if (arr[0] == (i, j)):
            return arr[1]
        elif (arr[1] == (i, j)):
            return arr[0]
        return None

    def __init__(self, file_name):
        # with open(file_name,'r') as f:
        f=open(file_name,'r')
        self.bonus_points = []
        self.pickup_points = []
        self.teleporters = {}

        n_bonus_points = int(next(f)[:-1])

        self.bonus_points = []
        for i in range(n_bonus_points):
            x, y, reward = map(int, next(f)[:-1].split(' '))
            self.bonus_points.append((x, y, reward))

        text=f.read()
        self.matrix=[list(i) for i in text.splitlines()]
        
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] == 'S':
                    self.start = (i, j)
                elif self.matrix[i][j] == ' ':
                    if (i == 0) or (i == self.height - 1) or (j == 0) or (j == self.width - 1):
                        self.goal = (i, j)
                if self.is_teleporter(i, j):
                    key = self.matrix[i][j][0]
                    if key not in self.teleporters:
                        self.teleporters[key] = []
                    self.teleporters[key].append((i, j))
