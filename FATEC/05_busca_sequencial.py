def busca_sequencial(lista,val):
    """
    Função que realiza uma busca sequencial em uma lista, procurando um val.
    Se val for encontrado, retorna um valor a posição de val na lista.
    Caso contrário, retorna o valor convencional -1.
    """
    # Percorre a lista do início até o fim, usando range() e len()
    # (É necessário ter acesso ás posições dos elementos)
    
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        
        if val == lista[pos]: return pos
    # <-- CUIDADO COM A IDENTAÇÃO AQUI
    # Percorreu toda a lista e não encontrou val; retorna -1
    
    return -1 

####################################################################

nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

pos30 = busca_sequencial(nums, 30)
print(f'Elemento 30 encontrado na posição {pos30}.')

pos_menos3 = busca_sequencial(nums, -3)
print(f'Elemento -3 encontrado na posição {pos_menos3}.')

pos4 = busca_sequencial(nums, 4)
print(f'Elemento 4 encontrado na posição {pos4}.')

#####################################################################

# TESTES COM A LISTA DE NOMES
from data.nomes_completos import nomes

resultado1 = busca_sequencial(nomes, "EDSON PEREIRA")
print(f"EDSON PEREIRA encontrado na posição {resultado1}")

resultado2 = busca_sequencial(nomes, "MARIA FERREIRA")
print(f"MARIA FERREIRA encontrado na posição {resultado2}")

resultado3 = busca_sequencial(nomes, "VALDIR SILVA")
print(f"VALDIR SILVA encontrado na posição {resultado3}")

resultado4 = busca_sequencial(nomes, "GILCINEIA GARCIA")
print(f"GILCINEIA GARCIA encontrado na posição {resultado4}")