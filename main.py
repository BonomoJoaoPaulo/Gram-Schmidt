import time

dimension = int(input('Dimensao da base: '))
vectors_list = []

for i in range(0, dimension):
    vector = tuple([int(i) for i in input().split()])
    vectors_list.append(vector)

base = tuple(vectors_list)

"""
def gram_schmidt(vector_conj):
    ortogonal_base = []
    ortogonal_base[0] = vector_conj[0]
    for i in range(1, len(vector_conj)+1):
        ortogonal_base[i] = vector_conj[i] - (internal_product(vector_conj[i], vector_conj[i-1])/internal_product(vector_conj[i-1], vector_conj[i-1])) * vector_conj[i-1]
    return ortogonal_base
"""

def internal_product(v, u):
    ip = 0
    for a in range(0, len(v)):
        ip += v[a] * u[a]
    
    return ip


print(base)
print(internal_product(base[1], base[1]))
time.sleep(10)
