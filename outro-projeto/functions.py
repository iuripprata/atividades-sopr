def menu():
    print("•----------------------------------------------•")
    print('⁜{:^43}⁜'.format('⁂CONVERSOR DE MEDIDAS⁂'))
    print("•----------------------------------------------•")
    print('¦{:45s}¦'.format('1 - TEMPERATURA'))
    print('¦{:45s}¦'.format('2 - COMPRIMENTO'))
    print('¦{:45s}¦'.format('3 - SAIR'))
    print("•----------------------------------------------•")
    NumMenu = int(input('SELECIONE UMA OPÇÃO: '))
    return NumMenu

def convTemp():
    while True:
        try:
            print("•----------------------------------------------•")
            print('⁜{:^43}⁜'.format('⁂CONVERSOR DE TEMPERATURAS⁂'))
            print("•----------------------------------------------•")
            print('¦{:45s}¦'.format('1 - CELSIUS → KELVIN'))
            print('¦{:45s}¦'.format('2 - CELSIUS → FAHRENHEITS'))
            print('¦{:45s}¦'.format('3 - KELVIN → FAHRENHEITS'))
            print('¦{:45s}¦'.format('4 - KELVIN → CELSIUS'))
            print('¦{:45s}¦'.format('5 - FAHRENHEITS → CELSIUS'))
            print('¦{:45s}¦'.format('6 - FAHRENHEITS → KELVIN'))
            valor = int(input('ESCOLHA A CONVERSÃO: '))
            if valor!=1 and valor!=2 and valor!=3 and valor!=4 and valor!=5 and valor!=6:
                raise Exception
            return valor
            break
        except:
            print('Por favor, insira um valor válido.')

def convComp():
    while True:
        try:
            print("•----------------------------------------------•")
            print('⁜{:^43}⁜'.format('⁂CONVERSOR DE COMPRIMENTOS⁂'))
            print("•----------------------------------------------•")
            print('¦{:45s}¦'.format('1 - METROS → QUILÔMETROS'))
            print('¦{:45s}¦'.format('2 - METROS → CENTÍMETROS'))
            print('¦{:45s}¦'.format('3 - QUILÔMETROS → CENTÍMETROS'))
            print('¦{:45s}¦'.format('4 - QUILÔMETROS → METROS'))
            print('¦{:45s}¦'.format('5 - CENTÍMETROS → QUILÔMETROS'))
            print('¦{:45s}¦'.format('6 - CENTÍMETROS → METROS'))
            valor = int(input('ESCOLHA A CONVERSÃO: '))
            if valor!=1 and valor!=2 and valor!=3 and valor!=4 and valor!=5 and valor!=6:
                raise Exception
            return valor
            break
        except:
            print('Por favor, insira um valor válido.')