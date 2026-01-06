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
    return my_dict


            

