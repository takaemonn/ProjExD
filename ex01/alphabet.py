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
    abs_chars = random.sanple(alph, num_abs_chars)
    print("表示文字：" ,end="")
    for c in sorted(abs_chars):
        if c not in abs_chars:
            print(c,end="")
    print()
    print("欠損文字：", abs_chars)


def kaito():
    pass

if __name__ == "__main__":
    alph = [chr(i+65) for i in range(num_alph)]
    shutudai(alph)