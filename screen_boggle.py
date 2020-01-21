import tkinter as tk
from boggle_board_randomizer import *
from boggle import *

EXIT_TITLE = "Please dont go"
EXIT_MESSAGE = "Are you sure you want to quit?"


class Screen_Boggle:

    def __init__(self,filename):

        self._root = tk.Tk()
        self._root.geometry("168x380")
        self._root.resizable(0, 0)
        self._root.title("BEST BOGGLE GAME EVER")
        self.__game_runner = GameRunner(filename)
        self._pressed_buttons = []
        self.init_buttons(self.__game_runner.get_board())
        self.init_labels()


        # here we need to add the label that will count the time
        # and the label thats represent the current string the player created

    def init_buttons(self,board):

        # creates the letter buttons - we will add letrter the binding with the event function

        for row_index, row in enumerate(board):

            for letter_index, letter in enumerate(row):

                if letter != "QU":
                    new_button = tk.Button(self._root, text=letter, font=("Courier", 30),
                                           height=2, width=2)
                    new_button.config(command=self.letter_pressed_event(new_button,letter,row_index,letter_index))
                else:
                    new_button = tk.Button(self._root, text=letter, font=("Courier", 30), height=2, width=2)
                    new_button.config(command=self.letter_pressed_event(new_button,letter,row_index,letter_index))

                new_button.grid(row=row_index, column=letter_index)

        # creates the quit button and guess button
        quit_button = tk.Button(self._root, text="Quit", font=("Courier", 32), width=4)
        quit_button.place(y=263)
        Try_button = tk.Button(self._root, text="Try", font=("Courier", 32), width=4,command=self.guess_pressed)
        Try_button.place(x=84, y=263)

    def init_labels(self):
        self.__time_label = tk.Label(self._root, text="10:10", font=("Courier", 22), width=11, bg="black", fg="white")
        self.__time_label.place(x=1, y=303)
        self.__points_label = tk.Label(self._root, text="100", font=("Courier", 22), width=11, bg="white", fg="black")
        self.__points_label.place(x=1, y=343)

    def get_root(self):
        return self._root


    def letter_pressed_event(self,button,letter,row,column):
        # הפונקציה צריכה לממש את שלוש הפעולות הבאות:
        # לבדוק אם המקש רציף אם הלחיצה הקודמת
        # אם כן להמשיך את הרצף ולשנות את ערך המחרזות
        # אם לא לשנות את המסך בהתאם ולהתחיל מחרוזת חדשה
        # button hasn't pressed already,and it's a new guess or legal continue
        def letter_pressed():
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
        if self.__game_runner.is_word_in_dict():
            self.__game_runner.update_score()
            self.__points_label.config(text=str(self.__game_runner.get_score()))
        self.unpress_all()
        self.__game_runner.set_cur_guess("")


    def quit_pressed(self):
        """
        This method asks the user if she wants to quit, and if so,
         closes the window
        """

    def end_of_time(self):
        pass


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

if __name__ == '__main__':
    screen = Screen_Boggle("boggle_dict.txt")
    screen.get_root().mainloop()



