
def adcionar_veiculo(veiculo_estacionado):
    placa = input ("digite a placa do veiculo")
    for i in range(len(veiculo_estacionado)):
        if veiculo_estacionado[i] is None:
            veiculo_estacionado[i] = placa
            print (f"veiculo com a placa '{placa}' adicionado à vaga {i + 1}.")
            return
        print("Não ahá vagas disponiveis")
        
def remover_veiculo(veiculo_estacionado,preco_inical,preco_por_hora):
    placa_remover = input("digite a placa do veiculo a ser removido")
    veiculo_encontrado = False
    
    for i in range (len(veiculo_estacionado)):
        if veiculo_estacionado[i] == placa_remover:
            horas_estacionado = input("digite as horas que o veiculo passou estacionado")
            preco_total = preco_inical + (preco_por_hora * horas_estacionado)
            print (f"preço a ser pago pelo veiculo '{placa_remover}': R$'{preco_total:.f2}'")
            veiculo_estacionado[i] = None
            veiculo_encontrado[i] = True
            break
        if not veiculo_encontrado:
         print(f"Veiculo com a placa '{placa_remover}' não encontrado")

def listar_veiculos(veiculo_estacionado):
    veiculos_presentes = false
    print ("Veiculos estacionados")
    for i, veiculo in enumerate(veiculo_estacionado):
        if veiculo is not None:
            print (f"Vaga {i+1}: {veiculo}")
            veiculos_presentes = true
        if not veiculos_presentes:
            print ("Não há veiculos estacionados")
            
def main ():
    print ("Bme-vindo")
    quantidade_de_vagas = int(input("quantidade de vagas que deseja utilizar?"))
    veiculo_estacionado = [None] * quantidade_de_vagas
    preco_inicial = 4.0
    preco_por_hora = 2.0
    
    while true:
        print("O que deseja fazer?")
        print("1. Adicionar Veiculo")
        print("2. Remover Veiculo")
        print("3. Listar Veiculos")
        print("4. Sair")
        
        opcao = int (input("Escolha a opção"))
        if opcao == 1:
            adcionar_veiculo(veiculo_estacionado)
            
        elif opcao == 2:
            remover_veiculo(veiculo_estacionado, preco_inical, preco_por_hora)
        
        elif opcao == 3:
            listar_veiculos(veiculo_estacionado)
        
        elif opcao == 4:
            print ("Obrigada por utilizar nossos serviços")
            break
            
        else:
            print("Opção invalida")
        
if __name__ == "main":
    main()