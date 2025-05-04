
import random
import time
import sys
import pyfiglet

username = None

def main():
    print(pyfiglet.figlet_format("Hello This is My Project! \n", font="slant"))
    global username
    username = input("What's your user name: ")
    print(f"\nHi {username}, you will play this UNO game with 3 bots, Good luck!")
    while True:
        start = str(input('Select "1" to start, "q" to exit. '))
        if start == "1":
            print(pyfiglet.figlet_format("\nGooo!", font="speed"))
            return initialize_deck()

        elif start == "q":
            break

        else:
            print("You entered it wrong!")

user = []
bot1 = []
bot2 = []
bot3 = []

#desteyi başlatma
def initialize_deck():
    global user, bot1, bot2, bot3
    user = deal_hands()
    bot1 = deal_hands()
    bot2 = deal_hands()
    bot3 = deal_hands()
    play_turn(user, bot1, bot2, bot3)


#all cards / global
cards = [
"🟦0", "🟦0", "🟦1", "🟦1", "🟦2", "🟦2", "🟦3", "🟦3", "🟦4", "🟦4", "🟦5", "🟦5", "🟦6", "🟦6", "🟦7", "🟦7", "🟦8", "🟦8", "🟦9", "🟦9",
"🟦Skip", "🟦Skip", "🟦Reverse", "🟦Reverse", "🟦Draw Two", "🟦Draw Two",
"🟥0", "🟥0", "🟥1", "🟥1", "🟥2", "🟥2", "🟥3", "🟥3", "🟥4", "🟥4", "🟥5", "🟥5", "🟥6", "🟥6", "🟥7", "🟥7", "🟥8", "🟥8", "🟥9", "🟥9",
"🟥Skip", "🟥Skip", "🟥Reverse", "🟥Reverse", "🟥Draw Two", "🟥Draw Two",
"🟨0", "🟨0", "🟨1", "🟨1", "🟨2", "🟨2", "🟨3", "🟨3", "🟨4", "🟨4", "🟨5", "🟨5", "🟨6", "🟨6", "🟨7", "🟨7", "🟨8", "🟨8", "🟨9", "🟨9",
"🟨Skip", "🟨Skip", "🟨Reverse", "🟨Reverse", "🟨Draw Two", "🟨Draw Two",
"🟩0", "🟩0", "🟩1", "🟩1", "🟩2", "🟩2", "🟩3", "🟩3", "🟩4", "🟩4", "🟩5", "🟩5", "🟩6", "🟩6", "🟩7", "🟩7", "🟩8", "🟩8", "🟩9", "🟩9",
"🟩Skip", "🟩Skip", "🟩Reverse", "🟩Reverse", "🟩Draw Two", "🟩Draw Two",
"⬛Wild", "⬛Wild", "⬛Wild", "⬛Wild", "⬛Wild Draw Four", "⬛Wild Draw Four", "⬛Wild Draw Four", "⬛Wild Draw Four"
]

#elleri dağıt
def deal_hands():
    random.shuffle(cards)
    return [cards.pop() for _ in range(7)]


#sırayı oyna
def play_turn(user, bot1, bot2, bot3):
    now_player = 0
    next_player = 1
    skip_player = 0
    queue = [user, bot1, bot2, bot3]
    top_card = cards.pop()
    print(f"\n {top_card} first card ")
    while True:

        if now_player == 0:
            try:
                select, play_card, next_color = choose_card_from_hand(queue[now_player], top_card)
            except:
                print("Invalid choice! You selected a number beyond your available cards.")
                select, play_card, next_color = choose_card_from_hand(queue[now_player], top_card)
        else:
            select, play_card, next_color = choose_card_from_bot(queue[now_player], top_card)

        if play_card == True:
            if "⬛" in select:
                top_card = next_color
                print(select)
            else:
                top_card = select
            print(top_card)
            next_player_x, skip_player = apply_card_effect(select, now_player, next_player)
            next_player *= next_player_x
            queue[now_player].remove(select)
            check_winner(user, bot1, bot2, bot3)
            time.sleep(1)

        #Sıranın doğru ilerlemesi / Correct progression of the sequence
        if now_player == 3 and next_player == 1 and skip_player == 0:
            now_player = 0
        elif now_player == 0 and next_player == -1 and skip_player == 0:
            now_player = 3
        elif skip_player == 0:
            now_player += next_player

        if now_player == 3 and next_player == 1 and skip_player == 1:
            now_player = 1
        elif now_player == 0 and next_player == -1 and skip_player == 1:
            now_player = 2
        elif now_player == 2 and next_player == 1 and skip_player == 1:
            now_player = 0
        elif now_player == 1 and next_player == -1 and skip_player == 1:
            now_player = 3
        elif skip_player == 1:
            now_player += next_player + next_player


