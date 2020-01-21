import tkinter as tk
from boggle_board_randomizer import *
from boggle import *

class Screen_Boggle:

    def __init__(self,filename):

        self._root = tk.Tk()
        self._root.geometry("168x380")
        self._root.resizable(0, 0)
        self._root.title("BEST BOGGLE GAME EVER")
        self.__root = tk.Tk()
        self.__root.title("BEST BOGGLE GAME EVER")
        self.__game_runner = GameRunner(filename)
        self.init_buttons(self.__game_runner.get_board())
        self.__near_buttons = {}
        self.__pressed_buttons = []
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
                else:
                    new_button = tk.Button(self._root, text=letter, font=("Courier", 30), height=2, width=2)

                new_button.grid(row=row_index, column=letter_index)

        # creates the quit button and guess button
        quit_button = tk.Button(self._root, text="Quit", font=("Courier", 32), width=4)
        quit_button.place(y=263)
        Try_button = tk.Button(self._root, text="Try", font=("Courier", 32), width=4)
        Try_button.place(x=84, y=263)

    def init_labels(self):
        self.__time_label = tk.Label(self._root, text="10:10", font=("Courier", 22), width=11, bg="black", fg="white")
        self.__time_label.place(x=1, y=303)
        self.__points_label = tk.Label(self._root, text="100", font=("Courier", 22), width=11, bg="white", fg="black")
        self.__points_label.place(x=1, y=343)
    def get_root(self):
        return self._root

    def letter_pressed(self,button):
        # הפונקציה צריכה לממש את שלוש הפעולות הבאות:
        # לבדוק אם המקש רציף אם הלחיצה הקודמת
        # אם כן להמשיך את הרצף ולשנות את ערך המחרזות
        # אם לא לשנות את המסך בהתאם ולהתחיל מחרוזת חדשה
        # button hasn't pressed already,and it's a new guess or legal continue
        if button not in self.__pressed_buttons and \
            (not self.__pressed_buttons or \
            button in self.__near_buttons[self.__pressed_buttons[-1]]):
            button.configure(bg = "red")
            self.__pressed_buttons.append(button) # add to the pressed list
            self.__game_runner.__cur_guess += button.text
        else:
            self.unpress_all()

    def guess_pressed(self):
        # הפונקציה צריכה לבדוק אם המחרוזת המנוחשת נמצאת במילון
        # אם כן לשנות את הניקוד בהתאם אם לא להדפיס הודעה שגיאה רלוונטית
        if self.__game_runner.check_guess():
            self.__game_runner.update_score(len(self.guess_pressed()))
            self.update_score_board()
        self.unpress_all()


    def quit_pressed(self):
        # הפונקציה סוגרת את המשחק (או מדפיסת הודעה לברר ששואלת אם להתחיל מחדש או לפרוש)

    def end_of_time(self):
        # הפונקציה מטפלת במקרה והזמן נגמר
        # הפונקציה תקושר לפונקציה after שמקבלת זמן ריצה ולאחריו מפעילה את הפונקציה הקשורה
        # תדפיס הודעת שגיאה מתאימה וכו׳

    def unpress_all(self):
        """
        This method unpress all the letters buttons,
         and nullify the current guess
        """
        for button in self.__pressed_buttons:
            button.configure(bg='')
        self.__pressed_buttons = []
        self.__game_runner.__cur_guess = ""

if __name__ == '__main__':
    screen = Screen_Boggle("boggle_dict.txt")
    screen.get_root().mainloop()




