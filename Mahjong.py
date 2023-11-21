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
cards_player1_Kan = []
cards_player2_Kan = []
cards_player3_Kan = []
cards_player4_Kan = []

CanPon1 = []
CanPon2 = []
CanPon3 = []
CanPon4 = []

CanKan1 = []
CanKan2 = []
CanKan3 = []
CanKan4 = []

CanKan1N = []
CanKan2N = []
CanKan3N = []
CanKan4N = []

LastP = 0
NextP = 1

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


def syncHandDecks():
    global HandDeck1
    global HandDeck2
    global HandDeck3
    global HandDeck4
    HandDeck1 = []
    HandDeck2 = []
    HandDeck3 = []
    HandDeck4 = []
    for i in cards_player1:
        if i.Cproperty != "word":
            HandDeck1.append(str(i.Ctype + str(i.Cvalue)))
        elif i.Cproperty == "word":
            HandDeck1.append(str(i.Ctype))
    for i in cards_player2:
        if i.Cproperty != "word":
            HandDeck2.append(str(i.Ctype + str(i.Cvalue)))
        elif i.Cproperty == "word":
            HandDeck2.append(str(i.Ctype))
    for i in cards_player3:
        if i.Cproperty != "word":
            HandDeck3.append(str(i.Ctype + str(i.Cvalue)))
        elif i.Cproperty == "word":
            HandDeck3.append(str(i.Ctype))
    for i in cards_player4:
        if i.Cproperty != "word":
            HandDeck4.append(str(i.Ctype + str(i.Cvalue)))
        elif i.Cproperty == "word":
            HandDeck4.append(str(i.Ctype))

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
    global NextP
    if player == 1:
        display_cards(1)
        trash = str(input("Choose a card to discard:"))
        if trash in HandDeck1:
            cards_player1_discard.append(cards_player1.pop(HandDeck1.index(trash)))
            LastP = 1
            LastCard = trash
            NextP = 2
            print("Cards that P1 discarded: " + str(cards_player1_discard))
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
            NextP = 3
            print("Cards that P2 discarded: " + str(cards_player2_discard))
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            discard(2)
    if player == 3:
        display_cards(3)
        trash = str(input("Choose a card to discard:"))
        if trash in HandDeck3:
            cards_player3_discard.append(cards_player3.pop(HandDeck3.index(trash)))
            LastP = 3
            LastCard = trash
            NextP = 4
            print("Cards that P3 discarded: " + str(cards_player3_discard))
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            discard(3)
    if player == 4:
        display_cards(4)
        trash = str(input("Choose a card to discard:"))
        if trash in HandDeck4:
            cards_player4_discard.append(cards_player4.pop(HandDeck4.index(trash)))
            LastP = 4
            LastCard = trash
            NextP = 1
            print("Cards that P4 discarded: " + str(cards_player4_discard))
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


