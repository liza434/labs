b = []
spisok = input().split()
print(spisok)
b.append(spisok[len(spisok) // 2])
b = ''.join(b)
spisok.pop(len(spisok) // 2)
print(spisok)
spisok.insert(len(spisok) // 2, b)
print(spisok)