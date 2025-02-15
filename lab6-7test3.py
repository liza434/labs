a = input()
cnt1 = 0
cnt2 = 0
for i in a:
    if i == "ф":
        cnt1 += 1
    if i == 'я':
        cnt2 += 1
print("Букв ф:", cnt1)
print("Букв я:", cnt1)