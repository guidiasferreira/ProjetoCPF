from random import randint
import validar_cpf
import validar_cpf
import validar_cpf

def gerar():
    cpf = ""

    for i in range(9):
        cpf += str(randint(0, 9))

    cpf.replace(".", "").replace("-", "").replace(" ", "") 

    primeiro_digito = str(validar_cpf.validar_primeiro(cpf))
    segundo_digito = str(validar_cpf.validar_segundo(cpf))
    validacao = str(validar_cpf.validar(cpf))

    if (validacao):
        cpf_formatado = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + primeiro_digito + segundo_digito
    
    else:
        gerar()

    return f"CPF gerado: {cpf_formatado}"

#Editando CPF para ficar no formato: ###.###.###-##
