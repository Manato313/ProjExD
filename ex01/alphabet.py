
import random
import datetime

all_alphabet = 26
line_alphabet = 10
del_alphabet = 2
challenge = 2

def out_q(alphabet):
    all_chr = random.sample(alphabet, line_alphabet)
    for c in sorted(all_chr):
        print("対象：",end=" ")
    print()

    delet = random.sample(all_chr,line_alphabet)
    print("表示文字列:",end="")
    for i in all_chr:
        if i not in delet:
            print(i,end=" ")
    print()
    return delet

def ans(anser):
    num = int(input("無くなった文字はいくつ？＝＞"))
    if num != del_alphabet:
        print("ちゃうよ")
    else:
        print("正解！んじゃぁ…何が消えとる？1個ずつ教えてくれや。")
        for i in range(num):
            a = input(f"{i+1}文字目教えてくれや！＝＞")
            if c not in anser:
                print("んぁ～ちゃうな！ドンマイ！")
                return False
            else:
                anser.remove(c)
        else:
            print("お！すごいやん兄ちゃん！完ペキやで！")
            return True
        return False

    if __name__ == "__main__":
        alphabet = [chr(i+65) for i in range(all_alphabet)]
        for _ in range(challenge):
            Delete = out_q(alphabet)
            ret = ans(Delete)
            if ret:
                break
            else:
                print("*"*20)