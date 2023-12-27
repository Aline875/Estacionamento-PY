
def bonito():
    print("-"*40)

def adcionar_veiculo(veiculo_estacionado):
    placa = input ("digite a placa do veiculo: ")
    for i in range(len(veiculo_estacionado)):
        if veiculo_estacionado[i] is None:
            veiculo_estacionado[i] = placa
            print (f"veiculo com a placa '{placa}' adicionado à vaga {i + 1}.")
            return 
        else:
            print("\033[1;31mNão há vagas disponiveis!\033[m")
        
def remover_veiculo(veiculo_estacionado,preco_inicial,preco_por_hora):
    placa_remover = input("digite a placa do veiculo a ser removido: ")
    veiculo_encontrado = False
    
    for i in range (len(veiculo_estacionado)):
        if veiculo_estacionado[i] == placa_remover:
            horas_estacionado = float(input("digite as horas que o veiculo passou estacionado: "))
            preco_total = preco_inicial + (preco_por_hora * horas_estacionado)
            bonito()
            print (f"preço a ser pago pelo veiculo {placa_remover}: \033[1;32mR${preco_total:.2f}\033[m")
            veiculo_estacionado[i] = None
            
            break
        if not veiculo_encontrado:
         print(f"Veiculo com a placa '{placa_remover}' não encontrado!")

def listar_veiculos(veiculo_estacionado):
    veiculos_presentes = False
    print ("\033[1;33mVeiculos estacionados:\033[m")
    for i, veiculo in enumerate(veiculo_estacionado):
        if veiculo is not None:
            print (f"Vaga {i+1}: {veiculo}")
            veiculos_presentes = True
        elif not veiculos_presentes:
            print ("\033[1;31mNão há veiculos estacionados!\033[m")
            
def main ():
    print ("Bem-vindo :)")
    quantidade_de_vagas = int(input("quantidade de vagas que deseja utilizar? "))
    veiculo_estacionado = [None] * quantidade_de_vagas
    preco_inicial = 4.0
    preco_por_hora = 2.0
    
    while True:
        bonito()
        print("O que deseja fazer?")
        print("1. Adicionar Veiculo")
        print("2. Remover Veiculo")
        print("3. Listar Veiculos")
        print("4. Sair")
        bonito()
        opcao = int (input("Escolha a opção: "))
        bonito()
        if opcao == 1:
            adcionar_veiculo(veiculo_estacionado)
            
        elif opcao == 2:
            remover_veiculo(veiculo_estacionado, preco_inicial, preco_por_hora)
        
        elif opcao == 3:
            listar_veiculos(veiculo_estacionado)
        
        elif opcao == 4:
            print ("Obrigada por utilizar nossos serviços")
            break
            
        else:
            print("Opção invalida")
        
main()
