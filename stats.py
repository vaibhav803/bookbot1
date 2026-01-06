def count_word(words):
    word_count = len(words.split())
    return word_count



def num_of_characters(words):
    characters = []
    count_of_character = []
    for i in words:
        if i not in characters:
            characters.append(i)
    for j in characters:
        count = 0
        for k in words:
            if j == k:
                count += 1
        count_of_character.append(count)
            
        # if i not in characters:
        #     characters.append(i)

            # for j in words:
            #     if i == j:
            #         count += 1
            # characters.append(count)
        # count_of_character.append(count)
        
    # mydict = dict.fromkeys(characters,count_of_character)
    # return mydict
    # mydict = dict.fromkeys(characters,num_of_characters)
    # return mydict

    my_dict = {key:value for key,value in zip(characters,count_of_character)}
    list_of_dict = []
    # keys_of = my_dict.keys()
    # values_of = my_dict.values()
    for key, value in my_dict.items():
        value = {"char":key, "num" : value}
        list_of_dict.append(value)

    #     updated = dict(char = key  , num = value) 
    #     list_of_dict.append(updated)
    # return list_of_dict

    return list_of_dict

def count_on(dictionary):
    return dictionary["num"]


def sorted(dict_to_sort):
    dict_to_sort.sort(reverse = True,key = count_on)

    return dict_to_sort
            



   
