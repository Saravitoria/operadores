# -*- coding: utf-8 -*-
"""AlunoMedia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x0ukyxFVyWVhUnoqwpfkg26j-iu3nhto
"""

idade_renata = 14
idade_fabiana = 18
dinnheiro_iara = 5000.00

if (idade_renata >= 14 and idade_fabiana == 18 or dinheiro_iara == 5000.00 ):
    situação = 'vai viajar'
else:
    situação = 'não vai viajar'

print(f'rodrigo {situação} para portugal')

sabeSambar = 'sim'
gostaFeijoada = 'não'
torceSelecaoBrasileira = 'sim'

if (sabeSambar == 'sim' or gostaFeijoada == 'sim' and torceSelecaoBrasileira == 'sim'):
    print('Esse é brasileiro')
else:
    print('Esse nao é brasileiro')

temDentes = 'sim'
temFome = 'nao'
gosta = 'sim'

if temDentes == 'sim':
    TDcondicao = 'verdadeiro'
elif temDentes == 'nao':
    TDcondicao = 'falso'

if temFome == 'sim':
    TFcondicao = 'verdadeiro'
elif temFome == 'nao':
    TFcondicao = 'falso'

if gosta == 'sim':
    Gcondicao = 'verdadeiro'
elif gosta == 'nao':
    Gcondicao = 'falso'

if Gcondicao == 'falso' or TFcondicao == 'falso':
    GTFcondicao = 'falso' 
else:
    GTFcondicao = 'verdadeiro'

if GTFcondicao == 'verdadeiro' and TDcondicao == 'verdadeiro':
    Fcondicao = 'verdadeiro'
else:
    Fcondicao = 'falso'

print(f'a pessoa precisa ter dentes {TDcondicao} e ter fome {TFcondicao} ou gostar de maca {Gcondicao}')

aluno = input('digite o nome do aluno: ')
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))
media = (n1+n2+n3/3)
if media >= 7:
    situacao = 'aprovado'
elif media >= 4:
    situacao = ' em recuperacao'
else:
    situacao = 'reprovado'
print(f'o aluno {aluno} esta em situacao {situacao} com media {media} ')