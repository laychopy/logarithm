from helpers import ep


class Logaritmo():
    def __init__(self, base, numero):
        self.b = base
        self.n = numero

    def apply(self):
        nu = 1
        b = self.b
        n = self.n
        while nu != 0:
            export = nu
            resultado = ep(b, nu)
            print resultado
            if resultado == n:
                print "El logaritmo de %s en base %s es %s" % (n, b, export)
                break
            else:
                nu += 1

# if __name__ == '__main__':
#     log = Logaritmo(2, 8)
