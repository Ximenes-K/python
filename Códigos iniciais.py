usuário= (input('digite seu nome: '))
alunos = {'Ana Carolina','Antonio', 'Andressa', 'Bruno','Breno', 'Bianca'}
if usuário not in alunos: 
    print ('você não é dessa turma')
elif usuário in alunos:
    n1=int(input('Informe a nota da N1: '))
    n2=int(input('informe a nota da N2: '))
    peso_1=float(input('informe o peso da N1: '))
    peso_2=float(input('informe o peso da N2: '))
# só interessa a parte inteira da média.
    media=(n1*peso_1 + n2*peso_2)//(peso_1 + peso_2)
    aprovados= media < 7
print('a sua média final é:',media)
if media > 7:
    print('você está aprovado,Boas festas!')
elif media == 7:
    print('você está de exame')
elif 5 < media < 7:
    print('Faça um trabalho para ajudar na nota' )
else:
    print('você está reprovado sem recuperação')



