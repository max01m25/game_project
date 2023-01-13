
def get_positive_int(txt):
    while True:
        while True:
            num = input(txt)
            if num.lstrip("-").isdigit():
                break
        n=int(num)
        if n>0:
            break
    return n

def get_key(txt):
    print("I suppose you posses a key to another place. Then, select the key to the place you want to visit!")
    while True:
        x = get_positive_int(txt)
        if x in range(0,4):
            break
    return x


def give_non_empty_str(txt):
    
    while True:
        data=input(txt)
        if len(data)!=0:
            break
    return data


#.