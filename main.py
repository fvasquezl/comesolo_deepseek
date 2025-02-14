

class Comesolo:
    def __init__(self):
        self.tablero = [1]*15
        self.movimientos = {}
        self.jugando = True

    def reiniciar_tablero(self):
        self.tablero = [1] * 15
        print("Tablero reiniciado.")
    

    def imprimir_tablero(self):
        for i in range(5):  # 5 niveles en el triángulo
            # Calcular el inicio y fin de cada fila usando la fórmula de números triangulares
            inicio = i * (i + 1) // 2
            fin = inicio + i + 1

            fila = self.tablero[inicio:fin]  # Obtener la fila actual 

            # Preparar la fila para imprimir, coloreando los 0s
            fila_str = []
            for valor in fila:
                if valor == 0:
                    fila_str.append(f"\033[33m{valor}\033[0m")  # Amarillo para 0
                else:
                    fila_str.append(f"\033[37m{valor}\033[0m")  # Blanco para 1

            # Centrar la fila y unir los elementos con espacios
            espacios = "  " * (4 - i)  # Espacios para centrar la fila
            print(espacios + "   ".join(fila_str))

    
    def primer_movimiento(self):
        # Verifica que las posiciones sean válidas
        while True:
            movimiento_inicial = int(input("Ingrese su movimiento inicial (1-15): "))
            if 1 <= movimiento_inicial <= 15:
                self.tablero[movimiento_inicial - 1] = 0
                self.imprimir_tablero()
                break
            else:
                print("Movimiento inválido. Debe ser un número entre 1 y 15.")

    def obtener_movimientos_validos(self, posicion):
        # buscar_izquierda
        
        # buscar_derecha
        # buscar+horizontal
        pass

        
            
    
    def jugar(self):
        print("¡Bienvenido al juego Come Solo!")
        print("Tablero inicial:")
        self.imprimir_tablero()
        # Solicitar el movimiento inicial al jugador
    
        self.primer_movimiento()
        


if __name__ == "__main__":

    # Jugar el juego
    juego = Comesolo()
    juego.jugar()


#           0                 0  0
#         1   2               1  1
#       3   4   5             2  1 1
#     6   7   8   9           3  1 1 1
#   10  11  12  13  14        4  1 1 1 1

# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
