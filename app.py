import os
clientes = [{"nome":"joão " , "cidade" : "foz", "bairro":" morumbi",  "ativo":True},
       {"nome":"gabriel", "cidade" : "foz", "bairro":" morumbi",  "ativo":True}]

lojas = [{"loja":"Morumbi 3", "produtos":" picoles de frutas, picoles de leite, skimo, cascão, casquinhas, milk shake e açai", "ativo":True},
       {"loja":"Primeiro de Maio", "produtos":" picoles de frutas, picoles de leite, skimo", "ativo":True}]

def mostra_titulo():
      print("""
            𝓘𝓶𝓹𝓮́𝓻𝓲𝓸 𝓓𝓸 𝓢𝓸𝓻𝓿𝓮𝓽𝓮
            """)

def mostra_escolha():
      print("1. cadrastrar_se ")
      print("2.lojas")
      print("3. produtos")
      print("4.sair")

def escolhe_opcao():

      def exibir_subtitulo(texto):
            os.system("cls")
            print(texto)
            print(" ")
      
      def retorna_menu():
            input("aperte para retonar")
            main()

      def cadrastrar_se():
            exibir_subtitulo("cadrastrar-se")
            nome_cliente = input("digite o seu nome")
            clientes.append(nome_cliente)
            print(f"o nome {nome_cliente}foi cadrastrado com sucesso\n")
            retorna_menu()

      def loja():
            exibir_subtitulo("lojas cadrastrada")
            for cliente in clientes:
                 nome = cliente["nome"]
                 cidade = cliente["cidade"]
                 ativo = cliente["ativo"]
                 print(f" - {nome} | {cidade} | {ativo}")
            
            retorna_menu()
            



      def finalizar_programa():
            os.system("cls")
            print("finalizando programa\n")
      
      def opcao_invalida():
            print("opçao invalida")
            input("Aperte para voltar ao inicio")
            main()
      try:
            opcao_escolhida = int(input("Escolha uma opção:"))
            if opcao_escolhida == 1:
                  cadrastrar_se()
            elif opcao_escolhida == 2:
                  loja()
            elif opcao_escolhida == 3:
                  print("você escolheu ver os produtos")
            elif opcao_escolhida == 4:
                  finalizar_programa()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
      mostra_titulo()
      mostra_escolha()
      escolhe_opcao()

if __name__ == "__main__":
      main()



