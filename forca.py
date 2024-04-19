from boneco_forca import desenhar_boneco
import random
from boneco_forca import lista


#ganhou = False
resposta  = ""

while resposta != "n":
    
    if resposta == "s" or resposta == "":   

        palavra = random.choice(lista)
        letra_usuario = []
        chances = 5
        erros = 0

        while chances >= 0:  
            #ganhou = all(letra.lower() in letra_usuario for letra in palavra)
            ganhou = True
            for letra in palavra:
                if letra.lower() not in letra_usuario:
                    ganhou = False

            if ganhou:
                break  
            #logica do jogo    
            for letra in palavra:        
                if letra.lower() in letra_usuario:
                    print(letra, end= " ")

                else:
                    print("_", end= " ")
            print("\n") 

            tentativa = input("Digite uma letra: ").lower().strip() # Converte para minúsculas e remove espaços extras   

            if len(tentativa) != 1 or not tentativa.isalpha():  # Verifica se a entrada é válida
                print("Por favor, digite apenas uma letra.")
                continue
        

            if tentativa in letra_usuario:
                print(f"Você ja digitou a letra: {tentativa}")

            else:

                letra_usuario.append(tentativa)

                if tentativa not in palavra:         
                    erros += 1
                    print(f"\nVocê errou, você tem {chances} chances")
                    desenhar_boneco(erros)
                    chances -= 1
                else:
                    
                    print(f"Você acertou uma letra! ") 
                    
            
                    
        
        if ganhou:
            print(f"Parabens você ganhou o jogo. A palavra era: {palavra}")
            print(" ")
            print("""
        |.-----.|
        |<> ^ <>|
        ||_.-._||
        `--)-(--`
       __[=====]___
      |::::::::::::|\
                  
      `-=========-`  """)
            print(" ")

        else:
            print(f"Você perdeu! A palavra era {palavra}")
            print("")
            print("""

   .-'---'-.
 .'  .-.-.  `.
/ |--| | |--| \\                  
| |  `-^-'  | |
\_/   (_)   \_/
||           ||
\_)         (_/
  ".       ."
    |  |  |
    |  |  |        
   (___|___)
""") 
            print(" ")

    resposta = input("Deseja jogar o jogo da forca ? ( s/n ): ")

#galdino Juunior realizado em 19/04

  
