# MahjongKaze
## _Easy to learn Mahjong minigame_
*[Github](https://github.com/TabunKaze03/MahjongKaze)*

MahjongKaze is a Japanese-style Mahjong minigame that does not require complex and annoying rules.

- Easy to Understand
- Clean(?) Interface (Literally console)
- Will exit itself when you lose/win


## Installation
Before playing MahjongKaze, a Python library needs to be installed in the Python environment.
- colorama

You may install the library by using the pip command in Python package:
```sh
pip install colorama
```
After installing the library, you are good to run the code.
## Game Rules
There are in total 176 Cards(Tiles) in this game:

| Type (Display in-game) | Value |
| ------ | ------ |
| Character (Char) | 1 - 9 |
| Dot (Dot) | 1 - 9 |
| Bamboo (Bamboo) | 1 - 9 |
| White Dragon (White) | None |
| Green Dragon (Rich) | None |
| Red Dragon (Middle) | None |
| East (East) | None |
| South (South) | None |
| West (West) | None |
| North (North) | None |

At the start, each player will be assigned 13 random cards as their HandDeck. The round then loops in the order of 
P1 -> P2 -> P3 -> P4 (In normal situation)

In your round, you will be assigned a new card taken randomly from the "Card Mountain", which consists of all the other cards in the game. Then, you will be asked to discard one card from your HandDeck (It can be the card you just got)

Your goal is to minimize the cards in your hand as much as possible by "Pon" and "Kan", which will be introduced next. 
## Pon

When you have two same cards in your HandDeck like this:
```sh
HAND DECK OF PLAYER 1: ['char2', 'char3', 'char5', 'char6', 'dot5', 'dot6', 'dot9', 'bamboo2', 'bamboo3', 'bamboo7', 'bamboo8', 'bamboo9', 'bamboo9', 'rich']
```
(In this HandDeck, You have two "Bamboo9")

If the previous player discarded a Bamboo9, you can choose "Pon" when the system asks you:
```sh
P1,which do you want to Pon bamboo9 ? (or 'skip') 
```
If you want to Pon, type the card you want to Pon:
```sh
bamboo9
```
After you Pon, those three cards (two in your hand + one from another player) will be placed in your "Pon zone", treat them as the cards discarded as they cannot be moved or involved in future gameplay.

After you Pon, you need to discard another card from your HandDeck.

If you want to Kan instead(see next section), you may type "skip" to continue the round without disturbing the order of gameplay.
```sh
skip
```

## Kan(1)

Kan is similar to Pon, but with higher priority than Pon:

When you have three same cards in your HandDeck like this:
```sh
HAND DECK OF PLAYER 1: ['char1', 'char3', 'char4', 'char6', 'dot5', 'dot6', 'dot9', 'bamboo2', 'bamboo3', 'bamboo7', 'bamboo8', 'bamboo8', 'bamboo8', 'rich']
```
(In this HandDeck, you have three "Bamboo8")



If the previouse player discarded a Bamboo8, you can choose "Kan" when the system asks you:
```sh
P1,which do you want to Kan bamboo8 ? (or 'skip') 
```
If you want to Kan, type the card you want to Kan:
```sh
Bamboo8
```
After you Kan, those four cards (three in your hand + one from another player) will be placed in your "Kan zone", treat them as the cards discarded as they cannot be moved or involved in future gameplay.

After you Kan, you will be assigned a new card from Cardmountain and asked to discard one card after it.

It is strongly suggested that you should Kan whenever you can because keeping them in your hand is meaningless, but if you have any special strategy, use "skip" to continue without Kan.
```sh
skip
```

## Kan(2)

There is another type of Kan, which you can do when you have four same cards in your hand.
Unlike the previous one, when you have four same cards in your HandDeck, you can only Kan when it is your round:
```sh
HAND DECK OF PLAYER 1: ['char1', 'char3', 'char4', 'char6', 'dot5', 'dot6', 'dot9', 'bamboo2', 'bamboo3', 'bamboo7', 'rich', 'rich', 'rich', 'rich']
```
(In this HandDeck, you have four “Rich”)

When it is your round, before the system assigns you a card, you will be asked:
```sh
P1,which do you want to self Kan Rich ? (or 'skip') 
```

If you want to self Kan, type the card you want to Kan:
```sh
Rich
```
After you self Kan, those four cards all in your HandDeck will be placed in your “Kan zone”, treat them as the cards discarded as they cannot be moved or involved in future gameplay.

After you self Kan, you will be assigned a new card from Cardmountain and asked to discard one card after it.

It is strongly suggested that you should self Kan whenever you can because keeping them in your hand is meaningless, but if you have any special strategy, use “skip” to continue without Kan.
```sh
skip
```

## Goal

Your goal is to Pon or Kan as much as possible to get rid of cards in your HandDeck. When you have only one card in your HandDeck, you will need to wait for the last same card either be discarded from others(Ron) or assigned to you in your round(Zumo).

Example:
```sh
HAND DECK OF PLAYER 1: ['char1']
```
The card you want to look for is char1 from others or assigned by system in your round.

## Card Mountain is empty

When Card Mountain is empty, it usually means players are holding cards that others want, and there are simply no more cards to be assigned by system.

System will then check how many cards left in each of the players' HandDeck, the player with the shortest HandDeck wins the round.


## Special rule
In this situation:
```sh
HAND DECK OF PLAYER 1: ['Char1', 'Char2', 'Middle', 'Middle']
HAND DECK OF PLAYER 2: ['Char1', 'Char2', 'Char3', 'Middle']
HAND DECK OF PLAYER 3: ['Middle']
HAND DECK OF PLAYER 4: ['Rich']
```
When Player 2 discards Middle, Player 1 has a chance to Pon, and Player 4 has a chance to Ron(Win).

- Player 1 may not Pon because Ron(Win) have a higher priority than Pon

## Hint

Each of the card consist of four, so check the discarded card from others to make sure there might have cards left in the Card mountain or in others HandDeck instead of Discarded which you can't win with them.

## Who made this?

Hey, It's the creator of MahjongKaze speaking here, name is TabunKaze, this is my first python project in this scale.
I am still trying to add more functions to make this Mahjong game complete (Standard Rule)
Please follow my Github to get more updates!









