print("(1) if文の使い方")

point = 55
if point > 80:
    print("優秀")
elif point > 60:
    print("合格")
else:
    print("不合格")

print("--------------------------------")

print("(2) for文の使い方")

#文字を上から一文字づつ変数として渡して表示している
for name in "俺は左馬刻様だ": #pythonは''も""変わらない
    print(name)

print("--------------------------------")

#range関数で指定回数繰り返している
for i in range(1,6):
    print(i)
print("--------------------------------")

print("(3) if文とfor文を混ぜてみた")

#range関数で1から10までを出力し、if分とfor文で3の倍数と5の倍数を表示するプログラム

for i in range(1, 11):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print(i)