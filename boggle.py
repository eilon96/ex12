import _tkinter
from boggle_board_randomizer import *
from screen_boggle import *
import math


class GameRunner:

    def __init__(self,filename):

        file = open(filename,"r")
        self.__dictionary  = file.read().split("\n")
        self.__board = randomize_board()
        self.__score = 0
        self.__time = 0
        self.__founded_words_list = []
        self.__cur_guess = ""
        file.close()



    """

    all get functions for class variables :

    """

    def get_dictionary(self):
        return self.__dictionary
    def get_board(self):
        return self.__board
    def get_points(self):
        return self.__points
    def get_time(self):
        return self.__time
    def get_founded_words_list(self):
        return self.__founded_words_list
    def get_last_button_pressed(self):
        return self.__last_button_pressed

    """
    all relevant set functions, the dictionary and board should not be changed 
    so they do not have a set function 
    """

    def set_points(self,points):
        """
        :param points: get an amount of points to add to the current amounts of points
        :return: the function adds the points to the points variable
        """
        self.__points += points

    def set_time(self,time):
        """
        :param time: gets an amount of time and adds it to the time variable
        """
        self.__time += time

    def add_founded_words_list(self,word):
        """

        :param word: a word that was found by the user
        :return: adds the word to the founded words list
        """
        self.__founded_words_list.append(word)

    def set_last_button_pressed(self,new_pressed_button):
        """

        :param new_pressed_button: the function gets a tuple representing the coordinates
                of the button that was pressed by the player and set it as the last pressed button
        :return:
        """
        self.__last_button_pressed = new_pressed_button



    def is_press_ok(self,new_letter_crd):
        """
        :param lst_let_crd: a tuple representing the coordinate of the last letter that was picked
        :param new_let_crd: a tuple representing the coordinate of the new letter that was picked
        :return: the function returns True if the player picked a legal letter and False if not
        """
        if abs(self.get_last_button_pressed()[0]-new_letter_crd[0]) >= 2:
            return False
        elif abs(self.get_last_button_pressed()[1]-new_letter_crd[1]) >= 2:
            return False
        return True


    def is_word_in_dict(self , word):
        """

        :param dict: a list of words in the dictionary
        :param word: a word that the player guessed
        :return: if the word is in the dictionary the function returns True else it returns False
        """
        return word in self.get_dictionary()

    def is_repeating_word(self,word):
        """

        :param words_found_list: a list of words that  have already been found
        :param word: a  word that the player guessed
        :return: the function returns True if the word was already found and False otherwise
        """
        return word in self.get_founded_words_list()

    def update_score(self, guess_len):
        self.__score += guess_len**2

