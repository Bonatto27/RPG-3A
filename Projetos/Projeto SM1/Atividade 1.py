import random


vida = 10

arvores = 0


for hora in range(3): # 3 horas

    print(f"\nHora {hora+1}: O lenhador cortou uma árvore.")

    print("O goblin apareceu!")

    acao = input("Você escolheu que o lenhador iria correr ou lutar? ").lower()


    if acao == "correr":

        if random.random() < 0.5:

            print("O lenhador correu, mas não conseguiu levar a árvore!")

        else:

            arvores += 1

            print("O lenhador correu e conseguiu levar a arvore.")

    elif acao == "lutar":

        vida -= 2

        arvores += 1

        print("O lenhador lutou e levou 2 de dano. Vida restante:", vida)

    else:

        vida = 0

        print("Ação inválida! ele fica parado e o goblin o ataca, tirando toda a vida dele, resultando em morte imediata!!")

        print("O Lenhador morreu!")

        break


    if vida <= 0:

        print("O Lenhador morreu!")

        break


# Calculo das estacas

estacas = 0

for i in range(arvores):

    estacas += random.randint(5, 7)


print(f"\nFim do dia. Árvores coletadas: {arvores}, Vida restante: {vida}")

print(f"Você conseguiu {estacas} estacas no total.")

