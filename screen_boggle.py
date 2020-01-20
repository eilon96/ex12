import tkinter as tk
from boggle_board_randomizer import *
class Screen_Boggle:

    def __init__(self,board):

        self._root = tk.Tk()
        self._root.title("BEST BOGGLE GAME EVER")
        for row_index,row in enumerate(board):
            for letter_index,letter in enumerate(row):
                new_button = tk.Button(self._root,text = letter)
                new_button.grid(row=row_index,column=letter_index,)


if __name__ == '__main__':

    root = tk.Tk()
    root.title("BEST BOGGLE GAME EVER")
    board = randomize_board()
    board[3][3] ="QU"
    root.resizable(0,0)
    print(root.winfo_height())
    for row_index, row in enumerate(board):
        for letter_index, letter in enumerate(row):
            if letter != "QU":
                new_button = tk.Button(root, text=letter,font=("Courier",30),
                                       height=2,width=2)
            else:
                new_button = tk.Button(root, text=letter, font=("Courier", 30),height=2,width=2)

            new_button.grid(row=row_index,column=letter_index)

    root.mainloop()



