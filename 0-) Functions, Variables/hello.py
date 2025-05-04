def main():
    name = input("What's your name? ")
    hello(name)

    hello()
    

def hello(to="world"):
    print("hello,", to)

main()