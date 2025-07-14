class Matrix:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def display(self):
        for row in self.data:
            print(row)

    def add(self, mat):
        sum=[]
        for i in range(len(self.data)):
            row=[]
            for j in range(len(self.data[i])):
                row.append(self.data[i][j]+mat[i][j])
            sum.append(row)
        return Matrix(sum)
    def sub(self, mat):
        diff=[]
        for i in range(len(self.data)):
            row=[]
            for j in range(len(self.data[i])):
                row.append(self.data[i][j]-mat[i][j])
            diff.append(row)
        return Matrix(diff)

    def multiply(self, B):
    # Number of rows and columns
        m, n = len(self.data), len(self.data[0])
        n_b, p = len(B.data), len(B.data[0])
    
    # Check if matrices can be multiplied
        if n != n_b:
            raise ValueError("Number of columns of A must equal number of rows of B")
    
    # Initialize result matrix with zeros
        result = [[0 for _ in range(p)] for _ in range(m)]
    
    # Perform multiplication
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    result[i][j] += self.data[i][k] * B.data[k][j]
        return Matrix(result)

    def transpose(self):
        trans=[]
        for i in range(len(self.data)):
            row=[]
            for j in range(len(self.data[i])):
                row.append(self.data[j][i])
            trans.append(row) 
        return Matrix(trans)

    def determinent(self):
        if all(len(row) == len(self.data) for row in self.data):
            if len(self.data)==2:
                det=(self.data[0][0]*self.data[1][1])-(self.data[0][1]*self.data[1][0])
                return det
            elif len(self.data)==3:
                a = self.data[0][0]
                b = self.data[0][1]
                c = self.data[0][2]
                d = self.data[1][0]
                e = self.data[1][1]
                f = self.data[1][2]
                g = self.data[2][0]
                h = self.data[2][1]
                i = self.data[2][2]
                det = (
                    a * (e * i - f * h)
                    - b * (d * i - f * g)
                    + c * (d * h - e * g)
                )
                return det
        else:
            print("Not a square matrix!!!")
            return None

    def scalarMultiply(self,n):
        for row in self.data:
            for i in range(len(row)):
                row[i]=n*row[i]
        return self
        

# Basic Matrix Test
m1=Matrix([[1, 2, 3],[4, 5, 6],[1, 2, 5]])
m2=Matrix([[7, 8, 9],[10, 11, 12], [4, 5, 6]])

m1.add(m2).display()
print()
m1.sub(m2).display()
print()
m1.multiply(m2).display()
print()
m1.transpose().display()
print()
print(m1.determinent())
m1.scalarMultiply(2).display()
