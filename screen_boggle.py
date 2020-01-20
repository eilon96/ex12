import tkinter as tk
from boggle_board_randomizer import *
from boggle import *

class Screen_Boggle:

    def __init__(self,filename):

        self._root = tk.Tk()
        self._root.title("BEST BOGGLE GAME EVER")
        self.__game_runner = GameRunner(filename)
        self.init_buttons(self.__game_runner.get_board())


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
    def guess_pressed(self):
        # הפונקציה צריכה לבדוק אם המחרוזת המנוחשת נמצאת במילון
        # אם כן לשנות את הניקוד בהתאם אם לא להדפיס הודעה שגיאה רלוונטית
    def quit_pressed(self):
        # הפונקציה סוגרת את המשחק (או מדפיסת הודעה לברר ששואלת אם להתחיל מחדש או לפרוש)
    def end_of_time(self):
        # הפונקציה מטפלת במקרה והזמן נגמר
        # הפונקציה תקושר לפונקציה after שמקבלת זמן ריצה ולאחריו מפעילה את הפונקציה הקשורה
        # תדפיס הודעת שגיאה מתאימה וכו׳

if __name__ == '__main__':

    root = tk.Tk()
    root.title("BEST BOGGLE GAME EVER")
    randomize_board()
    for row_index, row in enumerate(randomize_board()):
        for letter_index, letter in enumerate(row):
            if letter != "QU":
                new_button = tk.Button(root, text=letter, font=("Courier", 30),
                                       height=2, width=2)
            else:
                new_button = tk.Button(root, text=letter, font=("Courier", 30), height=2, width=2)

            new_button.grid(row=row_index, column=letter_index)



    root.mainloop()




