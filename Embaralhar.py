from random import sample

def embaralhar(palavra):
    s = sample(palavra, len(palavra))
    x = "".join(s)
    print(x.upper())
 
nome = input("Digite uma palavra: ")

embaralhar(nome)
