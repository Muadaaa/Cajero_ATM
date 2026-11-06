# =============================================================================
#  CAJERO ATM POR CONSOLA  


SALDO_INICIAL = 10000.0
RETIRO_MAXIMO = 7000.0
PIN_CORRECTO = 7777


saldo = SALDO_INICIAL



for x in range (4, 0, -1):
    pin_escrito = int(input('Ingresa tu PIN: '))
    if pin_escrito == PIN_CORRECTO:
        print('Acceso concedido')
        acceso = True
        break
    else:
        print(f'Te quedan {x-1} intetos')
        acceso = False



if acceso == False:
    print('Tarjeta retenida')
    exit()



opcion = 0
while( opcion != 4):
    print(""" 
          1) Consultar saldo
          2) Depositar 
          3) Retirar
          4) Salir
          """)
    opcion = int(input('¿Qué operación deseas realizar? '))




    if opcion == 1:
        print('====================================')
        print(f'Tu saldo es de ${saldo}')
        print('====================================')




    elif opcion == 2:
        monto = float(input('Coloca el monto a depositar: '))
        if monto >= 0:
            saldo += monto
            print('====================================')
            print(f'Tu saldo ahora es de ${saldo}')
            print('====================================')
        else:
            print('====================================')
            print('Monto invalido, ingresa una cantidad positiva')
            print('====================================')





    elif opcion == 3:
        monto = float(input('¿Qué cantidad desea retirar? '))
        if monto <= 0:
            print('====================================')
            print('Cantidad invalida')
            print('====================================')
        elif monto > RETIRO_MAXIMO:
            print('====================================')
            print('Excede el retiro máximo por operación')
            print('====================================')
        elif monto > saldo:
            print('====================================')
            print('Fondos insuficientes')
            print('====================================')
        else:
            saldo -= monto
            print('====================================')
            print(f' Ha retirado ${monto}')
            print(f' Su saldo ahora es de ${saldo}')
            print('====================================')




    elif opcion == 4:
        print('====================================')
        print('¡Gracias por usar nuestro cajero!')
        print('Buen día')



    else:
        print('====================================')
        print('Opción no valida, intenta nuevamente')
