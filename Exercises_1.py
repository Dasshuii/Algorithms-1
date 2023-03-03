""" Codigo python ejercicios primera semana, tomado del ejemplo del profesor
    Date: 02-03-2023
    Author: Daniel Ramirez Calvo
"""

def saludar_1(veces, msg):
    """ Sirve saludar una cantidad de veces por consola """
    print('saludar_1')
    for i in range(veces):
        print(msg)
        print('taraaan')
    """ 
        n | print
        0 | 0
        1 | 2
        2 | 4
        3 | 6
        4 | 8
        
        Algoritmo utilizado al recibir nuestra entrada (veces o n) es (n * 2[prints del for])

        ∴T_1(n) = n * 2 para ∀n >= 0
        ∴O(n)
    """

def saludar_2(veces, msg):
    """ Sirve saludar una cantidad de veces por consola """
    print('saludar_2')
    veces *= 2
    for i in range(2, veces + 1):
        print(msg)
    print('taraaan')

    """
        n | print
        0 | 0 
        1 | 1   
        2 | 3   
        3 | 5
        4 | 7
        
        Algoritmo utilizado al recibir entrada (veces o n) es 
        (n * 2 [el producto en la linea 29]) - 1 [por range(start=2)]

        O como alternativa n + (n - 1) puesto que n*2 = n + n, solo que se le resta el 1 por el start del range
        ∴T_2(n) = (n * 2) - 1 ∀n != 0 || n + (n - 1) ∀n != 0
        ∴O(n)
    """

def saludar_3(veces, msg):
    """ Sirve saludar una cantidad que depende de veces por consola"""
    print('saludar_3')
    for j in range(veces):
        for i in range(veces):
            print(msg)
    print('taraaan')

    """
        n | print
        0 | 0
        1 | 1
        2 | 4
        3 | 9
        4 | 16

        Algoritmo utilizado al recibir entrada (veces o n) es
        (n² [al estar dentro de un for anidado])

        ∴T_3(n) = n² ∀n >= 0
        ∴O(n²)
    """

def saludar_4(veces, msg):
    """ Sirve saludar una cantidad que depende de veces por consola"""
    print('saludar_4')
    for j in range(veces):
        for i in range(j + 1, veces):
            print(msg)
            print('taraaan')
    """
        n | print
        0 | 0
        1 | 0
        2 | 2 
        3 | 6 
        4 | 12 
        5 | 20 
        6 | 30

        Algoritmo utilizado al recibir entrada (veces o n) es
        (n²[por estar dentro de un for anidado] - n [por el aumento del start del range])

        ∴T_4(n) = n² - n ∀n > 0
        ∴O(n²)
    """


"""
Probar saludar(n) con valores
    saludar_n(veces=1, msg="Fresco Leche")
"""