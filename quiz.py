print('Seja bem vindo ao quiz! Teste seus conhecimentos de programação!')
resposta_usuario = input('Quer continuar? (S/N) ')

if resposta_usuario != 'S':
    quit()
    
score = 0
    
print('Começando...')
print('1. Qual é a principal função de uma "variável" em programação?')
print(' (A) Executar um loop repetidamente \n (B) Exibir imagens na tela \n (C) Compilar o código fonte \n (D) Armazenar dados para uso posterior no programa') 
repsosta_1 = input('Resposta: ')

if repsosta_1 == "D":
    print("Resposta certa!\n")
    score = score + 1
else:
    print("Resposta errada\n")
    
print('2.O que acontece se a condição de um loop "while" nunca se tornar falsa?')
print(' (A) A variavel é deletada \n (B) Cria-se um loop infinito \n (C) Ocorre um erro de sintaxe \n (D) O programa termina imediatamente') 
repsosta_2 = input('Resposta: ')

if repsosta_2 == "B":
    print("Resposta certa!\n")
    score = score + 1
else:
    print("Resposta errada\n")
    
    
print('3. Em muitas linguagens de programação (como Python, C e JavaScript), qual é o índice do primeiro elemento de um array (vetor)?')
print(' (A) 1 \n (B) 0 \n (C) -1 \n (D) 10') 
repsosta_3 = input('Resposta: ')

if repsosta_3 == "B":
    print("Resposta certa!\n")
    score = score + 1
else:
    print("Resposta errada\n")
  
    
print('4. Qual operador lógico retorna verdadeiro (True) apenas se AMBAS as condições forem verdadeiras?')
print(' (A) XOR (OU exclusivo) \n (B) OR (OU) \n (C) NOT (NÃO) \n (D) AND (E)') 
repsosta_4 = input('Resposta: ')

if repsosta_4 == "D":
    print("Resposta certa!\n")
    score = score + 1
else:
    print("Resposta errada\n")
 
    
print('5. O que é um "bug" no contexto de desenvolvimento de software?')
print(' (A) Um erro ou falha no código que causa um comportamento inesperado  \n (B) Uma ferramenta para escrever o código mais rápido \n (C) Um recurso de segurança do sistema \n (D) Um tipo de vírus de computador')
repsosta_5 = input('Resposta: ')	

if repsosta_5 == "A":
    print("Resposta certa!\n")
    score = score + 1
else:
    print("Resposta errada\n")

print(f"Você chegou no final do quiz... sua pontuação é {score}/5")   