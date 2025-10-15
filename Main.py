import calcular_gorjeta
from calcular_gorjeta import gorjeta

def tabulacao(texto):
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)

def menu():
    texto = "       BEM VINDO A CALCULADORA DE GORJETA      "
    tabulacao(texto)

def main():
    menu()
    valor_conta, valor_gorjeta = pegarDados()
    valor_gorj, total = Funções.gorjeta(valor_conta, valor_gorjeta)

    print(f"\nValor da gorjeta calculado: R$ {valor_gorj:.2f}")
    print(f"Total da conta: R$ {total:.2f}")

def pegarDados():
    try:
        valor_conta = float(input("\nValor da conta em R$:\t"))
        valor_gorjeta = float(input("Porcentagem da gorjeta (%):\t"))
        return valor_conta, valor_gorjeta
    except ValueError:
        print("Valores incorretos, tente novamente.")
        return pegarDados()  # chama de novo corretamente

if __name__ == "__main__":
    main()
