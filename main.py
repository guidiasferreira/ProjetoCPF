import gerar_cpf
import validar_cpf
from time import sleep

def menu():
    print("1. Gerar CPF")
    print("2. Validar CPF")
    print("3. Sair do programa")


while (True):
    menu()

    try:
        opcao = int(input("\nEscolha uma opção: "))

        match (opcao):
            case 1:
                print(gerar_cpf.gerar())
            
            case 2:
                cpf = str(input("Digite o CPF: ")).replace(".", "").replace("-", "").replace(" ", "")

                if (validar_cpf.validar(cpf)):
                    print("CPF válido! ✅")

                else:
                    print("CPF inválido! ❌")

            case 3:
                print("\nSaindo...")
                sleep(1)
                break

            case _:
                print("Informe um número entre 1 e 3.")
    
    except (ValueError):
        print("\nERRO! Informe apenas um número inteiro (int).")