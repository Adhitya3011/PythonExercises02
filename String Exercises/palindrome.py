def check_pal(string):
    count = 0
    for i in range(len(string)):
        if string[i] == string[-(i+1)]:
            count += 1
            

    print(count)
    if count == len(string):
        print("Given string is a palindrome")
    else:
        print("Not a palindrome")

check_pal('ababaa')
