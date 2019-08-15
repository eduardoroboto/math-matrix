class Matrix:
    
    def __init__(self, rows, cols, data = []):
        self.rows = rows
        self.cols = cols

        if data:
            self.data = data
        else:
            data = [0] * (rows,cols)

    def __getitem__(self, key):
        i, j = key
        return self.data[(j-1) + (i-1) * self.cols]
    
    def __setitem__(self, key, value):
        i, j = key
        self.data[(j-1) + (i-1) * self.cols ] = value
    
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
    

