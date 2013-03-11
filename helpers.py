def ep(n, e):
    resultado = n
    for x in range(e - 1):
        resultado *= n
    return resultado
