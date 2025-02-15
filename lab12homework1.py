N = int(input("Введите количество стран: "))
country_map = {}
for _ in range(N):
    data = input().split()
    country = data[0]
    cities = data[1:]
    for city in cities:
        country_map[city] = country

M = int(input("Введите количество запросов: "))
for _ in range(M):
    query_city = input().strip()
    if query_city in country_map:
        print(country_map[query_city])
    else:
        print("Город не найден")
