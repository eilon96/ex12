import _tkinter
from boggle_board_randomizer import *
import math

def is_press_ok(lst_let_crd,new_let_crd):
    """
    :param lst_let_crd: a tuple representing the coordinate of the last letter that was picked
    :param new_let_crd: a tuple representing the coordinate of the new letter that was picked
    :return: the function returns True if the player picked a legal letter and False if not
    """
    if abs(lst_let_crd[0]-new_let_crd[0]) >= 2:
        return False
    elif abs(lst_let_crd[1]-new_let_crd[1]) >= 2:
        return False
    return True


def is_word_in_dict(dict, word):
    """

    :param dict: a list of words in the dictionary
    :param word: a word that the player guessed
    :return: if the word is in the dictionary the function returns True else it returns False
    """
    return word in dict

def is_repeating_word(words_found_list,word):
    """

    :param words_found_list: a list of words that  have already been found
    :param word: a  word that the player guessed
    :return: the function returns True if the word was already found and False otherwise
    """
    return word in words_found_list

def read_dict_file(file_name):
    """

    :param file_name: the function gets a given file path
    :return: the function returns the words in the file as a list
    """
    file = open(file_name,"r")
    ret_lst = file.read().split("\n")
    return ret_lst





if __name__ == '__main__':

    print(randomize_board())