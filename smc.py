"""
Mestrado Profissional em Administração - UNP
Disciplina: Gestão da Cadeia de Suprimentos (Gestão de Operações)
Exercício A - Simulação de Monte Carlo com dez simulações fixas
Professora: Luciana Gondim de A. Guimarães
"""

# Alias para a biblioteca numpy importada
import numpy as np
import time

# Inicia a contagem do tempo de execução do código.
inicio_simulacao = time.perf_counter()

# Quantidade de simulações
num_simulacoes = 10

# Números distribuídos de forma empírica
x = np.array([38, 91, 18, 89, 71, 67, 46, 73, 42, 47])
y = np.array([34, 41, 69, 4, 51, 61, 29, 21, 2, 34])

# Criação do array sem valores
valor_x = np.array([], np.int16)
valor_y = np.array([], np.int16)
valor_z = np.array([], np.int16)

# Construção das colunas
print("-" * 75)
print(f"{'Simulação':<21} {'X definido':<10} {'X gerado':<10} {'Y definido':<10} {'Y gerado':<7} {'Z calculado'}")
print("-" * 75)

# Loop para realizar iterações de acordo com a quantidade de simulações
for i in range(0, num_simulacoes):
    if x[i] <= 20:
        valor_x = np.append(valor_x, 10)        
    elif x[i] > 20 and x[i] <= 70:
        valor_x = np.append(valor_x, 12)        
    elif x[i] > 70 and x[i] <= 100:
        valor_x = np.append(valor_x, 15)
    else:
        print (f"Valor inválido")
    
    if y[i] <= 40:
        valor_y = np.append(valor_y, 8)
    elif y[i] > 40 and y[i] <= 90:
        valor_y = np.append(valor_y, 9)
    elif y[i] > 90 and y[i] <= 100:
        valor_y = np.append(valor_y, 10)        
    else:
        print (f"Valor inválido")

    valor_z = 2 * valor_x + 3 * valor_y

    print (f"Simulação: {i + 1:<10} {x[i]:<10} {valor_x[i]:<10} {y[i]:<10} {valor_y[i]:<8} {valor_z[i]}")
    print("-" * 75)

print("-" * 75)
media_z = sum(valor_z) / num_simulacoes
print (f"Média de Z: {media_z:,.2f} ")
print("-" * 75)

# Finaliza a contagem do tempo de execução do código ao executar as simulações.
fim_simulacao = time.perf_counter()
tempo_simulacao = (fim_simulacao - inicio_simulacao) * 1000
print(f"Foram realizadas {num_simulacoes} simulações em {tempo_simulacao:.3f} ms.")