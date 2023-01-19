from art import logo
from random import randint
import time
import os

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    user = [cards[randint(0, len(cards) - 1)], cards[randint(0, len(cards) - 1)]]
    dealer = [cards[randint(0, len(cards) - 1)]]
    user_total = user[0] + user[1]
    dealer_total = dealer[0]
    print(f"Your Hand: {user}\nYour Total: {user_total}\n")
    print(f"Dealer's Hand: {dealer}\nDealer's Total: {dealer_total}\n")
    keep_playing = True
    user_turn = True
    while keep_playing:
        if user_turn:
            hit = input('Do You Want Another Card? Type "hit me" Or "pass": ')
            if hit == "hit me":
                new_card = cards[randint(0, len(cards) - 1)]
                user.append(new_card)
                user_total += new_card
                if user_total > 21:
                    if 11 in user:
                        user[user.index(11)] = 1
                        user_total -= 10
                    else:
                        print("\nBUST!!!\n")
                        keep_playing = False
                print(f"Your Hand: {user}\nYour Total: {user_total}\n")
            else:
                user_turn = False
        else:
            new_card = cards[randint(0, len(cards) - 1)]
            dealer.append(new_card)
            dealer_total += new_card
            print(f"Dealer's Hand: {dealer}\nDealer's Total: {dealer_total}\n")
            if dealer_total >= 17 and dealer_total <= 21:
                if user_total > dealer_total:
                    print("You Win!!!")
                elif user_total == dealer_total:
                    print("Draw :/")
                else:
                    print("Bad Luck This Time Around... You Lose :(")
                keep_playing = False
            elif dealer_total > 21:
                if 11 in dealer:
                    dealer[dealer.index(11)] = 1
                    dealer_total -= 10
                else:
                    print("The Dealer Bust! You Win!!!\n")
                    keep_playing = False
            time.sleep(1.75)
    if input("Do You Want To Play Again?: ") == "yes":
        blackjack()


blackjack()
