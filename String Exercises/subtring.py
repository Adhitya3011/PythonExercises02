def substr(string1, string2):
    pos_list = []
    for letter in string1:
        for position in range(len(string2)-1):
            if letter == string2[position]:
                pos_list.append(position)
                break

    print(pos_list)

    for i in range(len(pos_list)-1):
        if (pos_list[i+1] - pos_list[i]) > 1:
            print("Not a substring.")

        else:
            print("It is a substring.")


substr('ac', 'abcd')


