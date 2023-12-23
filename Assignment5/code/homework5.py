def ord_prefixspan(filename,min_sup):
    with open(filename) as file:
        SDB=[line.rstrip('\n').split(',')[1][2:-1] for line in file]     #This is to read the file and store the data in a list
    answer=recursion_to_get_patterns('',SDB,min_sup)
    return answer

def recursion_to_get_patterns(prefix, PDB, min_sup):
    Patterns={}     #This is the dictionary that will be returned
    frequency_for_each_item={}             #This is the dictionary that will be used to count the frequency of each item
    frequency_after_sorted={}      #This is the dictionary that will be used to store the items that have frequency greater than or equal to min_sup
    patterns_after_delete_element_less_than_threshold={}           #This is the dictionary that will be used to store the items that have frequency greater than or equal to min_sup
    counted={}
    for i in PDB:       
        counted.clear()             #This is to clear the dictionary after each iteration
        for j in i:
            if not counted.get(j,False):        #This is to check if the item has already been counted or not
                counted[j]=True
                frequency_for_each_item[j]=frequency_for_each_item.get(j,0)+1       #This is to count the frequency of each item
    frequency_after_sorted={k: v for k, v in sorted(frequency_for_each_item.items(), key=lambda item: item[1], reverse=True)}
    for key,value in frequency_after_sorted.items():    #This is to store the items that have frequency greater than or equal to min_sup
        if(value>=min_sup):          #If frequency is greater than or equal to min_sup, then add it to the dictionary
            patterns_after_delete_element_less_than_threshold[key]=value
            Patterns[prefix+key]=value
    for key in patterns_after_delete_element_less_than_threshold:
        temps=[]
        for i in PDB:
            if(i.find(key)!=-1):
                temp=i[i.find(key)+1:]
                temps.append(temp)
        next_prefix=recursion_to_get_patterns(prefix+key, temps, min_sup)
        Patterns.update(next_prefix)
    return Patterns