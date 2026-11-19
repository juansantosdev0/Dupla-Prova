import os
os.system("cls")

#atividade feita pelos alunos: Juan santos, Emerson Davi.





def mostrar_saldo(saldo):
    print(f'Saldo atual: R$ {saldo}')
    
def mostrar_extrato(extrato):
    if len(extrato) == 0:
        print('Nenhuma movimentação.')
    else:
        for linha in extrato:
            print(linha)
    print(f'Saldo atual: R$ {saldo}')
    
def depositar(saldo, extrato):
    valor = float(input("Valor do depósito: R$ "))
    if valor <= 0:
        print("Depósito recusado! Informe um valor maior que zero.")
        return saldo

    saldo += valor
    extrato.append(f"Depósito: + R$ {valor:.2f}")
    print("Depósito realizado com sucesso!")
    return saldo

def sacar(saldo, extrato):
    valor = float(input('Valor do Saque: '))
    if valor <= 0:
        print('Saque recusado, Valor Invalido!')
        return saldo
    if valor > saldo:
        print('Saque recusado, Valor Insuficiente!')
        return saldo
    saldo -= valor
    extrato.append(f'Saque: R$ {valor}')
    print('Saque realizado!')
    return saldo


def exibir_menu():
    
    print("""
    === BANCO COFRINHO - CAIXA ====
    1 - ver saldo
    2 - deporsitar
    3 - sacar
    4 - ver extrato
    0 - sair
    """)


saldo = 500
extrato = []


while True:
    os.system("cls")
    exibir_menu()

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            mostrar_saldo(saldo)
            input("Presione qualquer tecla para voltar ao menu...")
        case "2":
            saldo = depositar(saldo, extrato)
            input("Pressione qualquer tecla para voltar ao menu...")
        case "3":
            saldo = sacar(saldo, extrato)
            input(" Pressione qualquer tecla para voltar ao menu...")
        case "4":
            mostrar_extrato(extrato)
            input(" Pressione qualquer tecla para voltar ao menu...")
            
        case "0":
            print("\n=Saindo do caixa...")
            break
        case _:
            print("\n=Opção Invalida! =")
            input("Pressione Enter para tentar novamente")


