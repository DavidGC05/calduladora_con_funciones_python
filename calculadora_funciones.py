# Calculadora con Funciones
# 1. Solicitar el menu en una funcion
# 2. Solicitar los valores de los operadores en una funcion
# 3. La operacion a ejecutar va en otra fuhcion por separado

def menu_funcion():
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input('Seleccione una opcion: '))
    return opcion

def pedir_valores():
    numero1 = numero2 = 0
    numero1 = float(input('Primer valor: '))
    numero2 = float(input('Segundo valor: '))
    return numero1, numero2



def operacion_ejecutar(opcion, salir):
    if opcion >= 1 and opcion <= 4:
        num_1, num_2 = pedir_valores()
    resultado = 0
    if opcion == 1:
        resultado = num_1 + num_2
        print(f'El resultado de la suma es: {resultado}')
    elif opcion == 2:
        resultado = num_1 - num_2
        print(f'El resultado de la resta es: {resultado}')
    elif opcion == 3:
        resultado = num_1 * num_2
        print(f'El resultado de la multiplicacion es: {resultado}')
    elif opcion == 4:
        resultado = num_1 / num_2
        print(f'El resultado de la division es: {resultado}')
    elif opcion == 5:
         print(f'Saliendo... ')
         salir = True
    else:
        print('Valor invalido, selleccione otra opcion...')

    return salir

print('**** Calculadora en Python con Funciones ****')
salir = False
while not salir:
    opcion = menu_funcion()
    salir = operacion_ejecutar(opcion, salir)

