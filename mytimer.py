import tkinter as tk

class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        self.state = False
        self.minutes = 25
        self.seconds = 0

        self.display = tk.Label(master, height=10, width=10, textvariable="")
        self.display.config(text="00:00")
        self.display.grid(row=0, column=0, columnspan=2)

        self.start_button = tk.Button(master, bg="Green", activebackground="Dark Green", text="Start", width=8, height=4, command=self.start())
        self.start_button.grid(row=1, column=0)

        self.pause_button = tk.Button(master, bg="Red", activebackground="Dark Red", text="Pause", width=8, height=4, command=self.pause())
        self.pause_button.grid(row=1, column=1)

        self.countdown()

    def countdown(self):
        """Displays a clock starting at min:sec to 00:00, ex: 25:00 -> 00:00"""
        mins = self.minutes
        secs = self.seconds

        if self.state == True:
            if secs < 10:
                if mins < 10:
                    self.display.config(text="0%d : 0%d" % (mins, secs))
                else:
                    self.display.config(text="%d : 0%d" % (mins, secs))
            else:
                if mins < 10:
                    self.display.config(text="0%d : %d" % (mins, secs))
                else:
                    self.display.config(text="%d : %d" % (mins, secs))

            if (mins == 0) and (secs == 0):
                self.display.config(text="Done!")
            else:
                if secs == 0:
                    mins -= 1
                    secs = 59
                else:
                    secs -= 1

                self.master.after(1000, self.countdown())

        elif self.state == False:
            self.master.after(100, self.countdown())

    def start(self):
        if self.state == False:
            self.state = True

    def pause(self):
        if self.state == True:
            self.state = False


if __name__ == '__main__':

    root = tk.Tk()
    my_timer = Timer(root)
    root.mainloop()