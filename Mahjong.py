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


HandDeck1 = []
HandDeck2 = []
HandDeck3 = []
HandDeck4 = []

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
cards_player1_Pon = []
cards_player2_Pon = []
cards_player3_Pon = []
cards_player4_Pon = []

CanPon1 = []
CanPon2 = []
CanPon3 = []
CanPon4 = []

LastP = 0


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
    sleep(0.2)
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
sleep(0.2)
os.system("clear")


# copy a set of cards for mountain and shuffle
def move_shuffle():
    print(Fore.LIGHTYELLOW_EX + "[Caution] Shuffling cards...")
    for c in all_cards:
        cards_mountain.append(c)
    random.shuffle(cards_mountain)
    print(Fore.LIGHTYELLOW_EX + "[Caution] Shuffling cards...Done")
    print(Style.RESET_ALL)
    sleep(0.2)
    os.system("clear")


# assign winds to players
def assign_winds():
    list = ["east", "south", "west", "north"]
    print(Fore.LIGHTYELLOW_EX + "[Caution] Assigning winds...")
    print(Style.RESET_ALL)
    sleep(0.2)
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
    sleep(0.2)
    os.system("clear")


# sort the cards using Csort and Cvalue
def sort_cards():
    cards_player1.sort(key=lambda x: (x.Csort, x.Cvalue))
    cards_player2.sort(key=lambda x: (x.Csort, x.Cvalue))
    cards_player3.sort(key=lambda x: (x.Csort, x.Cvalue))
    cards_player4.sort(key=lambda x: (x.Csort, x.Cvalue))


def display_cards(player):
    global HandDeck1
    global HandDeck2
    global HandDeck3
    global HandDeck4
    if player == 1:
        HandDeck1 = []
        for i in cards_player1:
            if i.Cproperty != "word":
                HandDeck1.append(str(i.Ctype + str(i.Cvalue)))
            elif i.Cproperty == "word":
                HandDeck1.append(str(i.Ctype))
        print(Fore.LIGHTGREEN_EX + "HAND DECK OF PLAYER 1: " + str(HandDeck1))
        print(Style.RESET_ALL)
        sleep(0.2)
        os.system("clear")
    if player == 2:
        HandDeck2 = []
        for i in cards_player2:
            if i.Cproperty != "word":
                HandDeck2.append(str(i.Ctype + str(i.Cvalue)))
            elif i.Cproperty == "word":
                HandDeck2.append(str(i.Ctype))
        print(Fore.LIGHTGREEN_EX + "HAND DECK OF PLAYER 2: " + str(HandDeck2))
        print(Style.RESET_ALL)
        sleep(0.2)
        os.system("clear")
    if player == 3:
        HandDeck3 = []
        for i in cards_player3:
            if i.Cproperty != "word":
                HandDeck3.append(str(i.Ctype + str(i.Cvalue)))
            elif i.Cproperty == "word":
                HandDeck3.append(str(i.Ctype))
        print(Fore.LIGHTGREEN_EX + "HAND DECK OF PLAYER 3: " + str(HandDeck3))
        print(Style.RESET_ALL)
        sleep(0.2)
        os.system("clear")
    if player == 4:
        HandDeck4 = []
        for i in cards_player4:
            if i.Cproperty != "word":
                HandDeck4.append(str(i.Ctype + str(i.Cvalue)))
            elif i.Cproperty == "word":
                HandDeck4.append(str(i.Ctype))
        print(Fore.LIGHTGREEN_EX + "HAND DECK OF PLAYER 4: " + str(HandDeck4))
        print(Style.RESET_ALL)
        sleep(0.2)
        os.system("clear")


def GetCard(player):
    if cards_mountain:
        NewCard = cards_mountain.pop()
        if player == 1:
            cards_player1.append(NewCard)
            if NewCard.Cproperty != "word":
                print(Fore.LIGHTGREEN_EX + "Your new card is: " + str(NewCard.Ctype + str(NewCard.Cvalue)))
            elif NewCard.Cproperty == "word":
                print(Fore.LIGHTGREEN_EX + "Your new card is: " + str(NewCard.Ctype))
        if player == 2:
            cards_player2.append(NewCard)
            if NewCard.Cproperty != "word":
                print(Fore.LIGHTGREEN_EX + "Your new card is: " + str(NewCard.Ctype + str(NewCard.Cvalue)))
            elif NewCard.Cproperty == "word":
                print(Fore.LIGHTGREEN_EX + "Your new card is: " + str(NewCard.Ctype))
        if player == 3:
            cards_player3.append(NewCard)
            if NewCard.Cproperty != "word":
                print(Fore.LIGHTGREEN_EX + "Your new card is: " + str(NewCard.Ctype + str(NewCard.Cvalue)))
            elif NewCard.Cproperty == "word":
                print(Fore.LIGHTGREEN_EX + "Your new card is: " + str(NewCard.Ctype))
        if player == 4:
            cards_player4.append(NewCard)
            if NewCard.Cproperty != "word":
                print(Fore.LIGHTGREEN_EX + "Your new card is: " + str(NewCard.Ctype + str(NewCard.Cvalue)))
            elif NewCard.Cproperty == "word":
                print(Fore.LIGHTGREEN_EX + "Your new card is: " + str(NewCard.Ctype))
        sort_cards()


