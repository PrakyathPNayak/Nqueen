class Queen:
    def __init__(self):
        self.count, self.oneD = 0, [0] * 8
        self.queen_place(0)

    def queen_place(self, row):
        if row == 8:
            print(f'\nCount = {self.count + 1}\n' + ''.join((''.join('Q ' if j == self.oneD[i] else '- ' for j in range(8)) + '\n') for i in range(8)))
            self.count += 1
            return
        for col in range(8):
            for i in range(row):
                if self.oneD[i] == col or abs(i - row) == abs(self.oneD[i] - col):break
            else:
                self.oneD[row] = col
                self.queen_place(row + 1)


queen = Queen()
print(f'The program found {queen.count} number of possible variations\nEnd of program')



