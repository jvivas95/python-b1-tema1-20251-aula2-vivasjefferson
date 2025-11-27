'''
Jefferson Vivas

Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH

'''

def invert_text(text_chain:str):
    # Write here your code
    new_text_chain=''
    if text_chain =="":
        return text_chain
    elif not str(text_chain):
        raise ValueError("Error")
    else:
        for letra in reversed(text_chain):
            new_text_chain=new_text_chain+letra
        return new_text_chain

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(invert_text("987654321"))
