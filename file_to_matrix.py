import os
import re
from matrix import Matrix
import time
import collections


path = "/home/sred/prog/faculdade/python/matrix_trabalho/packs/pack7/"

print("Etapa - 0")


files = os.listdir(path)
files.sort()
for file in files:
    if "coe" in file:
        files.remove(file)

ex = dict()

print("Etapa - 1")

for file in files:
    with open(path+file, 'r') as txt:
        texto = list()
        for line in txt:
            if '%' in line:
                pass
            else:
                texto.append(line.strip("\n"))
        ex[file] = texto

print("Etapa - 2")

#for name in ex:
#    res = int(i) for i in test_string.split() if i.isdigit()

dic_ext_res = dict()

for name in ex:
    temp = re.findall(r'\d+', name)

    lista = [x.split(' ') for x in (ex[name])]
    
    dic_ext_res.setdefault(temp[0], []).append(lista)

print("Etapa - 3")



dic_matrix = dict()

for key in dic_ext_res:
    #print(key, dic_ext_res[key][0][0])
    
    
    rows =  int(dic_ext_res[key][0][0][0])
    cols =  int(dic_ext_res[key][0][0][1])


    #print("{} {}, {} {}".format(rows,type(rows), cols,type(cols)))

    new_matrix = Matrix(rows,cols)
    for pos in range(1, len(dic_ext_res[key][0])):
        i = int(dic_ext_res[key][0][pos][0])
        j = int(dic_ext_res[key][0][pos][1])
        value = int(dic_ext_res[key][0][pos][2])
        #print(i,j,value)
        #print(type(i),type(j),type(value))

        new_matrix[i,j] = value
    resposta = []
    for pos in range(1, len(dic_ext_res[key][1])):
        res = int(dic_ext_res[key][1][pos][2])
        resposta.append(res)
    

    

    dic_matrix.setdefault(key, []).extend([new_matrix, resposta])
    #print(key)
    #print(new_matrix)
    #print(dic_matrix[key][0])


print("Etapa - 4")

#print(dic_matrix["002"][0])


for key in dic_matrix:
    start_time = time.time()
    a = dic_matrix[key][0]
    res = dic_matrix[key][1]
    c = a.gauss_jordan()
    lista = c.return_list_cols(c.cols)
    print("Ordem: {} |Processamento em: {:^4.8f} seconds ---".format(a.rows,time.time() - start_time))
    print("A resposta deu igual a matriz resposta? :{}".format(collections.Counter(lista) == collections.Counter(res)))


#print(a)
#print(c)

    


    

#print(dic_ext_res['001'])

#for file in dic_ext_res:
#    for matrix in file[0]:
#        print(type(matrix))
            



#print(new_dict['001'])
def read_file():
    pass