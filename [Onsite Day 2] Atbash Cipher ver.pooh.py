"""[Onsite Day 2] Atbash Cipher"""
def main():
    """defind list"""
    list_word = []
    list_bigword = []
    word = ""
    norm = "abcdefghijklmnopqrstuvwxyz"
    upnorm = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for infor in norm:
        list_word.append(infor)
    for game in upnorm:
        list_bigword.append(game)
    rever = list_word[::-1]
    uprever = list_bigword[::-1]
    get = input()
    for xmen in get:
        if xmen.islower():
            dream = list_word.index(xmen)
            word += rever[dream]
        elif xmen.isupper():
            zebra = list_bigword.index(xmen)
            word += uprever[zebra]
        else:
            word += xmen
    print(word)
main()
