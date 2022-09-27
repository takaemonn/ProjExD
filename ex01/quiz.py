import random

def shutudai(q_list):
    ques = random.choice(q_list)
    print('問題：'+ques["q"])
    return ques["a"]

def kaito(ans_list):
    ans = input("答えるんだ")
    if ans in ans_list:
        print("正解")
    else:
        print("不正解")

if __name__ == "__main__":
    q_list = [
        {"q":"Which is stronger,Thursday or Saturday?", "a":["Saturday","saturday"]},
        {"q":"What begins with T, finishes with T, and has T in it?", "a":["Teapot", "teapot"]},
        {"q":"Which letter of the alphabet has the most water?","a":["C", "c"]}
        ]
    ans_list = shutudai(q_list)
    kaito(ans_list)