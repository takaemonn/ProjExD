import random
import datetime

num_alph = 26
num_all_chars = 10
num_abs_chars = 2
num_try = 2

def shutudai(alph):
    all_chars = random.sample(alph, num_all_chars)
    print("対象文字：" ,end="")
    for c in sorted(all_chars):
        print(c,end="")
    print()


    abs_chars = random.sample(all_chars, num_abs_chars)
    print("表示文字：" ,end="")
    for c in all_chars:
        if c not in abs_chars:
            print(c,end="")
    print()

    print("欠損文字：", abs_chars)
    return abs_chars


def kaito(seikai):
    ans = int(input("欠損文字はいくつあるでしょうか？:"))
    if ans !=  num_abs_chars:
        print("不正解")

    else:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(ans):
            c = input(f"{i+1}文字目を入力してください：")
            if c not in seikai:
                print("不正解です。")
                return False
            else:
                seikai.remove(c)
        else:
            print("欠損文字を含めてパーフェクト正解です")
            return True
    return False
            

if __name__ == "__main__":
    alph = [chr(i+65) for i in range(num_alph)]
    for _ in range(num_try):
        abs_chars = shutudai(alph)
        ret = kaito(abs_chars)
        if ret:
            break
        else:
            print("-"*20)