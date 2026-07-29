import random

def senhaa(size):

    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    senha = ""
    
    for _ in range(size):
       senha += random.choice(caracteres)
    return senha
