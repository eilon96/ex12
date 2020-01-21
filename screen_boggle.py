import tkinter as tk
from boggle_board_randomizer import *
from boggle import *

EXIT_TITLE = "Please dont go"
EXIT_MESSAGE = "Are you sure you want to quit?"

class Screen_Boggle:

    def __init__(self,filename):

        self.__root = tk.Tk()
        self.__root.title("BEST BOGGLE GAME EVER")
        self.__game_runner = GameRunner(filename)
        self.init_buttons(self.__game_runner.get_board())
        self.__near_buttons = {}
        self.__pressed_buttons = []


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
        quit_button = tk.Button(self._root,text="Quit This Shity Game",font=("Courier", 30))     # צריך לשחק פה עם הגואי למקם את הכפתור
        quit_button.grid(row=3,column=3)
        guess_button = tk.Button(self._root,text="I think that's a word",font=("Courier", 30))  # צריך לשחק פה עם הגואי למקם את הכפתור
        guess_button.grid(row=8,column=8)


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
        """
        This method asks the user if she wants to quit, and if so,
         closes the window
        """
        if tk.messagebox.askokcancel(EXIT_TITLE, EXIT_MESSAGE):
            self.__root.destroy()

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
    pass