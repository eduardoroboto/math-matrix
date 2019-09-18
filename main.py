from matrix import Matrix



# class test
if __name__ == '__main__':
    #a = Matrix(4,4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    #a = Matrix(3,4,[-1,1,-2,-20,5,2,1,21,2,5,4,33])
    #a = Matrix(2,5,[2,1,1,1,1,2,1,1,1,3])
    #a = Matrix(3,4,[1,-1,2,2,2,1,-1,1,-2,-5,3,3])
   # a = Matrix(2,2,[1,2,3,4])
    #b = Matrix(2,2,[2,2,2,2])

    #c = a.transpose()
    #c = b.__rsub__(a)
    #print(a)
    #print(c)
    #c = a.gauss_jordan()


    #a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    #b = Matrix(3, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90])

    #c =  b - a
    #print(c[2,2] == 45)

    #c = 2 - a
    #print(a)
    #print(c)
    #print(c[2,2] == 3)




    #print(a)
    #print(c)
    
    
    #Situação especifica em que o x3 não importa (gratis)
    #a = Matrix(3,4,[1,3,1,9,1,1,-1,1,3,11,5,35])
    #a = Matrix(3,4,[1,-2,1,0,0,2,-8,8,5,0,-5,10])

    # b =  Matrix(3,2,[2,0,1,-1,3,5])
    
    # b = [0,0,0,0]
    # a[2] = b
    #print(a.gauss())
    # a[1],a[2] = a[2],a[1]
    #print(a)
    #a.gauss_jordan()
    #print(a)
    # a.gauss()
    # c = a.dot(b)
    # print(c)

    # teste 1 OK
    #a = Matrix(2, 2, [1, 2, 3, 4])
    #print(a[3,3])
    #teste 2 ok
    #a[3,3] = 5

    a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = Matrix(2, 2, [10, 20, 30, 40])

    c = a.inverse()

    print("{}\n{}".format(a,c))
 