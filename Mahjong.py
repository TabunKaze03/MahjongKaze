import random
import os
from colorama import Fore, Back, Style
from time import sleep


class cards:
    def __init__(self, Ctype, Csort, Cvalue, Cproperty, Cposition):
        self.Ctype = Ctype
        self.Csort = Csort
        self.Cvalue = Cvalue
        self.Cproperty = Cproperty
        self.Cposition = Cposition


HandDeck = []

all_cards = []
char_cards = []
dot_cards = []
bamboo_cards = []
dragon_cards = []
wind_cards = []

# Card places
cards_mountain = []
cards_player1 = []
cards_player2 = []
cards_player3 = []
cards_player4 = []
cards_player1_discard = []
cards_player2_discard = []
cards_player3_discard = []
cards_player4_discard = []


def create_cards():
    print(Fore.LIGHTYELLOW_EX + "[Caution] Creating cards...(1/2)")
    for i in range(1, 10):
        for j in range(1, 5):
            char_cards.append(cards("char", 1, i, None, None))
            dot_cards.append(cards("dot", 2, i, None, None))
            bamboo_cards.append(cards("bamboo", 3, i, None, None))
    print(Fore.LIGHTYELLOW_EX + "[Caution] Creating cards...(2/2)")
    for i in range(1, 5):
        dragon_cards.append(cards("white", 4, 0, "word", None))
        dragon_cards.append(cards("rich", 5, 0, "word", None))
        dragon_cards.append(cards("middle", 6, 0, "word", None))
        wind_cards.append(cards("east", 7, 0, "word", None))
        wind_cards.append(cards("south", 8, 0, "word", None))
        wind_cards.append(cards("west", 8, 0, "word", None))
        wind_cards.append(cards("north", 9, 0, "word", None))
    print(Fore.LIGHTYELLOW_EX + "[Caution] Creating cards...Done")
    print(Style.RESET_ALL)
    sleep(1.5)
    os.system("clear")


create_cards()

for i in char_cards:
    all_cards.append(i)
for i in dot_cards:
    all_cards.append(i)
for i in bamboo_cards:
    all_cards.append(i)
for i in dragon_cards:
    all_cards.append(i)
for i in wind_cards:
    all_cards.append(i)

# check if number of cards is correct
print(Fore.LIGHTYELLOW_EX + "[Caution] Checking the number of cards...")
if len(char_cards) + len(dot_cards) + len(bamboo_cards) + len(dragon_cards) + len(wind_cards) != 136:
    print(Fore.LIGHTRED_EX + "Error: number of cards is incorrect")
    warning = input("proceed anyway?(y/n)")
    if warning == "n":
        exit()
    print(Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX + "[Caution] Checking the number of cards...Done")
print(Style.RESET_ALL)
sleep(1.5)
os.system("clear")


# copy a set of cards for mountain and shuffle
def move_shuffle():
    print(Fore.LIGHTYELLOW_EX + "[Caution] Shuffling cards...")
    for c in all_cards:
        cards_mountain.append(c)
    random.shuffle(cards_mountain)
    print(Fore.LIGHTYELLOW_EX + "[Caution] Shuffling cards...Done")
    print(Style.RESET_ALL)
    sleep(1.5)
    os.system("clear")


# assign winds to players
def assign_winds():
    list = ["east", "south", "west", "north"]
    print(Fore.LIGHTYELLOW_EX + "[Caution] Assigning winds...")
    print(Style.RESET_ALL)
    sleep(1.5)
    os.system("clear")


# assign cards to players (with mountain updated)
def assign_cards():
    print(Fore.LIGHTYELLOW_EX + "[Caution] Assigning cards...")
    for i in range(0, 13):
        cards_player1.append(cards_mountain.pop())
        cards_player2.append(cards_mountain.pop())
        cards_player3.append(cards_mountain.pop())
        cards_player4.append(cards_mountain.pop())
    for i in cards_player1:
        i.Cposition = "player1"
    for i in cards_player2:
        i.Cposition = "player2"
    for i in cards_player3:
        i.Cposition = "player3"
    for i in cards_player4:
        i.Cposition = "player4"
    print(Fore.LIGHTYELLOW_EX + "[Caution] Assigning cards...Done")
    print(Style.RESET_ALL)
    sleep(1.5)
    os.system("clear")


# sort the cards using Csort and Cvalue
def sort_cards():
    cards_player1.sort(key=lambda x: (x.Csort, x.Cvalue))
    cards_player2.sort(key=lambda x: (x.Csort, x.Cvalue))
    cards_player3.sort(key=lambda x: (x.Csort, x.Cvalue))
    cards_player4.sort(key=lambda x: (x.Csort, x.Cvalue))


def display_cards():
    HandDeck.clear()
    for i in cards_player1:
        if i.Cproperty != "word":
            HandDeck.append(str(i.Ctype + str(i.Cvalue)))
        elif i.Cproperty == "word":
            HandDeck.append(str(i.Ctype))
    print(Fore.LIGHTGREEN_EX + str(HandDeck))
    print(Style.RESET_ALL)
    sleep(1.5)
    os.system("clear")


def discard():
    flag = 0
    display_cards()
    ToBeDiscard = input("which card to discard? (cards in list):")
    for i in cards_player1:
        if (i.Ctype + str(i.Cvalue)) == ToBeDiscard:
            cards_player1.remove(i)
            cards_player1_discard.append(i)
            display_cards()
            flag = 1
            break
        if ToBeDiscard == "white" or ToBeDiscard == "rich" or ToBeDiscard == "middle" or ToBeDiscard == "east" or ToBeDiscard == "south" or ToBeDiscard == "west" or ToBeDiscard == "north":
            if i.Ctype == ToBeDiscard:
                cards_player1.remove(i)
                cards_player1_discard.append(i)
                display_cards()
                flag = 1
                break
        if flag == 0:
            print("[Error] Invalid card")
            sleep(1.5)
            os.system("clear")
            discard()






move_shuffle()
assign_cards()
sort_cards()
while 1:
    discard()
    os.system("clear")
