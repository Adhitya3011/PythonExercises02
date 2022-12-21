def find_prefix(string1,string2):
    pos_list = []
    word_list = []
    for i in string1:
        for pos in range(len(string2)-1):
            if i == string2[pos]:
                word_list.append(i)
                pos_list.append(pos)
                break
    
    for i in range(len(pos_list)-1):
        if (pos_list[i+1] - pos_list[i]) > 1:
            print("Not a substring.")
            
        else:
            if word_list[0] != string2[0]:
                print("No prefix Found!")
            else:
                pref = ''.join(word_list)
                print(pref)

find_prefix("ftb","football")

    


