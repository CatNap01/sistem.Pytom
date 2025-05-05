def soma():
    resultado = num_01 + num_02

    return resultado

def somaDoisNumeros(nota_01, nota_02):
    resultado = nota_01 + nota_02

    return print(resultado)

somaDoisNumeros(31, 43)

def cadastrar (nome, idade):
    data =  {
        "nome":nome,
        "idade":idade
    }

    return print(data)

nome = input("Qual seu nome:" )

idade = input("Qual sua idade:" )

cadastrar ("nome, idade")