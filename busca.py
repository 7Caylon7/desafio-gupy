# 2)Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def count_letters(string):
    string_lower = string.lower()
    amount = string_lower.count('a')
    
    if amount > 0:
        return f"A letra 'a/A' aparece {amount} vezes."
    else:
        return f"A letra buscada não aparece na string inserida."
    
string = input("Digite uma string: ")
result = count_letters(string)
print(result)