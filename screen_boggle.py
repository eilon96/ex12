import tkinter as tk
from boggle_board_randomizer import *
from boggle import *

EXIT_TITLE = "Please dont go"
EXIT_MESSAGE = "Are you sure you want to quit?"
LTRS_FNT_SZ = 30
FUNCS_FNT_SZ = 32
CMD_Y_PLACE = 263
TRY_X_PLACE = 84



class Screen_Boggle:

    def __init__(self,filename,root):

        self._root = root
        self._root.geometry("168x380")
        self._root.resizable(0, 0)
        self._root.title("BEST BOGGLE GAME EVER")
        self.__game_runner = GameRunner(filename)
        self._pressed_buttons = []
        self.init_buttons(self.__game_runner.get_board())
        self.init_labels()
        self.update_time()


    def init_buttons(self,board):

        # creates the letter buttons - we will add letrter the binding with the event function

        for row_index, row in enumerate(board):

            for letter_index, letter in enumerate(row):

                if letter != "QU":
                    new_button = tk.Button(self._root, text=letter, font=("Courier", LTRS_FNT_SZ),
                                           height=2, width=2)
                    new_button.config(command=self.letter_pressed_event(new_button,letter,row_index,letter_index))
                else:
                    new_button = tk.Button(self._root, text=letter, font=("Courier", LTRS_FNT_SZ), height=2, width=2)
                    new_button.config(command=self.letter_pressed_event(new_button,letter,row_index,letter_index))

                new_button.grid(row=row_index, column=letter_index)

        # creates the quit button and guess button
        quit_button = tk.Button(self._root, text="Quit", font=("Courier", FUNCS_FNT_SZ), width=4)
        quit_button.place(y=CMD_Y_PLACE)
        Try_button = tk.Button(self._root, text="Try", font=("Courier", FUNCS_FNT_SZ), width=4,command=self.guess_pressed)
        Try_button.place(x=TRY_X_PLACE, y=CMD_Y_PLACE)

    def init_labels(self):
        self.__time_label = tk.Label(self._root, text="10:10", font=("Courier", 22), width=11, bg="black", fg="white")
        self.__time_label.place(x=1, y=303)
        self.__points_label = tk.Label(self._root, text="100", font=("Courier", 22), width=11, bg="white", fg="black")
        self.__points_label.place(x=1, y=343)
        self.time_ended_label = tk.Message(self._root,text="zmancha avar")

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
        if self.__game_runner.try_word():
            self.__game_runner.update_score()
            self.__points_label.config(text=str(self.__game_runner.get_score()))
        self.unpress_all()
        self.__game_runner.set_cur_guess("")


    def quit_pressed(self):
        """
        This method asks the user if she wants to quit, and if so,
         closes the window
        """

    def update_time(self):
        self.__game_runner.set_time(1)
        self.__time_label.config(text=f"0{self.__game_runner.get_time()//60}:{(self.__game_runner.get_time()%60)//10}{(self.__game_runner.get_time()%60)%10}")
        if not self.__game_runner.did_time_passed():
            self._root.after(1000, self.update_time)
        else:
            self.end_of_time()

    def end_of_time(self):
        self.time_ended_label.pack()
        self._root.destroy()

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
    root = tk.Tk()
    screen = Screen_Boggle("boggle_dict.txt",root)
    root.mainloop()



