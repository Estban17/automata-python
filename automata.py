# Definimos los estados del autómata
class Estados:
    q0 = 0
    q1 = 1
    q2 = 2

# Función para procesar una palabra en el autómata
def proceso(entrada):
    estado = Estados.q0  # El estado inicial es q0

    for i in entrada:
        if estado == Estados.q0:
            if i == 'a':
                estado = Estados.q1  # Transición de q0 a q1 con 'a'
            elif i == 'b':
                estado = Estados.q2  # Transición de q0 a q2 con 'b'
            else:
                return False  # Caracter inválido
        elif estado == Estados.q1:
            if i == 'a':
                estado = Estados.q1  # Transición de q1 a q1 con 'a'
            elif i == 'b':
                estado = Estados.q1  # Transición de q1 a q1 con 'b'
            else:
                return False  # Caracter inválido
        elif estado == Estados.q2:
            if i == 'a':
                estado = Estados.q0  # Transición de q2 a q0 con 'a'
            elif i == 'b':
                estado = Estados.q2  # Transición de q2 a q2 con 'b'
            else:
                return False  # Caracter inválido

    # El autómata acepta la palabra si termina en el estado de aceptación q1
    return estado == Estados.q1 or estado == Estados.q2

def main():
    palabra = input("Ingresa una palabra: ")

    if proceso(palabra):
        print("La palabra es aceptada por el autómata.")
    else:
        print("La palabra NO es aceptada por el autómata.")

if __name__ == "__main__":
    main()