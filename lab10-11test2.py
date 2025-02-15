hitrity = input("Введите фамилии за хитрость: ").split()
zhadnost = input("Введите фамилии за жадность: ").split()
set_hitrity = set(hitrity)
set_zhadnost = set(zhadnost)
exclusive_hitrity = set_hitrity - set_zhadnost
exclusive_zhadnost = set_zhadnost - set_hitrity
count_exclusive = len(exclusive_hitrity) + len(exclusive_zhadnost)
print("Количество людей, получивших строго одну надбавку:", count_exclusive)
