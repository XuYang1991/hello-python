s = input()
input_list = list(s)
dic = {}
for char in input_list:
    dic[char] = dic.get(char, 0) + 1
sorted_list = sorted(dic.items(), key=lambda item: item[1], reverse=True)
count = 0
for i in sorted_list:
    if count != 3:
        key, value = i
        print(key + " " + str(value))
        count += 1