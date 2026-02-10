import random
# módulo random - desenvolvido para gerar numeros randomicos

print("Seja bem vindo ao jogo de adivinhação de números!")
choice_number = input("Digite o número teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro! O valor informado não é numérico. Favor execute novamente e informe um numero")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input("Adivinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro! O valor informado não é numérico. Favor execute novamente e informe um numero")
        continue
    
    n_choices = n_choices + 1
    
    if answer_user == random_number:
        print('Acertou!')
        break
    
    elif answer_user > random_number:
        print('Chutou alto! O número é menor...')
    else:
        print('Chutou baixo! O número é maior...')
    
print('Número de tentativas: ' + str(n_choices))