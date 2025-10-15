def gorjeta(valorConta, porcentagemGorjeta):

    valorGorjeta = valorConta * (porcentagemGorjeta * 0.01)
    totalConta = valorGorjeta + valorConta

    return valorGorjeta, totalConta

