dimension = int(input('Dimensao da base: '))
vectors_list = []

for i in range(0, dimension):
    vector = tuple([int(i) for i in input().split()])
    vectors_list.append(vector)

base = tuple(vectors_list)


def gram_schmidt(vector_conj):
    ortogonal = [[None]*len(vector_conj[0])]*len(vector_conj)
    ortogonal[0] = vector_conj[0]
    for i in range(1, len(vector_conj)):
        proj = (internal_product(vector_conj[i], vector_conj[i-1])/internal_product(vector_conj[i-1], vector_conj[i-1]))
        second_product = mult_list_for_number(vector_conj[i-1], proj)
        for j in range(len(vector_conj[i])):
            ortogonal[i][j] = vector_conj[i][j] - second_product[j]
        ortogonal[i] = tuple(ortogonal[i])
    return ortogonal


def mult_list_for_number(lista, number):
    new_list = [None]*len(lista)
    for ind in range(len(lista)):
        new_list[ind] = lista[ind] * number

    return new_list


def internal_product(v, u):
    ip = 0
    for a in range(0, len(v)):
        ip += v[a] * u[a]
    
    return ip


print("Base: ", base)

ortogonal_base = gram_schmidt(base)
print("Base Ortogonal: ", ortogonal_base)

ortogonal_ip = internal_product(ortogonal_base[0], ortogonal_base[1])
print("Produto Interno da Base Ortogonal: ", ortogonal_ip)

"""
-----------------------------------------------------------------------------------------
OBS: - Os produtos internos estarao com valores incorretos por conta do arredondamento;
    - Eh necessario implementar o uso de fracoes;
    - Resolver warning da linha 19;
    - Testar com conjuntos de vetores de dimensoes != 2;
    - Implementar a Normalizacao.
"""