def discard(player):
    global LastP
    global LastCard
    if player == 1:
        display_cards(1)
        trash = str(input("Choose a card to discard:"))
        if trash in HandDeck1:
            cards_player1_discard.append(cards_player1.pop(HandDeck1.index(trash)))
            LastP = 1
            LastCard = trash
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            discard(1)
    if player == 2:
        display_cards(2)
        trash = str(input("Choose a card to discard:"))
        if trash in HandDeck2:
            cards_player2_discard.append(cards_player2.pop(HandDeck2.index(trash)))
            LastP = 2
            LastCard = trash
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            discard(2)
    if player == 3:
        display_cards(3)
        trash = str(input("Choose a card to discard:"))
        print(HandDeck3)
        if trash in HandDeck3:
            cards_player3_discard.append(cards_player3.pop(HandDeck3.index(trash)))
            LastP = 3
            LastCard = trash
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            discard(3)
    if player == 4:
        display_cards(4)
        trash = str(input("Choose a card to discard:"))
        print(HandDeck4)
        if trash in HandDeck4:
            cards_player4_discard.append(cards_player4.pop(HandDeck4.index(trash)))
            LastP = 4
            LastCard = trash
            # I love this move, since HandDeck and cards_player are synchronized,
            # use HandDeck to find the index of the card and then pop it from cards_player.
            # no copilot used, figure it out myself *proud_face*
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            discard(4)


def CHK_pon():
    global CanPon1, CanPon2, CanPon3, CanPon4
    # Gonna initialize the list every time so the list won't repeat itself
    CanPon1 = []
    CanPon2 = []
    CanPon3 = []
    CanPon4 = []
    for a in HandDeck1:
        if HandDeck1.count(a) == 2:
            CanPon1.append(str(a))
    for b in HandDeck2:
        if HandDeck2.count(b) == 2:
            CanPon2.append(str(b))
    for c in HandDeck3:
        if HandDeck3.count(c) == 2:
            CanPon3.append(str(c))
    for d in HandDeck4:
        if HandDeck4.count(d) == 2:
            CanPon4.append(str(d))
        CanPon1 = list(set(CanPon1))
        CanPon2 = list(set(CanPon2))
        CanPon3 = list(set(CanPon3))
        CanPon4 = list(set(CanPon4))
    print(CanPon1)
    print(CanPon2)
    print(CanPon3)
    print(CanPon4)


def want_Pon():
    global decide
    if CanPon1 != [] and LastP != 1 and LastP != 0 and LastCard in CanPon1:
        decide = str(input("P1,which do you want to Pon " + LastCard + " ? (or 'skip') "))
        if decide != "skip" and (decide in CanPon1):
            cards_player1_Pon.append(cards_player1.pop(HandDeck1.index(decide)))
            cards_player1_Pon.append(cards_player1_discard.pop())
        elif decide == "skip":
            pass
    if CanPon2 != [] and LastP != 2 and LastP != 0 and LastCard in CanPon2:
        decide = str(input("P2,which do you want to Pon " + LastCard + " ? (or 'skip') "))
        if decide != "skip" and (decide in CanPon2):
            cards_player2_Pon.append(cards_player2.pop(HandDeck2.index(decide)))
            cards_player2_Pon.append(cards_player2_discard.pop())
        elif decide == "skip":
            pass
    if CanPon3 != [] and LastP != 3 and LastP != 0 and LastCard in CanPon3:
        decide = str(input("P3,which do you want to Pon " + LastCard + " ? (or 'skip') "))
        if decide != "skip" and (decide in CanPon3):
            cards_player3_Pon.append(cards_player3.pop(HandDeck3.index(decide)))
            cards_player3_Pon.append(cards_player3_discard.pop())
        elif decide == "skip":
            pass
    if CanPon4 != [] and LastP != 4 and LastP != 0 and LastCard in CanPon4:
        decide = str(input("P4,which do you want to Pon " + LastCard + " ? (or 'skip') "))
        if decide != "skip" and (decide in CanPon4):
            cards_player4_Pon.append(cards_player4.pop(HandDeck4.index(decide)))
            cards_player4_Pon.append(cards_player4_discard.pop())
        elif decide == "skip":
            pass


# functions list:
# 1. move_shuffle()
# 2. assign_winds()
# 3. assign_cards()
# 4. sort_cards()
# 5. display_cards(player)
# 6. GetCard(player)
# 7. discard(player)
# 8. CHK_pon()
# 9. Want_Pon(player)

move_shuffle()
assign_winds()
assign_cards()
sort_cards()
display_cards(1)
display_cards(2)
display_cards(3)
display_cards(4)
GetCard(1)
discard(1)
CHK_pon()
want_Pon()
GetCard(2)
discard(2)
CHK_pon()
want_Pon()
GetCard(3)
discard(3)
CHK_pon()
want_Pon()
GetCard(4)
discard(4)
CHK_pon()
want_Pon()