def want_Pon():
    global decidePon
    global NextP
    if CanPon1 != [] and LastP != 1 and LastP != 0 and LastCard in CanPon1:
        decidePon = str(input("P1,which do you want to Pon " + LastCard + " ? (or 'skip') "))
        if decidePon != "skip" and (decidePon in CanPon1):
            for i in range(0, 2):
                syncHandDecks()
                cards_player1_Pon.append(cards_player1.pop(HandDeck1.index(decidePon)))
            if LastP == 2:
                cards_player3_Pon.append(cards_player2_discard.pop())
            if LastP == 3:
                cards_player3_Pon.append(cards_player3_discard.pop())
            if LastP == 4:
                cards_player3_Pon.append(cards_player4_discard.pop())
            discard(1)
            NextP = 2
        elif decidePon == "skip":
            pass
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            want_Pon()

    if CanPon2 != [] and LastP != 2 and LastP != 0 and LastCard in CanPon2:
        decidePon = str(input("P2,which do you want to Pon " + LastCard + " ? (or 'skip') "))
        if decidePon != "skip" and (decidePon in CanPon2):
            for i in range(0, 2):
                syncHandDecks()
                cards_player2_Pon.append(cards_player2.pop(HandDeck2.index(decidePon)))
            if LastP == 1:
                cards_player3_Pon.append(cards_player1_discard.pop())
            if LastP == 3:
                cards_player3_Pon.append(cards_player3_discard.pop())
            if LastP == 4:
                cards_player3_Pon.append(cards_player4_discard.pop())
            discard(2)
            NextP = 3
        elif decidePon == "skip":
            pass
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            want_Pon()

    if CanPon3 != [] and LastP != 3 and LastP != 0 and LastCard in CanPon3:
        decidePon = str(input("P3,which do you want to Pon " + LastCard + " ? (or 'skip') "))
        if decidePon != "skip" and (decidePon in CanPon3):
            for i in range(0, 2):
                syncHandDecks()
                cards_player3_Pon.append(cards_player3.pop(HandDeck3.index(decidePon)))
            if LastP == 1:
                cards_player3_Pon.append(cards_player1_discard.pop())
            if LastP == 2:
                cards_player3_Pon.append(cards_player2_discard.pop())
            if LastP == 4:
                cards_player3_Pon.append(cards_player4_discard.pop())
            discard(3)
            NextP = 4
        elif decidePon == "skip":
            pass
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            want_Pon()

    if CanPon4 != [] and LastP != 4 and LastP != 0 and LastCard in CanPon4:
        decidePon = str(input("P4,which do you want to Pon " + LastCard + " ? (or 'skip') "))
        if decidePon != "skip" and (decidePon in CanPon4):
            for i in range(0, 2):
                syncHandDecks()
                cards_player3_Pon.append(cards_player3.pop(HandDeck3.index(decidePon)))
            if LastP == 1:
                cards_player3_Pon.append(cards_player1_discard.pop())
            if LastP == 2:
                cards_player3_Pon.append(cards_player2_discard.pop())
            if LastP == 3:
                cards_player3_Pon.append(cards_player3_discard.pop())
            discard(4)
            NextP = 1
        elif decidePon == "skip":
            pass
        else:
            print(Fore.LIGHTRED_EX + "Error: card not found")
            print(Style.RESET_ALL)
            want_Pon()


def CHK_kan():
    global CanKan1, CanKan2, CanKan3, CanKan4, CanKan1N, CanKan2N, CanKan3N, CanKan4N
    CanKan1 = []
    CanKan2 = []
    CanKan3 = []
    CanKan4 = []
    for a in HandDeck1:
        if HandDeck1.count(a) == 3:
            CanKan1.append(str(a))
        if HandDeck1.count(a) == 4:
            CanKan1N.append(str(a))
    for b in HandDeck2:
        if HandDeck2.count(b) == 3:
            CanKan2.append(str(b))
        if HandDeck2.count(b) == 4:
            CanKan2N.append(str(b))
    for c in HandDeck3:
        if HandDeck3.count(c) == 3:
            CanKan3.append(str(c))
        if HandDeck3.count(c) == 4:
            CanKan3N.append(str(c))
    for d in HandDeck4:
        if HandDeck4.count(d) == 3:
            CanKan4.append(str(d))
        if HandDeck4.count(d) == 4:
            CanKan4N.append(str(d))
        CanKan1 = list(set(CanKan1))
        CanKan2 = list(set(CanKan2))
        CanKan3 = list(set(CanKan3))
        CanKan4 = list(set(CanKan4))
        CanKan1N = list(set(CanKan1N))
        CanKan2N = list(set(CanKan2N))
        CanKan3N = list(set(CanKan3N))
        CanKan4N = list(set(CanKan4N))


