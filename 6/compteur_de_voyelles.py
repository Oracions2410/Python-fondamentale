# Compteur de voyelles

def get_vowels_number(word):
    a_count = 0
    e_count = 0
    u_count = 0
    i_count = 0
    o_count = 0
    y_count = 0

    for v in word:
        if v.lower() == "a" and a_count == 0:
            a_count += 1
        elif v.lower() == "e" and e_count == 0:
            e_count += 1
        elif v.lower() == "u" and u_count == 0:
            u_count += 1
        elif v.lower() == "i" and i_count == 0:
            i_count += 1
        elif v.lower() == "o" and o_count == 0:
            o_count += 1
        elif v.lower() == "y" and y_count == 0:
            y_count += 1

    return a_count + e_count + u_count + i_count + o_count + y_count


print(get_vowels_number('Portez ce whisky au vieux juge blond qui fume !'))