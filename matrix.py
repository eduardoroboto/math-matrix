# transpose: OK!

# mumtiplicação matrix: OK!

# soma escalar: OK!
# subtração escalar: OK! 
# divisão escalar: OK!
# multiplicação escalar: OK!


class Matrix:
    def __init__(self, rows, cols, data = []):
        self.rows = rows
        self.cols = cols

        if data:
            self.data = data
        else:
            self.data = [0] * rows*cols

    def __getitem__(self, key):
        if type(key) == tuple:
            i, j = key
            if i > self.rows or j > self.cols:
                raise ValueError("Valor invalido")
            return self.data[(j-1) + (i-1) * self.cols]
        else:
            return self.return_list_rows(key)
        
    def __setitem__(self, key, value):
        if type(key) == tuple:
            i, j = key
            if i > self.rows or j> self.cols:
                raise ValueError("Valor invalido")
            self.data[(j-1) + (i-1) * self.cols ] = value
        else:
            self.insert_row(key,value)

            
    
    def __add__(self, other):
        res = Matrix(self.rows, self.cols)

        for i in range(1,self.rows + 1):
            for j in range(1,self.cols + 1):
                res[i, j] = self[i, j] + other[i, j]
        return res
    
    def __sub__(self, other):
        res = Matrix(self.rows, self.cols)

        for i in range(1,self.rows + 1):
            for j in range(1,self.cols + 1):
                res[i, j] = self[i, j] - other[i, j]
        return res

    def __mul__(self, other):
        res = Matrix(self.rows, self.cols)

        for i in range(1,self.rows + 1):
            for j in range(1,self.cols + 1):
                res[i, j] = self[i, j] * other[i, j]
        return res
    
    def __truediv__(self, other):
        res = Matrix(self.rows, self.cols)

        for i in range(1,self.rows + 1):
            for j in range(1,self.cols + 1):
                try:
                    res[i, j] = self[i, j] / other[i, j]
                except ZeroDivisionError:
                    print("Divisão por zero, NOPE!!")
        return res

    
    def __repr__(self):
        s = str()
        for i in range(1,self.rows + 1):
            for j in range(1,self.cols + 1):
                s+=" {:^5.1f}".format(self[i, j])
            s+="\n"
        
        return s

    def insert_row(self,desteny,lista):
        for k in range(1,self.cols+1):
            self[desteny,k] = lista[k-1]

    def transposition(self):
        b = Matrix(self.cols, self.rows, [])
        for i in range(1,self.rows + 1):
            for j in range(1,self.cols + 1):
                b[j, i] = self[i, j]
        
        self.rows = b.rows
        self.cols = b.cols
        self.data = b.data
               

    def return_list_rows(self, index):
        rows = list()

        for i in range(1,self.cols + 1):
            rows.append(self[index,i])
        
        return rows

    def return_list_cols(self,index):
        cols = list()
        for i in range(1,self.rows + 1):
            cols.append(self[i,index])

        return cols



    def dot(self, b):
        if(self.cols != b.rows ):
            raise ValueError("Matrizes invalidas!!")
        
        new_matrix = Matrix(self.rows,b.cols)
        for i in range(1,new_matrix.rows + 1):
            for j in range(1,new_matrix.cols + 1):
                list_rows = self.return_list_rows(i)
                list_cols = b.return_list_cols(j)
                value = 0
                for x1, x2 in zip(list_cols, list_rows):
                    value += x1*x2
                new_matrix[i,j] = value
        
        return new_matrix

    def get_first_one(self,value,posx,posy,):
        if posy < posx:
            for x in range(1, self.rows):
                if self[x,posy] == 1:
                    print("busc su",x,posy)
                    return self[x]
        elif posy > posx:
            for x in range(self.rows, 0 , -1):
                print("pos",x,posy)
                if self[x,posy] == 1:
                    print("busc in",x,posy)
                    return self[x]



    def one_ladder_check(self):
        for i in range(1, self.cols):
            if self[i,i] != 1:
                return False
        
        return True
            
    def zeroes_triangle(self):
        for i in range(1, self.cols):
            for j in range(i+1, self.rows + 1):
                if self[j,i] != 0:
                    return False
            
            return True

# Pegar cada posicao for com 1,1 e continuar se ele for 1 continue se nao de swap

    def gauss(self):
        print("Entrou")
        if self.rows+1 != self.cols:
            raise ValueError("Matrix invalida, tem que ser uma matrix NxN+1")

        for i in range(1, self.cols):
            print(self)


            if self[i,i] == 0 :
                for j in range(i+1, self.rows + 1):
                    if self[j,i] > self[i,i]:
                        self[i,i] ,self[i,j] =  self[j,i], self[i,i]
                        break

            if self[i,i] != 1:
                #faz a multiplicao pelo valor da linha sobre 1
                self[i] = [value * (1/self[i,i]) for value in self[i]]

            for j in range(i+1, self.rows + 1):
                if self[j,i] != 0:
                    linha = [ ((-1*self[j,i]) * value) for value in self.get_first_one(self[j,i],j,i)]
                    self [j] = [x + y for x ,y in zip(self[j], linha)]

        print(self)
        print("Indo zerar")
    #   faz no triangulo superior.
        for j in range(self.cols - 1, 0, -1):
             for i in range(j - 1, 0 , -1):
                if self[i,j] != 0:
                    print("d\n",self)
                    print("tri",i,j)
                    print(self.get_first_one(self[i,j],i,j))
                    linha = [ ((-1*self[i,j]) * value) for value in self.get_first_one(self[i,j],i,j)]
                    self [i] = [x + y for x ,y in zip(self[i], linha)]
                



        # troca de matriz
        # self[max_row], self[i] = self[i], self[max_row]
                    



# class test
if __name__ == '__main__':
    # a = Matrix(4,4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    # a = Matrix(3,4,[-1,1,-2,-20,5,2,1,21,2,5,4,33])
    # a = Matrix(2,5,[2,1,1,1,1,2,1,1,1,3])
    # a = Matrix(3,4,[1,-1,2,2,2,1,-1,1,-2,-5,3,3])
    a = Matrix(3,4,[1,3,1,9,1,1,-1,1,3,11,5,35])
    a = Matrix(3,4,[1,-2,1,0,0,2,-8,8,5,0,-5,10])

    # b =  Matrix(3,2,[2,0,1,-1,3,5])
    
    # b = [0,0,0,0]
    # a[2] = b
    #print(a.gauss())
    # a[1],a[2] = a[2],a[1]
    print(a)
    a.gauss()
    print(a)
    # a.gauss()
    # c = a.dot(b)
    # print(c)