# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a 
# soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número 
# informado pertence ou não a sequência.

def seq_fibonacci(n):
    s_fibonacci = [0, 1]
    while True:
      next_value = s_fibonacci[-1] + s_fibonacci[-2]
      if next_value > n:
          break
      s_fibonacci.append(next_value)
    return s_fibonacci

def check_fibonacci(num):
  s_fibonacci = seq_fibonacci(num)
  if num in s_fibonacci:
    return f"O número {num} está contido na sequência de Fibonacci."
  else:
    return f"O númeor {num} não está contido na sequência de Fibonacci"


number = int(input("Número a ser testado: "))
result = check_fibonacci(number)
print(result)