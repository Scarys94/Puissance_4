import tkinter as tk

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Puissance 4")

        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.board = tk.Canvas(self.frame, width=700, height=600)
        self.board.pack(side=tk.LEFT, padx=10, pady=10)
        self.board.bind("<Button-1>", self.add_disc)

        self.create_board()
        self.turn = 1
        self.columns = [0] * 7
        self.grid = [[0] * 6 for i in range(7)]
        self.discs = []

    def create_board(self):
        for i in range(7):
            self.board.create_line(i*100, 0, i*100, 600, width=2)
        for i in range(6):
            self.board.create_line(0, i*100, 700, i*100, width=2)

    def add_disc(self, event):
        column = event.x // 100
        row = 5 - self.columns[column]
        if row >= 0:
            if self.turn == 1:
                color = "red"
                self.turn = 2
                value = 1
            else:
                color = "blue"
                self.turn = 1
                value = 2
            self.grid[column][row] = value
            disc = self.board.create_oval(column*100+25, row*100+25, column*100+75, row*100+75, fill=color)
            self.discs.append(disc)
            self.columns[column] += 1
            if self.is_winner(column, row, value):
                self.show_winner(value)
            elif self.is_tie():
                self.show_tie()

    def is_winner(self, column, row, value):
        # check horizontal
        count = 0
        for i in range(7):
            if self.grid[i][row] == value:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # check vertical
        count = 0
        for i in range(6):
            if self.grid[column][i] == value:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # check diagonal (top-left to bottom-right)
        count = 0
        row_ = row
        for i in range(column, -1, -1):
            if row_ < 0:
                break
            if self.grid[i][row_] == value:
                count += 1
                if count == 4:
                    return True
                row_ -= 1
            else:
                break
        row_ = row + 1
        for i in range(column+1, 7):
                    if row_ >= 6:
                        break
        if self.grid[i][row_] == value:
            count += 1
            if count == 4:
                return True
            row_ += 1
        else:
            break
            

        # check diagonal (top-right to bottom-left)
        count = 0
        row_ = row
        for i in range(column, 7):
            if row_ < 0:
                break
            if self.grid[i][row_] == value:
                count += 1
                if count == 4:
                    return True
                row_ -= 1
            else:
                break
        row_ = row + 1
        for i in range(column-1, -1, -1):
            if row_ >= 6:
                break
            if self.grid[i][row_] == value:
                count += 1
                if count == 4:
                    return True
                row_ += 1
            else:
                break

        return False

    def is_tie(self):
        return all(val != 0 for val in self.columns)

    def show_winner(self, value):
        if value == 1:
            winner = "Rouge"
        else:
            winner = "Bleu"
        tk.messagebox.showinfo("Gagnant", "Le joueur {} a gagné!".format(winner))
        self.master.quit()

    def show_tie(self):
        tk.messagebox.showinfo("Match nul", "Match nul!")
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
