def simple_compress(s):
    if not s:  
        return ""
    
    compressed = ""
    count = 1
    
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1]  
            if count > 1:
                compressed += str(count)  
            count = 1  
    
    return compressed

user_input = input("Введите строку: ")
result = simple_compress(user_input)
print("Результат архивации:", result)