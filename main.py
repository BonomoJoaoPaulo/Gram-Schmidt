dimension = int(input('Dimensao da base: '))
vectors_list = []

for i in range(0, dimension):
    vector = [int(i) for i in input().split()]
    vectors_list.append(vector)

base = vectors_list


def gram_schmidt(vector_conj):
    ortogonal = [[None]*len(vector_conj[0])]*len(vector_conj)
    ortogonal[0] = vector_conj[0]
    for i in range(1, len(vector_conj)):
        ortogonal[i] = sub_list(vector_conj[i], recursive_proj(vector_conj, i))

        #proj = (internal_product(vector_conj[i], vector_conj[i-1])/internal_product(vector_conj[i-1], vector_conj[i-1]))
        #second_product = mult_list_for_number(vector_conj[i-1], proj)
        #for j in range(len(vector_conj[i])):
         #   ortogonal[i][j] = vector_conj[i][j] - second_product[j]
    return ortogonal


def recursive_proj(vector_conj, k):
    if k == 0:
        return vector_conj[0]

    proj_k = internal_product(vector_conj[k], vector_conj[k-1])/internal_product(vector_conj[k-1], vector_conj[k-1])
    second_product = mult_list_for_number(vector_conj[k-1], proj_k)

    return sum_list(second_product, recursive_proj(vector_conj, k - 1))


def mult_list_for_number(lista, number):
    new_list = [None]*len(lista)
    for ind in range(len(lista)):
        new_list[ind] = lista[ind] * number

    return new_list


def sub_list(list_a, list_b):
    new_list = [None] * len(list_a)
    for j in range(len(list_a)):
        new_list[j] = list_a[j] - list_b[j]
    return new_list


def sum_list(list_a, list_b):
    new_list = [None]*len(list_a)
    for j in range(len(list_a)):
        new_list[j] = list_a[j] + list_b[j]
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
OBS:    - Os produtos internos estarao com valores incorretos por conta do arredondamento;
        - Eh necessario implementar o uso de fracoes;
        - Ortogonalização incorreta: problema deve estar na função recursiva;
        - Implementar a Normalizacao.
"""
