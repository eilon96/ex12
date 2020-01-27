import tkinter as tk
from boggle_board_randomizer import *
from boggle import *

EXIT_TITLE = "Please dont go"
EXIT_MESSAGE = "Are you sure you want to quit?"


class Screen_Boggle:

    def __init__(self,filename,root):

        self.file = filename
        self._root = root
        self._root.geometry("400x380")
        self._root.resizable(0,0)  # Unchangeable size
        self._root.title("BEST BOGGLE GAME EVER")
        self.__game_runner = GameRunner(self.file)
        self._pressed_buttons = []
        self.init_buttons(self.__game_runner.get_board())
        self.init_labels()
        self.init_words_table()
        self.update_time()
        self.disable=False


    def init_buttons(self,board):

        # creates the letter buttons - we will add letter the binding with the
        # event function

        for row_index, row in enumerate(board):

            for letter_index, letter in enumerate(row):
                new_button = tk.Button(self._root, text=letter,
                                font=("Courier", 30), height=2, width=2)
                new_button.config(command=self.letter_pressed_event
                (new_button,letter,row_index,letter_index))

                new_button.grid(row=row_index, column=letter_index)

        # creates the quit button and guess button
        quit_button = tk.Button(self._root, text="Quit", font=("Courier", 32),
                                width=4,command=self.quit_pressed)
        quit_button.place(y=263)
        Try_button = tk.Button(self._root, text="Try", font=("Courier", 32),
                               width=4,command=self.guess_pressed)
        Try_button.place(x=84, y=263)

    def init_labels(self):
        self.__time_label = tk.Label(self._root, text="10:10", font=("Courier", 22), width=12, bg="black", fg="white")
        self.__time_label.place(x=1, y=303)
        self.__points_label = tk.Label(self._root, text="0", font=("Courier", 22), width=11, bg="white", fg="black")
        self.__points_label.place(x=1, y=343)

    def init_words_table(self):
        S = tk.Scrollbar(root)
        S.place(x=380, y=10)
        self.__words_table = tk.Text(self._root, height=2, width=30, font=("Courier", 22), bg="white", fg="black")
        self.__words_table.place(x=185, y=10)
        S.config(command=self.__words_table.yview)
        self.__words_table.config(yscrollcommand=S.set)
        self.__words_table.insert(tk.END, "Guessed words: \n")


    def get_root(self):
        return self._root


    def letter_pressed_event(self,button,letter,row,column):
        # הפונקציה צריכה לממש את שלוש הפעולות הבאות:
        # לבדוק אם המקש רציף אם הלחיצה הקודמת
        # אם כן להמשיך את הרצף ולשנות את ערך המחרזות
        # אם לא לשנות את המסך בהתאם ולהתחיל מחרוזת חדשה
        # button hasn't pressed already,and it's a new guess or legal continue

        def letter_pressed():
            if self.disable == False:
                if self.__game_runner.is_press_ok((row,column)):
                    button.config(fg="red")
                    self._pressed_buttons.append(button) # add to the pressed list
                    self.__game_runner.set_last_button_pressed((row,column))
                    self.__game_runner.set_cur_guess(letter)
                else:
                    self.unpress_all()

        return letter_pressed


    def guess_pressed(self):
        # הפונקציה צריכה לבדוק אם המחרוזת המנוחשת נמצאת במילון
        # אם כן לשנות את הניקוד בהתאם אם לא להדפיס הודעה שגיאה רלוונטית
        if self.disable == False:
            if self.__game_runner.try_word():
                self.__game_runner.update_score()
                self.__points_label.config(text=str(self.__game_runner.get_score()))
            self.unpress_all()
            self.__game_runner.set_cur_guess("")


    def quit_pressed(self,other_root=None):
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
        self.__game_runner.set_time(0)
        self.__time_label.config(text=f"0{self.__game_runner.get_time()//60}:"
                              f"{(self.__game_runner.get_time()%60)//10}"
                              f"{(self.__game_runner.get_time()%60)%10}")
        if not self.__game_runner.did_time_passed():
            self._root.after(1000, self.update_time)
        else:
            self.end_of_time_func()

    def end_of_time_func(self):
        self.disable=True
        self.end_of_time = tk.Tk()
        self.end_of_time.title("Your Time is Up")
        self.end_of_time.geometry("200x100")
        self.end_of_time.resizable(0, 0)
        end_of_time_label = tk.Label(self.end_of_time,
                                text="to continue press continue to \n"
                                         "quit well you know what to do... ")
        end_of_time_label.pack()
        quit_button = tk.Button(self.end_of_time, text="Quit", font=("Courier",
                                        20), width=5,command=self.quit_pressed)
        quit_button.place(x=10,y=50)
        continue_button = tk.Button(self.end_of_time, text="continue",
                                    font=("Courier", 20), width=8,
                                    command=self.continue_button_pressed)
        continue_button.place(x=85,y=50)
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

    def continue_button_pressed(self):
        self.end_of_time.destroy()
        self.__game_runner = GameRunner(self.file)
        self._pressed_buttons = []
        self.init_buttons(self.__game_runner.get_board())
        self.init_labels()
        self.update_time()
        self.disable = False


if __name__ == '__main__':
    root = tk.Tk()
    screen = Screen_Boggle("boggle_dict.txt",root)
    root.mainloop()



