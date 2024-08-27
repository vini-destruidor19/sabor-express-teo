import os

def mostra_titulo():
      print("""
            𝓘𝓶𝓹𝓮́𝓻𝓲𝓸 𝓓𝓸 𝓢𝓸𝓻𝓿𝓮𝓽𝓮
            """)

def mostra_escolha():
      print("1. cadrastrar ")
      print("2. historia")
      print("3.lojas")
      print("4. produtos")
      print("5.sair")

def escolhe_opcao():
      
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
                  print("você escolheu se cadrastrar")
            elif opcao_escolhida == 2:
                  print("você escolheu ver a historia")
            elif opcao_escolhida == 3:
                  print("você escolheu descubrir as nossas lojas")
            elif opcao_escolhida == 4:
                  print("você escolheu ver os produtos")
            elif opcao_escolhida == 5:
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



