"""
SaldoFalado - Converta valor monetário em texto falado

Author: Charles Oliveira
Contact: neo_charles@outlook.com

Version 1.3

Alterações:
    - correção de bugs
    - tratamento de entradas incorretas ('42', ',99', '1,2345')
    - implementado retorno de 'saldo zerado'
    - atribuido constantes para numero de casas: 4 para Reais e  2 para centavos
    - Tratado centavos > 99 dentro da função
    - Tratar valor dentro da função
    - Adicionado comentários no código
    

Issues:
    - Adicionar biblioteca de fala

"""

def convTexto(valor):
    """
    retorna como se lê o valor numérico inserido
    """
#Constantes
    MAX_NUMERO_DE_CASAS = 4

#Variaveis
    valorMilhar = 0
    valorCentena = 0
    valorDezena = 0
    valorUnidade = 0

#Trata Valor de Entrada
    valor = valor[::-1]

    valorUnidade = int(valor[0])
    valorDezena = int(valor[1])

    if len(valor) > 2:
        valor = valor[:MAX_NUMERO_DE_CASAS:]
        valorCentena = int(valor[2])
        valorMilhar = int(valor[3])

    valor = int(valor) 

#Trata as unidades
    unidade = {0:'', 1:'um', 2:'dois', 3:'tres', 4:'quatro', 5:'cinco', 6:'seis', 7:'sete', 8:'oito', 9:'nove'}

    if valorDezena == 1:
        retUnidade = ''
    else:
        retUnidade = unidade[valorUnidade]
    
#Trata as dezenas
    dezena = {0:'', 1:'dez', 2:'vinte', 3:'trinta', 4:'quarenta', 5:'cinquenta', 6:'sessenta', 7:'setenta', 8:'oitenta', 9:'noventa'}
    dezena1 = {0:'dez', 1:'onze', 2:'doze', 3:'treze', 4:'quatorze', 5:'quinze', 6:'dezeseis', 7:'dezesete', 8:'dezoito', 9:'dezenove'}
    dezena2 = {0:'', 1:'', 2:'vinte e ', 3:'trinta e ', 4:'quarenta e ', 5:'cinquenta e ', 6:'sessenta e ', 7:'setenta e ', 8:'oitenta e ', 9:'noventa e '}
   

    if valorDezena == 1:
        retDezena = dezena1[valorUnidade]

    else:
        if valorUnidade > 0:
            retDezena = dezena2[valorDezena]
        else:
            retDezena = dezena[valorDezena]

#Trata a Centena
    centena = {0:'', 1:'cem', 2:'duzentos', 3:'trezentos', 4:'quatrocentos', 5:'quinhentos', 6:'seissentos', 7:'setecentos', 8:'oitocentos', 9:'novecentos'}
    centena1 = {0:'', 1:'cento e ', 2:'duzentos e ', 3:'trezentos e ', 4:'quatrocentos e ', 5:'quinhentos e ', 6:'seissentos e ', 7:'setecentos e ', 8:'oitocentos e ', 9:'novecentos e '}

    if valorDezena > 0 or valorUnidade > 0:
        retCentena = centena1[valorCentena]
    else:
        retCentena = centena[valorCentena]

#Trata milhar
    milhar = {0:'', 1:'um mil', 2:'dois mil', 3:'tres mil', 4:'quatro mil', 5:'cinco mil', 6:'seis mil', 7:'sete mil', 8:'oito mil', 9:'nove mil'}
    milhar1 = {0:'', 1:'um mil e ', 2:'dois mil e ', 3:'tres mil e ', 4:'quatro mil e ', 5:'cinco mil e ', 6:'seis mil e ', 7:'sete mil e ', 8:'oito mil e ', 9:'nove mil e '}
    
    if valorCentena > 0 or valorDezena > 0 or valorUnidade > 0:
        retMilhar = milhar1[valorMilhar]
    else:
        retMilhar = milhar[valorMilhar]

#Trata dezena de milhar
    """
    Espaço destinado a aplicação de melhoria futura
    """

    return retMilhar + retCentena + retDezena + retUnidade

def ConTexto(valor):
    """
    Trata [valor] numérico iserido e [imprime texto] escrito no contexto como se fala em protuguês
    """
#Constantes
    CASAS_REAIS = 4
    CASAS_CENTAVOS = 2

#Variáveis

#Trata Valor
    valor = valor.replace(',','.')
    
    if valor.isalnum():
        valor = valor + '.'

    reais, centavos = valor.split('.')

#Trata Reais
    if reais == '':
        reais = '0'
    reais = reais[:CASAS_REAIS].rjust(CASAS_REAIS,'0')

#Trata Centavos
    if centavos == '':
        centavos = '0'           
    centavos = centavos[:CASAS_CENTAVOS].ljust(CASAS_CENTAVOS,'0')

#Trata Texto e Pluralidade
    if int(centavos) == 0:
        if int(reais) > 1:
            print(convTexto(reais),'reais')

        elif int(reais) == 1:
            print(convTexto(reais),'real')

        else:            
            print('Saldo zerado')

    elif int(reais) == 0:
        if int(centavos) > 1:
            print(convTexto(centavos),'centavos')

        else:        
            print(convTexto(centavos),'centavo')

    else:
        if int(reais) > 1:
            print(convTexto(reais),'reais e', end=' ')
                
            if int(centavos) > 1:
                print(convTexto(centavos),'centavos')

            else:        
                print(convTexto(centavos),'centavo')

        else:
            print(convTexto(reais),'real e', end=' ')
                
            if int(centavos) > 1:
                print(convTexto(centavos),'centavos')

            else:        
                print(convTexto(centavos),'centavo')
                
while(True):
    valor = input('Digite um valor numerico em reais, entre 0,01 e 9999,99 (Serm R$): R$')
    
    valor = valor.replace(',','.')
    
    if valor.isalnum():
        valor = valor + '.'

    reais, centavos = valor.split('.')
    reais = reais.rjust(4,'0')
    centavos = centavos.ljust(2,'0')

    fvalor = float(reais+'.'+centavos)
    if fvalor > 0.0 and fvalor <= 9999.99:
        break

ConTexto(valor)