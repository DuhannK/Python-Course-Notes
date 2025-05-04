emoticon = "w.w"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
