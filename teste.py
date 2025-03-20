from collections import deque

nomes = ["Pai", "Mãe", "Filha 1", "Filha 2", "Filho 1", "Filho 2", "Policial", "Prisioneiro"]

def pode_atravessar(estado, movimento):
    margem_atual = estado[-1]
    return all(estado[i] == margem_atual for i in movimento)

def estado_valido(estado):
    margem1 = [i for i, x in enumerate(estado) if x == 1]  
    margem2 = [i for i, x in enumerate(estado) if x == 0]  
    
    if 1 in margem1:
        if 4 in margem1 or 5 in margem1:
            if 0 not in margem1:
                return False
    if 0 in margem1:
        if 2 in margem1 or 3 in margem1:
            if 1 not in margem1:
                return False
    if 7 in margem1:
        if len(margem1) > 1 and 6 not in margem1:
            return False    
        




    if 1 in margem2:
        if 4 in margem2 or 5 in margem2:
            if 0 not in margem2:
                return False
    if 0 in margem2:
        if 2 in margem2 or 3 in margem2:
            if 1 not in margem2:
                return False
    if 7 in margem2:
        if len(margem2) > 1 and 6 not in margem2:
            return False 
        

        
    
    return True









def movimentos(estado):
    possiveis = []
    for i in range(len(estado) - 1):
        for j in range(i, len(estado) - 1):
            if not pode_atravessar(estado, [i, j]):
                continue
            novo_estado = estado[:]
            novo_estado[i] = 1 - estado[-1]
            novo_estado[j] = 1 - estado[-1]
            novo_estado[-1] = 1 - estado[-1]
            if estado_valido(novo_estado):
                if i == 0 or i == 1 or i == 6 or j == 0 or j == 1 or j == 6:
                    possiveis.append((novo_estado, (i, j)))
    
    return possiveis

def bfs(inicio, final):
    fila = deque([([inicio], [])])
    explorado = set()
    
    while fila:
        caminho, movimentos_realizados = fila.popleft()
        estado_atual = caminho[-1]
        
        if tuple(estado_atual) in explorado:
            continue
        
        if estado_atual == final:
            return caminho, movimentos_realizados
        
        for prox_estado, mov in movimentos(estado_atual):
            if tuple(prox_estado) in explorado:
                continue
            novo_caminho = caminho + [prox_estado]
            novo_movimentos = movimentos_realizados + [mov]
            if prox_estado == final:
                return novo_caminho, novo_movimentos
            fila.append((novo_caminho, novo_movimentos))
        
        explorado.add(tuple(estado_atual))
    
    return None, None

inicio = [1, 1, 1, 1, 1, 1, 1, 1, 1]
final = [0, 0, 0, 0, 0, 0, 0, 0, 0]

solucao, movimentos_realizados = bfs(inicio, final)

if solucao:
    print("Solução encontrada:")
    for i, mov in enumerate(movimentos_realizados, start=1):
        estado_origem = solucao[i-1]
        pessoa1 = nomes[mov[0]]
        pessoa2 = nomes[mov[1]]
        margem_origem = "0 → 1" if estado_origem[-1] == 0 else "1 → 0"
        
        if mov[0] == mov[1]:
            print(f"Movimento {i}: {pessoa1} atravessou sozinho ({margem_origem})")
        else:
            print(f"Movimento {i}: {pessoa1} e {pessoa2} atravessaram ({margem_origem})")
else:
    print("Nenhuma solução encontrada.")
