'''
Jefferson Vivas

Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado 
'fibonacci_number'  y devuelva el valor de la serie Fibonacci en esa posición.
Asimismo, si el valor no es numérico, o es menor a cero, se debe lanzar 
una excepción ValueError("mensaje"), la cual puede incluir un mensaje que debería 
corresponder con el tipo de error durante la validación.

Parámetros:
- fibonacci_number: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

Ejemplo:
    Entrada:
    fibonacci(10)

    Salida:
    55

'''

def fibonacci(fibonacci_number):
    # Write here your code
    if not isinstance(fibonacci_number, int):
        raise ValueError("Error")
    elif fibonacci_number < 0:
        raise ValueError("Error")
    else:
        # Contador para las iteraciones
        i=0
        # Variable que acumulará el número que se irá sumando, 
        acum=0
        # Variable auxiliar que contendrá el número anterior para irlo sumando con el acumulado
        aux=1
        while i <fibonacci_number:
            acum = acum + aux
            aux  = acum - aux
            i+=1
    return acum

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(fibonacci("fsa"))
