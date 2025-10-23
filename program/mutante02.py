def ladosTriangulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a) and a > 0 and b > 0 and c > 0:
        if a == b and b != c and c == b:
            return "Equilatéro"
        elif (a == b and b != c) or (a != c and a == b) or (c == b and a != b):
            return "Isóceles"
        elif a != b and b == c and a != c:
            return "Escaleno"
        else:
            return "Não é válido"
    else:
        return "Não é possível formar um triangulo"
