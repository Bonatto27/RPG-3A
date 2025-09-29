 
import random

import time

# Configurações iniciais

estacas_disponiveis = 2

lenhador = 4

minerador = 10

ferreiro = 10

plantacoes = 7  # nova variável para contar plantações


print("Início do dia...")

time.sleep(1)

investidas = random.randint(2, 3)


for i in range(investidas):

    print(f"\nInvestida {i+1}")


    goblins = random.randint(2, 5)

    print(f"{goblins} goblins estão atacando!")

    time.sleep(1)

    for j in range(goblins):

        print(f"\nGoblin #{j+1} está tentando atravessar!")

        time.sleep(1)

        if estacas_disponiveis > 0:

            chance = random.randint(1, 100)

            if chance >= 31:

                print(f"Estaca bloqueou o goblin! (porcentagem = {chance})")

            else:

                estacas_disponiveis -= 1

                print(f"Estaca destruída! Goblin conseguiu passar! (porcentagem = {chance})")

                time.sleep(1)

                escolha = input("Você quer enfrentar o goblin? (s/n): ").strip().lower()

                if escolha == "s":

                    print("Você enfrentou o goblin!")

                else:

                    print("Goblin atacou os moradores!")

                    queima = random.randint(1, 100)

                    if queima <= 5:

                        print("VOCÊ PERDEU UMA PLANTAÇÃO!")

                        plantacoes -= 1

                    else:

                        print("1 dano causado aos moradores.")

                        lenhador -= 1

                        minerador -= 1

                        ferreiro -= 1

        else:

            print(f"Sem estacas! Goblin passou direto! (porcentagem = {chance})")

            escolha = input("Você quer enfrentar o goblin? (s/n): ").strip().lower()

            if escolha == "s":

                print("Você enfrentou o goblin!")

            else:

                print("Goblin atacou os moradores!")

                queima = random.randint(1, 100)

                if queima <= 5:

                    print("VOCÊ PERDEU UMA PLANTAÇÃO!")

                    plantacoes -= 1

                else:

                    lenhador - 1

                    minerador - 1

                    ferreiro - 1

                    print("1 dano causado aos moradores.")


# Fim do dia

print(f"\nFim do dia.")

print(f"Estacas restantes: {estacas_disponiveis}")

print(f"Vida do lenhador {lenhador}")

print(f"vida do minerador {minerador}")

print(f"vida do ferreiro {ferreiro}")

print(f"Plantações restantes: {plantacoes}")