def want_Kan():
    global decideKan
    global NextP
    if CanKan1 != [] and LastP != 1 and ((LastCard in CanKan1) or CanKan1N != []):
        if LastCard in CanKan1:
            decideKan = str(input("P1,which do you want to Kan " + LastCard + " ? (or 'skip') "))
            if decideKan != "skip" and (decideKan in CanKan1):
                syncHandDecks()
                cards_player1_Kan.append(cards_player1.pop(HandDeck1.index(decideKan)))
                cards_player1_Kan.append(cards_player1.pop(HandDeck1.index(decideKan)))
                cards_player1_Kan.append(cards_player1.pop(HandDeck1.index(decideKan)))
                cards_player1_Kan.append(cards_player1_discard.pop())
                if LastP == 2:
                    cards_player1_Kan.append(cards_player2_discard.pop())
                if LastP == 3:
                    cards_player1_Kan.append(cards_player3_discard.pop())
                if LastP == 4:
                    cards_player1_Kan.append(cards_player4_discard.pop())
                GetCard(1)
                discard(1)
                NextP = 2
            elif decideKan == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: card not found")
                print(Style.RESET_ALL)
                want_Kan()

        elif CanKan1N:
            decideKan = str(input("P1,which do you want to Kan " + str(CanKan1N) + " ? (or 'skip') "))
            if decideKan != "skip" and (decideKan in CanKan1N):
                syncHandDecks()
                cards_player1_Kan.append(cards_player1.pop(HandDeck1.index(decideKan)))
                cards_player1_Kan.append(cards_player1.pop(HandDeck1.index(decideKan)))
                cards_player1_Kan.append(cards_player1.pop(HandDeck1.index(decideKan)))
                cards_player1_Kan.append(cards_player1.pop(HandDeck1.index(decideKan)))
                GetCard(1)
                discard(1)
                NextP = 2
            elif decideKan == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: card not found")
                print(Style.RESET_ALL)
                want_Kan()

    if CanKan2 != [] and LastP != 2 and ((LastCard in CanKan2) or CanKan2N != []):
        if LastCard in CanKan2:
            decideKan = str(input("P2,which do you want to Kan " + LastCard + " ? (or 'skip') "))
            if decideKan != "skip" and (decideKan in CanKan2):
                syncHandDecks()
                cards_player2_Kan.append(cards_player2.pop(HandDeck2.index(decideKan)))
                cards_player2_Kan.append(cards_player2.pop(HandDeck2.index(decideKan)))
                cards_player2_Kan.append(cards_player2.pop(HandDeck2.index(decideKan)))
                cards_player2_Kan.append(cards_player2_discard.pop())
                if LastP == 1:
                    cards_player2_Kan.append(cards_player1_discard.pop())
                if LastP == 3:
                    cards_player2_Kan.append(cards_player3_discard.pop())
                if LastP == 4:
                    cards_player2_Kan.append(cards_player4_discard.pop())
                GetCard(2)
                discard(2)
                NextP = 3
            elif decideKan == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: card not found")
                print(Style.RESET_ALL)
                want_Kan()

        elif CanKan2N:
            decideKan = str(input("P2,which do you want to Kan " + str(CanKan2N) + " ? (or 'skip') "))
            if decideKan != "skip" and (decideKan in CanKan2N):
                syncHandDecks()
                cards_player2_Kan.append(cards_player2.pop(HandDeck2.index(decideKan)))
                cards_player2_Kan.append(cards_player2.pop(HandDeck2.index(decideKan)))
                cards_player2_Kan.append(cards_player2.pop(HandDeck2.index(decideKan)))
                cards_player2_Kan.append(cards_player2.pop(HandDeck2.index(decideKan)))
                GetCard(2)
                discard(2)
                NextP = 3
            elif decideKan == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: card not found")
                print(Style.RESET_ALL)
                want_Kan()

    if CanKan3 != [] and LastP != 3 and ((LastCard in CanKan3) or CanKan3N != []):
        if LastCard in CanKan3:
            decideKan = str(input("P3,which do you want to Kan " + LastCard + " ? (or 'skip') "))
            if decideKan != "skip" and (decideKan in CanKan3):
                syncHandDecks()
                cards_player3_Kan.append(cards_player3.pop(HandDeck3.index(decideKan)))
                cards_player3_Kan.append(cards_player3.pop(HandDeck3.index(decideKan)))
                cards_player3_Kan.append(cards_player3.pop(HandDeck3.index(decideKan)))
                cards_player3_Kan.append(cards_player3_discard.pop())
                if LastP == 1:
                    cards_player3_Kan.append(cards_player1_discard.pop())
                if LastP == 2:
                    cards_player3_Kan.append(cards_player2_discard.pop())
                if LastP == 4:
                    cards_player3_Kan.append(cards_player4_discard.pop())
                GetCard(3)
                discard(3)
                NextP = 4
            elif decideKan == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: card not found")
                print(Style.RESET_ALL)
                want_Kan()

        elif CanKan3N:
            decideKan = str(input("P3,which do you want to Kan " + str(CanKan3N) + " ? (or 'skip') "))
            if decideKan != "skip" and (decideKan in CanKan3N):
                syncHandDecks()
                cards_player3_Kan.append(cards_player3.pop(HandDeck3.index(decideKan)))
                cards_player3_Kan.append(cards_player3.pop(HandDeck3.index(decideKan)))
                cards_player3_Kan.append(cards_player3.pop(HandDeck3.index(decideKan)))
                cards_player3_Kan.append(cards_player3.pop(HandDeck3.index(decideKan)))
                GetCard(3)
                discard(3)
                NextP = 4
            elif decideKan == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: card not found")
                print(Style.RESET_ALL)
                want_Kan()

    if CanKan4 != [] and LastP != 4 and ((LastCard in CanKan4) or CanKan4N != []):
        if LastCard in CanKan4:
            decideKan = str(input("P4,which do you want to Kan " + LastCard + " ? (or 'skip') "))
            if decideKan != "skip" and (decideKan in CanKan4):
                syncHandDecks()
                cards_player4_Kan.append(cards_player4.pop(HandDeck4.index(decideKan)))
                cards_player4_Kan.append(cards_player4.pop(HandDeck4.index(decideKan)))
                cards_player4_Kan.append(cards_player4.pop(HandDeck4.index(decideKan)))
                cards_player4_Kan.append(cards_player4_discard.pop())
                if LastP == 1:
                    cards_player4_Kan.append(cards_player1_discard.pop())
                if LastP == 2:
                    cards_player4_Kan.append(cards_player2_discard.pop())
                if LastP == 3:
                    cards_player4_Kan.append(cards_player3_discard.pop())
                GetCard(4)
                discard(4)
                NextP = 1
            elif decideKan == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: card not found")
                print(Style.RESET_ALL)
                want_Kan()

        elif CanKan4N:
            decideKan = str(input("P4,which do you want to Kan " + str(CanKan4N) + " ? (or 'skip') "))
            if decideKan != "skip" and (decideKan in CanKan4N):
                syncHandDecks()
                cards_player4_Kan.append(cards_player4.pop(HandDeck4.index(decideKan)))
                cards_player4_Kan.append(cards_player4.pop(HandDeck4.index(decideKan)))
                cards_player4_Kan.append(cards_player4.pop(HandDeck4.index(decideKan)))
                cards_player4_Kan.append(cards_player4.pop(HandDeck4.index(decideKan)))
                GetCard(4)
                discard(4)
                NextP = 1
            elif decideKan == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: card not found")
                print(Style.RESET_ALL)
                want_Kan()


