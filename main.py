from helpers import ep


class Logarithm():
    '''Main Class of the library. Instance Logarithm with two arguments the base and the number Example:
	   l = Logarithm(2,8)  '''
    def __init__(self, base, numero):
        self.b = base
        self.n = numero

    def solve(self):
        nu = 1
        b = self.b
        n = self.n
        while nu != 0:
            export = nu
            resultado = ep(b, nu)
            # print resultado
            if resultado == n:
                break
            else:
                nu += 1
        return nu
# if __name__ == '__main__':
#     log = Logaritmo(2, 8)
# '''a method to solve the logarithm. Example: l.solve(). return the result as a int '''
