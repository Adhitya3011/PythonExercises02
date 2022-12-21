def find_prefix(string1,string2):
    pos_list = []
    word_list = []
    for i in string1:
        for pos in range(len(string2)-1):
            if i == string2[pos]:
                word_list.append(i)
                pos_list.append(pos)
                break
    
    
    
    pref = ''.join(word_list)
    print(pref)

find_prefix("footb","football")