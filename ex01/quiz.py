from decimal import ROUND_DOWN
import random
from traceback import print_tb

q1 = "カービィという名前が付く前、カービィはなんという名前だった？"
q2 = "メタナイトの飛行戦艦の名称は？"
q3 = "伝説のエアライドマシン、ドラグーンともう一つは？"
a1 = ["ポポポ","ティンクルポポ","ぽぽぽ"]
a2 = ["ハルバード","戦艦ハルバード","いつも墜落するやつ"]
a3 = ["ハイドラ"]

qa_dic = {q1:a1,q2:a2,q3:a3}

qes = random.choice(list(qa_dic.keys()))

print(qes)
ans = (input("答え入力=>"))

if ans in qa_dic[qes]:
    print ("正解！")
else:
    print("不正解！")
