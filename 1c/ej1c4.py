""" 
Jefferson Vivas

Enunciado:
Escribe una función llamada is_palindrome(word) que reciba como parámetro
una cadena word y verifique si es un palíndromo utilizando recursión.
La función debe devolver True si la cadena es un palíndromo y False en
caso contrario.

Parámetros:
    word (str): una cadena de caracteres.

Ejemplo:
    Entrada:
    word = "racecar"
    print(is_palindrome(word))

    Salida:
    True

"""


def is_palindrome(word):
    # Write here your code
    if len(word) <= 1:
        return True
    
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
    
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# word = "level"
# print(f"Is '{word}' word palindrome?", is_palindrome(word))
#
# word = "juan"
# print(f"Is '{word}' word palindrome?", is_palindrome(word))
