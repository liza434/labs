input_str = input()
words = input_str.split()
output = [words[i][::-1] if i % 2 == 1 else words[i] for i in range(len(words))]
print(output)