#bot kart seçme
def choose_card_from_bot(bot, top_card):
    for i in range(len(bot)):
        if bot[i][0] in top_card or bot[i][1:] in top_card:
            return bot[i], True, "not_black"
    for i in range(len(bot)):   #siyah kartı seç > botta olan kartı iste(siyah harici) / select black card > request card from bot(non-black)
        if "⬛" in bot[i]:
            for j in range(len(bot)):
                if bot[j][0] in "🟦🟥🟨🟩":
                    return bot[i], True, bot[j][0]
            return bot[i], True, random.choice("🟦🟥🟨🟩")
    bot.append(cards.pop())
    print(f"bot drew card!")
    return "", False, "not_black"


#elindeki kartlardan seçme
def choose_card_from_hand(hand, top_card):
    colors = ["🟦","🟥","🟨","🟩"]
    while True:
        print("0.(Draw a card), ", end="")
        for i in range(len(hand)):
            print(f"{i+1}.({hand[i]})", end=", ")
        select = int(input("\nSelect card: ")) -1
        if select == -1:
            user.append(cards.pop())
            print(f"I drew a card!")
            return "", False, "not_black"
        else:
            playable = is_playable(hand[select], top_card)
            if playable == True:
                if "⬛" in hand[select]:     #siyah kart ise > sadece seçilen rengi 🟦🟥🟨🟩 geri döndür / if black card > return only the selected color 🟦🟥🟨🟩
                    color_number = int(input("Choose your next color! 1.(🟦) 2.(🟥) 3.(🟨) 4.(🟩) : "))
                    return hand[select], True, colors[color_number-1]
                return hand[select], True, "not_black"



#kart oynanabilir mi?
def is_playable(select, top_card):
    if "⬛" in select:
        return True
    elif select[0] in top_card or select[1:] in top_card:
        return True
    else:
        print("This card cannot be played!")
        return False


#kart etkisini uygula
def apply_card_effect(select, now_player, next_player):
    queue = [user, bot1, bot2, bot3]
    if now_player == 3 and next_player == 1:
            now_player = -1
    if now_player == 0 and next_player == -1:
            now_player = 3
    else:
        now_player += next_player

    if "Reverse" in select:
        print("The direction is reversed.")
        return -1, 0

    elif "Draw Two" in select:
        print(f"The next player drew 2 cards.")
        queue[now_player] += [cards.pop() for _ in range(2)]
        return 1, 0

    elif "Skip" in select:
        if now_player == 0:
            print("You've been skipped.")
        print("The next player was skipped")
        return 1, 1

    elif "Wild Draw Four" in select:
        print(f"The next player drew 4 cards.")
        queue[now_player] += [cards.pop() for _ in range(4)]
        return 1, 0
    return 1, 0


#kazanını kontrol et
def check_winner(user, bot1, bot2, bot3):
    if user == []:
        print(pyfiglet.figlet_format(f"{username} is Won!", font="slant"))
        sys.exit()

    elif bot1 == []:
        print(pyfiglet.figlet_format("Bot1 is Won!", font="slant"))
        sys.exit()

    elif bot2 == []:
        print(pyfiglet.figlet_format("Bot2 is Won!", font="slant"))
        sys.exit()

    elif bot3 == []:
        print(pyfiglet.figlet_format("Bot3 is Won!", font="slant"))
        sys.exit()



if __name__ == "__main__":
    main()