def SimpleWinCheck():
    Rank = []
    if not cards_mountain:
        Rank.append(len(cards_player1))
        Rank.append(len(cards_player2))
        Rank.append(len(cards_player3))
        Rank.append(len(cards_player4))
        Rank.sort()
        print(Fore.LIGHTGREEN_EX + "The rank is: " + str(Rank))
        print(Style.RESET_ALL)
        sleep(0.2)
        os.system("clear")
        if Rank[0] == len(cards_player1):
            print(Fore.LIGHTRED_EX + "Player 1 wins!")
            print(Style.RESET_ALL)
            sleep(0.2)
            os.system("clear")
        if Rank[0] == len(cards_player2):
            print(Fore.LIGHTRED_EX + "Player 2 wins!")
            print(Style.RESET_ALL)
            sleep(0.2)
            os.system("clear")
        if Rank[0] == len(cards_player3):
            print(Fore.LIGHTRED_EX + "Player 3 wins!")
            print(Style.RESET_ALL)
            sleep(0.2)
            os.system("clear")
        if Rank[0] == len(cards_player4):
            print(Fore.LIGHTRED_EX + "Player 4 wins!")
            print(Style.RESET_ALL)
            sleep(0.2)
            os.system("clear")
        quit()
    elif cards_mountain:
        syncHandDecks()
        if len(set(HandDeck1)) == len(HandDeck1):
            print(Fore.LIGHTRED_EX + "Player 1 wins!")
            print(Style.RESET_ALL)
            sleep(0.2)
            os.system("clear")
            quit()
        if len(set(HandDeck2)) == len(HandDeck2):
            print(Fore.LIGHTRED_EX + "Player 2 wins!")
            print(Style.RESET_ALL)
            sleep(0.2)
            os.system("clear")
            quit()
        if len(set(HandDeck3)) == len(HandDeck3):
            print(Fore.LIGHTRED_EX + "Player 3 wins!")
            print(Style.RESET_ALL)
            sleep(0.2)
            os.system("clear")
            quit()
        if len(set(HandDeck4)) == len(HandDeck4):
            print(Fore.LIGHTRED_EX + "Player 4 wins!")
            print(Style.RESET_ALL)
            sleep(0.2)
            os.system("clear")
            quit()
        if (LastCard in HandDeck1) and (LastP != 1):
            P1Decide = str(input("P1, do you want to Ron? (Ron/skip)"))
            if P1Decide == "Ron":
                print(Fore.LIGHTRED_EX + "Player 1 wins!")
                print(Fore.LIGHTRED_EX + str(LastP) + " Defeated!")
                print(Style.RESET_ALL)
                sleep(0.2)
                os.system("clear")
                quit()
            if P1Decide == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: invalid input")
                print(Style.RESET_ALL)
                sleep(0.2)
                os.system("clear")
                SimpleWinCheck()

        if (LastCard in HandDeck2) and (LastP != 2):
            P2Decide = str(input("P2, do you want to Ron? (Ron/skip)"))
            if P2Decide == "Ron":
                print(Fore.LIGHTRED_EX + "Player 2 wins!")
                print(Fore.LIGHTRED_EX + str(LastP) + " Defeated!")
                print(Style.RESET_ALL)
                sleep(0.2)
                os.system("clear")
                quit()
            if P2Decide == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: invalid input")
                print(Style.RESET_ALL)
                sleep(0.2)
                os.system("clear")
                SimpleWinCheck()

        if (LastCard in HandDeck3) and (LastP != 3):
            P3Decide = str(input("P3, do you want to Ron? (Ron/skip)"))
            if P3Decide == "Ron":
                print(Fore.LIGHTRED_EX + "Player 3 wins!")
                print(Fore.LIGHTRED_EX + str(LastP) + " Defeated!")
                print(Style.RESET_ALL)
                sleep(0.2)
                os.system("clear")
                quit()
            if P3Decide == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: invalid input")
                print(Style.RESET_ALL)
                sleep(0.2)
                os.system("clear")
                SimpleWinCheck()

        if (LastCard in HandDeck4) and (LastP != 4):
            P4Decide = str(input("P4, do you want to Ron? (Ron/skip)"))
            if P4Decide == "Ron":
                print(Fore.LIGHTRED_EX + "Player 4 wins!")
                print(Fore.LIGHTRED_EX + str(LastP) + " Defeated!")
                print(Style.RESET_ALL)
                sleep(0.2)
                os.system("clear")
                quit()
            if P4Decide == "skip":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Error: invalid input")
                print(Style.RESET_ALL)
                sleep(0.2)
                os.system("clear")
                SimpleWinCheck()


# functions list:
# 1. move_shuffle()
# 2. assign_winds()
# 3. assign_cards()
# 4. sort_cards()
# 5. display_cards(player)
# 6. GetCard(player)
# 7. discard(player)
# 8. CHK_pon()
# 9. want_Pon()

move_shuffle()
assign_winds()
assign_cards()
sort_cards()

while cards_mountain:
    syncHandDecks()
    GetCard(NextP)
    syncHandDecks()
    discard(NextP)
    syncHandDecks()
    CHK_kan()
    syncHandDecks()
    want_Kan()
    syncHandDecks()
    CHK_pon()
    syncHandDecks()
    want_Pon()
    syncHandDecks()
    SimpleWinCheck()
SimpleWinCheck()