def revSent(string):
    temp_list = string.split()
    final_list = [temp_list[-i] for i in range(1,len(temp_list)+1)]
    
    print(' '.join(final_list))

revSent('The map is blue')
    
