import time

dimension = int(input('Dimensao da base: '))
vectors_list = []

for i in range(0, dimension):
    vector = tuple([int(i) for i in input().split()])
    vectors_list.append(vector)

base = tuple(vectors_list)

print(base)
time.sleep(5)
