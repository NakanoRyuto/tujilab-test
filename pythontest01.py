print("(1)")

n = 123
if n % 2 == 0:
    res = "偶数です"
else:
    res = "奇数です"
print(str(n) + "は" + res)

print("-----------------------------------------------")

print("(2)")

n = 15
if 10 <= n and n <= 20:
        print(str(n) + "は範囲内です")
else:
        print(str(n) + "は範囲外です")
print("-----------------------------------------------")

print("(3)")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
#totalはforの中で使う変数なので指定しておく。
total = 0
for n  in data:
    total += n
ave = total // len(data)

msg = "合計 = " + str(total) + " 平均 = " + str(ave)
print(msg)
print("-----------------------------------------------")
    