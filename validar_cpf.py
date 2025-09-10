
def primeiro_digito(cpf):
    cpf_formatado = cpf[:9]

    soma = 0
    mult = 1
    cont = 10

    #1º Passo - Realizar a soma dos 9 primeiros dígitos do CPF sendo multiplicados pela contagem regressiva começando pelo 10
    for numero in cpf_formatado:
        mult = (int(numero) * cont)
        soma += mult
        cont -= 1
        

    #2º Passo - Multiplicar o resultado anterior por 10
    mult = 10 * soma

    #3º Passo - Obter o resto da divisão da conta anterior por 11
    resultado = mult % 11

    if (resultado > 9):
        resultado = 0

    else:
        resultado = resultado

    return resultado


def segundo_digito(cpf):
    cpf_formatado = cpf[:10]

    soma = 0
    mult = 1
    cont = 11

    #1º Passo - Realizar a soma dos 10 primeiros dígitos do CPF sendo multiplicados pela contagem regressiva começando pelo 11
    for numero in cpf_formatado:
        mult = (int(numero) * cont)
        soma += mult
        cont -= 1
        

    #2º Passo - Multiplicar o resultado anterior por 10
    mult = 10 * soma

    #3º Passo - Obter o resto da divisão da conta anterior por 11
    resultado = mult % 11

    if (resultado > 9):
        resultado = 0

    else:
        resultado = resultado

    return resultado


def validar(cpf):
    if (len(cpf) != 11 or not cpf.isdigit()):
        return False

    if (cpf == cpf[0] * len(cpf)):
        return False
    
    primeiro = primeiro_digito(cpf)
    segundo = segundo_digito(cpf)
    
    return(cpf[-2:] == f"{primeiro}{segundo}")