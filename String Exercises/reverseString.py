def reverse(string):
    temp_list = []
    for i in range(1,len(string)+1):
        temp_list.append(string[-i])

    print(str(temp_list))
    ans = ''.join(temp_list)
    print(ans)

reverse("abcdefg")

