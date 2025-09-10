from gerar_cpf import gerar
from validar_cpf import validar
from time import sleep


def menu():
    print()
    print("Gerador & Validador de CPF")
    print("1. Gerar CPF")
    print("2. Validar CPF")
    print("3. Sair do programa")
    print()


def executar_opcao(opcao):
    match (opcao):
        case 1:
            result = gerar()
        
        case 2:
            cpf = str(input("Digite o CPF: ")).replace(".", "").replace("-", "").replace(" ", "")

            if (validar(cpf)):
                result = "CPF válido! ✅"

            else:
                result = "CPF inválido! ❌"
        
        case 3:
            return None
        
        case _:
            result = "Escolha uma opção entre 1 e 3."
    
    return result


while (True):
    menu()

    try:
        opcao = int(input("Escolha uma opção: "))
        result = executar_opcao(opcao)

        if (result is None):
            print("\nSaindo do programa...")
            sleep(1)
            break
        
        else:
            print(result)
    
    except (ValueError):
        print("\nErro! Informe apenas um número inteiro (int).")
    
    except Exception as e:
        print(f"\nErro! Desconhecido: {e}")