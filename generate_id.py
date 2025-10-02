import random

def id_generator(length=4):
    return "BX00KU"+ "".join(random.choices("0123456789ABCDEF", k=length))



