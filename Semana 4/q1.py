def reposta(orcas, tanque1, tanque2):
    #Preenche o tanque 1 com as keys dos vizinhos de 1
    for x in range(len(orcas[1])):
        if orcas[1][x] == 1:
            tanque1.add(x+1)
    #Testa se os vizinhos de 1 podem estar no tanque 1
    t1 = tanque1.copy()
    for orca_atual in t1:
        for orca_vizinha in t1:
            #Caso a orca atual nao seja vizinho de todos do tanque 1, retiro ela de la
            if orcas[orca_atual][orca_vizinha-1] == 0:
                tanque1.remove(orca_atual)
                #Tento adicionar ela no tanque 2, caso esteja vazio, so adiciono
                if len(tanque2) == 0:
                    tanque2.add(orca_atual)
                #Caso nao esteja vazio
                else:
                    #Testo se a orca eh vizinha de todos no tanque 2
                    for orca_vizinha in tanque2:
                        #Se nao for, retorna falha
                        if orcas[orca_atual][orca_vizinha-1] == 0:
                            return "Fail!"
                    #Se for, adiciona no tanque 2
                    tanque2.add(orca_atual)
                #Para o loop porque ja foi decidio onde ela vai ficar
                break
        #Atualiza o auxiliar pra percorrer o tanque 1
        t1 = tanque1.copy()

    #Pega todas as orcas que ainda nao estao em tanque
    set_orcas = set(orcas.keys())
    #E guarda na variavel orcas_que_sobraram
    orcas_que_sobraram = set_orcas.difference(tanque1.union(tanque2))

    #Percorre todas as orcas que sobraram 
    for orca_atual in orcas_que_sobraram:
        #Percorre as orcas no tanque 1
        for orca_vizinha in t1:
            #Se a orca atual nao for vizinha de todas no tanque 1
            if orcas[orca_atual][orca_vizinha-1] == 0:
                ##Tento adicionar ela no tanque 2, caso esteja vazio, so adiciono
                if len(tanque2) == 0:
                    tanque2.add(orca_atual)
                #Caso nao esteja vazio
                else:
                    #Testo se a orca eh vizinha de todos no tanque 2
                    for orca_vizinha in tanque2:
                        #Se nao for, retorna falha
                        if orcas[orca_atual][orca_vizinha-1] == 0:
                            return "Fail!"
                    #Se for, adiciona no tanque 2
                    tanque2.add(orca_atual)
                #Para o loop porque ja foi decidio onde ela vai ficar
                break
    #Caso tenha conseguido distribuir todas as orcas, retorna sucesso
    return "Bazinga!"

#Pega a quantidade de orcas
N = int(input())
#Cria o dicionario de orcas
orcas = {}
#Cria os tanques
tanque1 = set()
tanque2 = set()
#Guarda a lista de 1 e 0 da orca atual
for i in range(N):
    se_falam = [int(valor) for valor in input().split(' ')]
    orcas[i+1] = se_falam
#Chama o método com o resultado final
print(reposta(orcas, tanque1, tanque2))
