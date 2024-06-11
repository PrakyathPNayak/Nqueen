class Queen:
    def __init__(self):
        self.getaway = 0
        self.count = 0
        self.current_row = 1
        self.current_collumn = 1
        self.oneD = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.twoD = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.lastrow = 1

    def queen_print(self):
        #print(f'In queen_print\nCount = {self.count + 1}')
        for i in range(1, 9, 1):
            out = ''
            for j in range(1, 9, 1):
                if j == self.oneD[i]:
                    out += 'Q '
                else:
                    out += '. '
            print(f'{out}')

    def board_clear(self):
        #print('In board_clear')
        for i in range(1, 9):
            for j in range(1, 9):
                self.twoD[i][j] = 0

    def threat_check(self):
        #print('In threat_check')
        self.board_clear()
        #print(f'last_row = {self.lastrow}')
        for self.current_row in range(1, self.lastrow + 1):
            self.current_collumn = self.oneD[self.current_row]
            for i in range(1, 9):
                for j in range(1, 9):
                    if i == self.current_row or j == self.current_collumn or self.current_row - self. current_collumn == i - j or self.current_row + self.current_collumn == i + j:
                        self.twoD[i][j] = 1
            #print(f'Current_row = {self.current_row}\tCurrent_collumn = {self.current_collumn}')
        self.lastrow += 1
        #print(f'Last_row = {self.lastrow}')
        self.queen_place()

    def queen_place(self):
        #print('In queen_place')
        self.getaway += 1
        for i in range(1, 9):
            if self.lastrow >= 9:
                self.queen_print()
                self.count += 1
                self.lastrow = 6
                self.oneD[8] = 0
                self.threat_check()
            for j in range(self.oneD[i]+1, 9):
                if self.twoD[i][j] == 0:
                    self.oneD[i] = j
                    self.threat_check()
            if i == self.lastrow:
                self.lastrow -= 2
                self.oneD[i] = 0
                self.threat_check()
            if self.getaway > 10:
                self.getaway = 0
                return 0


test = Queen()
while test.count < 100:
    print(f'count = {test.count}')
    a = test.queen_place()
print(f'The program found {test.count} number of possible variations')
print('End of program')
