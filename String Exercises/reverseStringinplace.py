def rev(string):
    l = len(string)
    for i in range(l-1):
        temp = string[i]
        string[i] = string[l-i-1]
        str[l-i-1] = temp

rev("ABC")