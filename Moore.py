class MooreAutomaton:
    def __init__(self):
        self.state = 'S0'  # Estado inicial

    def next_state(self, input_bit):
        # Estado S0
        if self.state == 'S0':
            if input_bit == '0':
                self.state = 'S0'
                return '0'
            elif input_bit == '1':
                self.state = 'S1'
                return '1'
        
        # Estado S1
        elif self.state == 'S1':
            if input_bit == '0':
                self.state = 'S0'
                return '0'
            elif input_bit == '1':
                self.state = 'S2'
                return '0'
        
        # Estado S2 (se reemplaza el segundo '1' por '0' y vuelve a S0)
        elif self.state == 'S2':
            if input_bit == '0':
                self.state = 'S0'
                return '0'
            elif input_bit == '1':
                self.state = 'S1'
                return '1'

    def process(self, input_string):
        output = ''
        for bit in input_string:
            output += self.next_state(bit)
        return output

# Solicitar secuencia de entrada al usuario
input_sequence = input("Ingrese una secuencia de '1' y '0': ")

# Crear instancia del autómata y procesar la entrada
automaton = MooreAutomaton()
output_sequence = automaton.process(input_sequence)

# Mostrar la salida
print(f"Secuencia de entrada: {input_sequence}")
print(f"Secuencia de salida: {output_sequence}")
