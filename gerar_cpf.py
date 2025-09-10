from random import randint
from validar_cpf import validar, primeiro_digito, segundo_digito

def gerar():
    cpf = ""

    for i in range(9):
        cpf += str(randint(0, 9))

    primeiro = str(primeiro_digito(cpf))
    segundo = str(segundo_digito(cpf))

    cpf_completo = cpf + primeiro + segundo

    if (validar(cpf_completo)):
        cpf_formatado = cpf_completo[:3] + "." + cpf_completo[3:6] + "." + cpf_completo[6:9] + "-" + cpf_completo[9:]
        return f"CPF gerado: {cpf_formatado}"
    
    else:
        return gerar()