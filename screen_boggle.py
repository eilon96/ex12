import tkinter as tk
from boggle_board_randomizer import *
from boggle import *

EXIT_TITLE = "Please dont go"
EXIT_MESSAGE = "Are you sure you want to quit?"
WINDOW_SIZE = "400x380"
GAME_TITLE = "BEST BOGGLE GAME EVER"
START_LABEL = "Start Game"
END_LABEL = "to resart press restart to \n" \
            "quit well you know what to do... "
LETTER_SIZE = 30


class Screen_Boggle:

    def __init__(self, filename):

        self.file = filename    # the file with the dictionary
        self._root = tk.Tk()   # the root the game runs on
        self._root.geometry(WINDOW_SIZE) # sets the size of the window
        self._root.resizable(0, 0)  # Unchangeable size
        self._root.title(GAME_TITLE)   # sets the title of the game
        self.__game_runner = GameRunner(self.file) # an object of a single game
        self._pressed_buttons = []   # list of  buttons that are already pressed on screen
        self.init_buttons(self.__game_runner.get_board())   # creates the buttons and place them on screen
        self.init_labels()
        self.init_words_table()
        self.update_time()
        self.disable = False
        self.lst_button_pressed = []

    def init_buttons(self, board):

        # creates the letter buttons - we will add letter the binding with the
        # event function

        for row_index, row in enumerate(board):

            for letter_index, letter in enumerate(row):
                new_button = tk.Button(self._root, text=letter,
                                       font=("Courier", LETTER_SIZE), height=2, width=2)
                new_button.config(command=self.letter_pressed_event
                (new_button, letter, row_index, letter_index))

                new_button.grid(row=row_index, column=letter_index)

        # creates the quit button and guess button
        quit_button = tk.Button(self._root, text="Quit", font=("Courier", 32),
                                width=4, command=self.quit_pressed)
        quit_button.place(y=263)
        Try_button = tk.Button(self._root, text="Try", font=("Courier", 32),
                               width=4, command=self.guess_pressed)
        Try_button.place(x=84, y=263)

    def init_labels(self):

        self.__time_label = tk.Label(self._root, text="00:00", font=("Courier", 22),
                                     width=12, bg="black", fg="white")
        self.__time_label.place(x=-7, y=303)

        self.__points_label = tk.Label(self._root, text="0", font=("Courier", 22),
                                       width=11, bg="white", fg="black")

        self.__points_label.place(x=1, y=343)

    def init_words_table(self):

        self.__headline = tk.Label(self._root, height=2, width=15, font=("Courier", 22),
                                   bg="white", fg="black", text="Guessed Words:\n", anchor="nw")

        self.__words_table = tk.Label(self._root, height=20, width=30, font=("Courier", 15),
                                      bg="white", fg="black", anchor="nw",wraplengt=175,justify="left")

        self.__headline.place(x=180, y=10)
        self.__words_table.place(x=180, y=40)



    def letter_pressed_event(self, button, letter, row, column):

        def letter_pressed():

            if self.disable == False and button not in self.lst_button_pressed:

                if self.__game_runner.is_press_ok((row, column)):

                    button.config(fg="red")
                    self._pressed_buttons.append(button)  # add to the pressed list
                    self.__game_runner.set_last_button_pressed((row, column))
                    self.__game_runner.set_cur_guess(letter)
                    self.lst_button_pressed.append(button)

                else:
                    self.unpress_all()

        return letter_pressed

    def guess_pressed(self):

        if not self.disable:

            if self.__game_runner.try_word():
                self.__game_runner.update_score()
                self.__points_label.config(text=str(self.__game_runner.get_score()))
                self.add_word(self.__game_runner.get_cur_guess())

            self.unpress_all()
            self.__game_runner.set_cur_guess("")

    def add_word(self, word):

        text = self.__words_table.cget("text")
        text += f"{word} "
        self.__words_table.config(text=text,anchor="nw")

    def quit_pressed(self, other_root=None):
        """
        This method asks the user if she wants to quit, and if so,
         closes the window
        """
        try:
            self.end_of_time.destroy()
        except AttributeError:
            pass
        finally:
            self.get_root().destroy()

    def update_time(self):
        self.__game_runner.set_time(1)
        self.__time_label.config(
            text=f"0{self.__game_runner.get_time() // 60}:{(self.__game_runner.get_time() % 60) // 10}"
                 f"{(self.__game_runner.get_time() % 60) % 10}")
        if not self.__game_runner.did_time_passed():
            self._root.after(1000, self.update_time)
        else:
            self.end_of_time_func()

    def end_of_time_func(self):
        self.disable = True
        self.end_of_time = tk.Tk()
        self.end_of_time.title("Your Time is Up")
        self.end_of_time.geometry("210x100")
        self.end_of_time.resizable(0, 0)
        end_of_time_label = tk.Label(self.end_of_time,
                                     text=END_LABEL)
        end_of_time_label.pack()
        quit_button = tk.Button(self.end_of_time, text="Quit", font=("Courier",
                                                                     20), width=5, command=self.quit_pressed)
        quit_button.place(x=10, y=50)
        restart_button = tk.Button(self.end_of_time, text="restart",
                                   font=("Courier", 20), width=8,
                                   command=self.restart_button_pressed)
        restart_button.place(x=85, y=50)
        self.end_of_time.mainloop()

    def unpress_all(self):
        """
        This method unpress all the letters buttons,
         and nullify the current guess
        """
        for button in self._pressed_buttons:
            button.config(fg='black')
            self.__game_runner.set_last_button_pressed(None)
        self._pressed_buttons = []
        self.__game_runner.__cur_guess = ""
        self.lst_button_pressed = []

    def restart_button_pressed(self):
        self.end_of_time.destroy()
        self.__game_runner = GameRunner(self.file)
        self._pressed_buttons = []
        self.init_buttons(self.__game_runner.get_board())
        self.init_labels()
        self.init_words_table()
        self.update_time()
        self.disable = False

    def get_root(self):
        return self._root


if __name__ == '__main__':
    screen = Screen_Boggle("boggle_dict.txt")
    screen.get_root().mainloop()
