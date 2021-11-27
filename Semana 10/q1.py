def binary_search(lista, k, N):
    low = 0
    high = N - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if lista[mid] <= k:
            return mid
        else:
            low = mid + 1
    return -1

def erdoes_gallai(lista, N, soma):
    for k in range(1, N+1):
        esq = soma[k-1]
        pos = binary_search(lista, k, N)
        if k+1 > N:
            di = k*(k-1)
        elif (pos+1) <= (k+1):
            di = k*(k-1) + soma[N-1] - soma[k-1]
        else: 
            di = k*(k-1) + k*(pos-k) + soma[N-1] - soma[pos-1]
        if esq > di:
            return False
    return True

while(True):
    try:
        N = int(input())
        aux = False
        li = [0]*(N)
        soma =  0
        soma_inv = [0]*(N)
        entrada = input().split()
        for i in range(N):
            if int(entrada[i]) > N:
                aux = True
                break
            li[i] = int(entrada[i])
            soma += li[i]
        if soma%2 != 0 or aux:
            print('impossivel')
        else:
            li.sort(reverse=True)
            #print(li)
            # 3 - 5 - 6
            soma_inv[0] = li[0]
            for i in range(1,N):
                soma_inv[i] = soma_inv[i-1] + li[i]
            print(soma_inv)
            if(erdoes_gallai(li,N,soma_inv)):
                print('possivel')
            else:
                print('impossivel')
    except EOFError:
        break
    
