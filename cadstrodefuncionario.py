import json
import os 

ARQUIVO = 'funcionarios.json'

def carregar_funcionarios():
    if os.path.exists(ARQUIVO):
        if os.path.exists(ARQUIVO):
            with open(ARQUIVO, 'r') as f:
                return json.load(f)
    return {}

def salvar_funcionarios(funcionarios):
           with open(ARQUIVO, 'w') as f:
                json.dump(funcionarios, f, indent=4)

def gerar_id(funcionarios):
     if funcionarios:
          return str(int(max(funcionarios.keys())) +1)
     return "1"

def validar_cpf(cpf):
     return cpf.isdigit() and len(cpf) == 11

def adicionar_funcionario(funcionarios):
     nome = input("Nome: ")
     cargo = input("Cargo: ")

     while True:
          cpf = input("CPF (apenas números): ")
          if validar_cpf(cpf):
               break
          print("CPF inválido. Deve conter 11 números.")


     salario = float(input("Salário: "))
     email = input("Email: ")
    

     id_func = gerar_id(funcionarios)
     funcionarios[id_func] = {
          "Nome": nome,
          "Cargo": cargo,
          "cpf": cpf,
          "Salario": salario,
          "Email": email
     }
     print(f"Funcionário {nome} cadastrado com ID {id_func}.")

def listar_funcionarios(funcionarios):
     if not funcionarios:
          print("Nenhum funcionário cadastrado.")
     else: 
          for id_func, dados in funcionarios.items():
               print(f"\nID: {id_func}")
               for chave, valor in dados.items():
                    print(f"{chave.capitalize()}: {valor}")

def buscar_funcionario(funcionarios):
     busca = input("Digite o ID, nome , ou cpf do funcionario: ").lower()
     encontrado = False
     for id_func, dados in funcionarios.items():
          if (
               busca == id_func
               or busca in dados["nome"].lower()
               or busca in dados["cpf"].lower()
           ):   
               print(f"\nID: {id_func}")
               for chave, valor in  dados.items():
                    print(f"{chave.capitalize()}: {valor}")
               encontrado = True
     if not encontrado: 
               print("Funcionário não encontrado.")   

def atualizar_funcionario(funcionarios):
     id_func = input("Digite o ID do Funcionário para atualizar: ")
     if id_func in funcionarios:
           print("Deixe em branco, para manter oa valor atual.")
           atual = funcionarios[id_func]

           nome = input(f"Novo nome ({atual['nome']}): ") or funcionarios[id_func]['nome']
           cargo = input(f"Novo Cargo ({atual['cargo']}): ") or funcionarios[id_func]['cargo']

           novo_cpf = input(f"CPF ({atual['cpf']}): ") or funcionarios[id_func]
           if novo_cpf:
                while not validar_cpf(novo_cpf):
                     print("CPF inválido. deve conter 11 números.")
                     novo_cpf = input("Novo CPF: ")
           else: 
                novo_cpf = funcionarios  [id_func]['cpf']        

           salario = input(f"Novo Salário: ({atual['salario']})") or funcionarios[id_func]['salario']
           email = input(f"Novo Email: ({atual['email']})") or funcionarios[id_func]['email']

           funcionarios[id_func] = {
                "Nome": nome,
                "Cargo": cargo,
                "CPF": novo_cpf,
                "Salario": float(salario),
                "Email": email
           }
           print("Funcioário atualizado com sucesso.") 
     else:
          print("ID não encontrado.")
    
def remover_funcionario(funcionarios):
     id_func = input("Digite o ID, para remoever o funcionário: ")
     if id_func in funcionarios:
            confirm = input(f"Deseja remover {funcionarios[id_func]['nome']}? (s/n): ")
            if  confirm.lower() == 's':
                 del funcionarios[id_func]
                 print("Funcionário removido com sucesso.")
            else:
                 print("Ação cancelada.")
     else:
            print("ID não encontrado.")

def menu():
     funcionarios = carregar_funcionarios()
     
     opcoes = {
          '1': adicionar_funcionario,
          '2':listar_funcionarios,
          '3':buscar_funcionario,
          '4':atualizar_funcionario,
          '5':remover_funcionario
     }                

     while True:
          print(""""
  ___Menu Funcionário___
  1. Adicionar_funcionário
  2. Listar_funcionário                            
  3. Buscar_funcionário           
  4. Atualizar_funcionário
  5. Remover_funcionário   
  6. Sair                         
""")
          escolha = input("Escolha uma das opções: ")
          if escolha == '6':
               salvar_funcionarios(funcionarios)
               print("Saindo...Dados salvos.")
               break
          elif escolha in opcoes:
               opcoes[escolha](funcionarios)
          else :
               print("Opeção inválida.")

if __name__ == "__main__":
     menu()


                    








       


          
