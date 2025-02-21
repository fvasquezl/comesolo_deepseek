import math
from typing import List, Dict


class Comesolo:
    def __init__(self):
        self.tablero: List[int] = [1] * 15
        self.no_niveles: int = self.calcular_niveles(len(self.tablero))
        self.movimientos: Dict[str, str] = {}
        self.jugando: bool = True

    def reiniciar_tablero(self):
        self.tablero = [1] * 15
        print("Tablero reiniciado.")

    @staticmethod
    def calcular_niveles(longitud_tablero):
        n = (-1 + math.sqrt(1 + 8 * longitud_tablero)) / 2
        return int(n)

    @staticmethod
    def valor_maximo(max_level):
        return (max_level * (max_level + 1) // 2) - 1

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

    def obtener_nivel_de_una_ficha(self, posicion):
        nivel = 1
        total = 0
        while total <= posicion:
            total += nivel
            nivel += 1
        return nivel - 1

    def triangular_next_element(self, level):
        return level * (level + 1) // 2
    
    def children(self, level, inc):
        return self.triangular_next_element(level) + inc

    def buscar_izquierda(self):
        # numero de niveles -2
        max_level = self.no_niveles - 2

        for i in list(range(0, self.valor_maximo(max_level))):
            if self.tablero[i] == 0:
                f_level = self.obtener_nivel_de_una_ficha(self.tablero[i])
                hijo=self.tablero[self.children(f_level+1, i*f_level)]
                if(hijo==1):
                    print('hijo')
                    nieto = self.tablero[self.children(f_level+2, i*f_level)]
                    if(nieto==1):
                        print('nieto')
                        print(i,self.children(f_level+1, i*f_level),self.children(f_level+2, i*f_level)) 




    def jugar(self):
        print("¡Bienvenido al juego Come Solo!")
        print("Tablero inicial:")
        self.imprimir_tablero()
        # Solicitar el movimiento inicial al jugador
        self.primer_movimiento()
        self.buscar_izquierda()


if __name__ == "__main__":
    # Jugar el juego
    juego = Comesolo()
    juego.jugar()


#             1                 1  0
#           2   3               2  1
#         4   5   6             3  1 1
#       7   8   9   10          4  1 1 1
#     11  12  13  14  15        5  1 1 1 1

#             0                 1  0
#           1   2               2  1
#         3   4   5             3  1 1
#       6   7   8   9          4  1 1 1
#     10  11  12  13  14        5  1 1 1 1
#
#     i*(i+1)//2

# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
