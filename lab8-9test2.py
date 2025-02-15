a = input().split()
if len(a) > 1:
    a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
    a[len(a) - 1] = a[len(a) - 1].lower()
    a[0] = a[0].capitalize()
    sentence = ' '.join(a)
    print(sentence)
else:
    print("Не получится поменять(")