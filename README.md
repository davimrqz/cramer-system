# cramer-system
A matrix system in Python.

# Sistema Linear 3x3 com Regra de Sarrus e Cramer

Este projeto resolve sistemas lineares 3x3 utilizando Python puro, com aplicação da **Regra de Sarrus** para cálculo do determinante e **Regra de Cramer** para encontrar as incógnitas `x`, `y` e `z`.

## 📚 Descrição

O programa solicita ao usuário:

- Os coeficientes da matriz 3x3 (uma linha por vez);
- Os 3 termos independentes (vetor 3x1).

Depois, calcula:

- O determinante da matriz principal (usando Regra de Sarrus);
- Os determinantes das matrizes modificadas (Cramer);
- Os valores de `x`, `y` e `z`.

## 🚀 Como usar

Execute o programa e digite os valores quando solicitado.

### Exemplo de entrada:
```
Linha 1 (separe os 3 números com espaço): 2 -1 3  
Linha 2 (separe os 3 números com espaço): 1 0 4  
Linha 3 (separe os 3 números com espaço): 5 2 -2  

Termo 1: 7  
Termo 2: 4  
Termo 3: 3
```

### Saída esperada:
```
Solução do sistema:
x = 1.625  
y = -1.96875  
z = 0.78125
```

## 🧠 Fundamentos matemáticos usados

- **Regra de Sarrus**: cálculo de determinantes 3x3.
- **Regra de Cramer**: resolução de sistemas lineares com matriz invertível.

## 📁 Arquivo principal

- `sistema_cramer.py`

## 👨‍💻 Equipe

- Davi Marques  
- Luan Rocha  
- Gabriel Rodrigues  
- Gabriel Campos  
- Renan Oliveira

---

Projeto desenvolvido para a disciplina de **Matemática Computacional** – Engenharia de Software – UniAteneu.
