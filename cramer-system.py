def sarrus(mat):
    """Calcula o determinante de uma matriz 3x3 usando a Regra de Sarrus"""
    a, b, c = mat[0]
    d, e, f = mat[1]
    g, h, i = mat[2]
    det = (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)
    return det


def substituir_coluna(matriz, coluna_substituir, nova_coluna):
    """Substitui uma coluna de uma matriz por uma nova coluna"""
    nova_matriz = []
    for i in range(3):
        nova_linha = matriz[i].copy()
        nova_linha[coluna_substituir] = nova_coluna[i]
        nova_matriz.append(nova_linha)
    return nova_matriz


def resolver_sistema_cramer(matriz, termos):
    """Resolve um sistema 3x3 usando a Regra de Cramer"""
    det_principal = sarrus(matriz)

    if det_principal == 0:
        return None, "Sistema impossível ou indeterminado (det = 0)"  # ← se o sistema não tiver solução única

    matriz_x = substituir_coluna(matriz, 0, termos)
    matriz_y = substituir_coluna(matriz, 1, termos)
    matriz_z = substituir_coluna(matriz, 2, termos)

    det_x = sarrus(matriz_x)
    det_y = sarrus(matriz_y)
    det_z = sarrus(matriz_z)

    x = det_x / det_principal  # ← x pode ser 0.0, sem problema
    y = det_y / det_principal
    z = det_z / det_principal

    return (x, y, z), None


if __name__ == "__main__":
    print("=== Resolução de sistema 3x3 pela Regra de Cramer ===")

    matriz = []
    termos = []

    print("Digite os coeficientes da matriz 3x3 (linha por linha):")
    for i in range(3):
        linha = input(f"Linha {i+1} (separe os 3 números com espaço): ")
        numeros = list(map(float, linha.strip().split()))
        if len(numeros) != 3:
            print("Erro: cada linha deve ter exatamente 3 números.")
            exit(1)
        matriz.append(numeros)

    print("Digite os 3 termos independentes (um por linha):")
    for i in range(3):
        termo = float(input(f"Termo {i+1}: "))
        termos.append(termo)

    resultado, erro = resolver_sistema_cramer(matriz, termos)

    if erro:
        print(erro)
    else:
        x, y, z = resultado
        print("\nSolução do sistema:")
        print(f"x = {x}")
        print(f"y = {y}")
        print(f"z = {z}")
