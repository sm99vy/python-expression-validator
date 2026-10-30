pilha = []
correto = True

expressao = str(input('Digite a expressão: ')).strip()
for count in range(len(expressao)):
    if expressao[count] == '(':
        pilha.append('(')
    elif expressao[count] == ')':
        if pilha:
            pilha.pop()
        else:
            correto = False
            
if correto == True and pilha == []:
    print('Sua expressão está correta !')
else:
    print('Sua expressão está errada !')