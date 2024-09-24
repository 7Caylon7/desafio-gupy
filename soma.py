# 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; 
# enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

indice = 12;
soma = 0;
K = 1;

while K < indice:
    K = K + 1;
    soma = soma + K;
    

print(f"O valor da variável soma é: {soma}");
