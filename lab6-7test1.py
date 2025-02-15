name = input("Введите ваше имя: ")
if name:  
    last_letter = name[-1] 
    print("Последняя буква в верхнем регистре:", last_letter.upper())
else:
    print("Вы не ввели имя.")