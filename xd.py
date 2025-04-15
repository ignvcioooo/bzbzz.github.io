import random

#definimos las cartas y sus valores
Mazo = [
  # Corazones
    'A de ♥', '2 de ♥', '3 de ♥', '4 de ♥',
    '5 de ♥', '6 de ♥', '7 de ♥', '8 de ♥',
    '9 de ♥', '10 de ♥', 'J de ♥', 'Q de ♥',
    'K de ♥',

    # Diamantes
    'A de ♦', '2 de ♦', '3 de ♦', '4 de ♦',
    '5 de ♦', '6 de ♦', '7 de ♦', '8 de ♦',
    '9 de ♦', '10 de ♦', 'J de ♦', 'Q de ♦',
    'K de ♦',

    # Tréboles
    'A de ♣', '2 de ♣', '3 de ♣', '4 de ♣',
    '5 de ♣', '6 de ♣', '7 de ♣', '8 de ♣',
    '9 de ♣', '10 de ♣', 'J de ♣', 'Q de ♣',
    'K de ♣',

    # Picas
    'A de ♠', '2 de ♠', '3 de ♠', '4 de ♠',
    '5 de ♠', '6 de ♠', '7 de ♠', '8 de ♠',
    '9 de ♠', '10 de ♠', 'J de ♠', 'Q de ♠',
    'K de ♠', ]

VALORES_CARTAS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1,
}

#función para obtener el valor total de una mano
def calcular_valor(mano):
    valor = 0
    ases = 0
    for carta in mano:
        valor += VALORES_CARTAS[carta.split()[0]]
        if carta.split()[0] == 'A':
            ases += 1
    
    #ajustar valor de los ases (1 o 11)
    while valor <= 11 and ases > 0:
        valor += 10
        ases -= 1
    
    return valor

#función para el turno del crupier
def turno_crupier(mazo_crupier):
    print("\nTurno del crupier:")
    mano_crupier = [mazo_crupier.pop(), mazo_crupier.pop()]  #el crupier recibe dos cartas
    valor_crupier = calcular_valor(mano_crupier)
    print(f"Cartas del crupier: {mano_crupier} - Valor: {valor_crupier}")
    
    #el crupier debe pedir carta si tiene menos de 17
    while valor_crupier < 17:
        carta = mazo_crupier.pop()
        mano_crupier.append(carta)
        valor_crupier = calcular_valor(mano_crupier)
        print(f"El crupier pide carta: {carta} - Valor total: {valor_crupier}")
        
    print(f"El crupier se planta con valor: {valor_crupier}")
    return valor_crupier

#función para manejar el turno de los jugadores
def manejar_turnos_jugadores(numero_jugadores, mazos_adicionales):
    jugadores_valores = []
    for i in range(numero_jugadores):
        mano = []
        print(f"\nTurno del jugador {i + 1}:")
        while True:
            carta = mazos_adicionales[i].pop()
            mano.append(carta)
            valor = calcular_valor(mano)
            print(f"Cartas: {mano} - Valor: {valor}")
            if valor >= 21:
                break
            decision = input("Quieres pedir otra carta? (s para sí, cualquier otra tecla para plantarse): ")
            if decision.lower() != 's':
                break
        jugadores_valores.append(valor)
    return jugadores_valores

#iniciar el juego
def main():
    print("Bienvenido al Blackjack\n")
    
    #ingresar el número de jugadores
    while True:
        numero_jugadores = input("Intruduzca el número de jugadores (2 a 7): ")
        if numero_jugadores.isdigit():
            numero_jugadores = int(numero_jugadores)
            if 2 <= numero_jugadores <= 7:
                break
            else:
                print("El número de jugadores debe estar entre 2 y 7. Intenta nuevamente.")
        else:
            print("Por favor, ingresa un número válido.")
    
    #ingresar nombres de los jugadores
    jugadores = []
    for i in range(numero_jugadores):
        nombre = input(f"Ingresa el nombre del jugador {i + 1}: ").strip()
        jugadores.append(nombre)

    #mezclar el mazo
    random.shuffle(Mazo)
    
    #crear mazos para cada jugador
    mazos_adicionales = []
    for _ in range(numero_jugadores):
        mazo_jugador = Mazo.copy()
        random.shuffle(mazo_jugador)
        mazos_adicionales.append(mazo_jugador)
    
    #los jugadores toman su turno
    jugadores_valores = manejar_turnos_jugadores(numero_jugadores, mazos_adicionales)
    
    #el crupier juega su turno
    mazo_crupier = Mazo.copy()
    random.shuffle(mazo_crupier)
    valor_crupier = turno_crupier(mazo_crupier)
    
    #determinar el ganador
    print("\n Resultados")
    print(f"El crupier tiene un valor final de: {valor_crupier}")
    
    for i, valor in enumerate(jugadores_valores):
        print(f"{jugadores[i]} tiene un valor final de: {valor}")
        if valor > 21:
            print(f"{jugadores[i]} ha perdido (se pasó de 21).")
        elif valor == valor_crupier:
            print(f"{jugadores[i]} ha empatado con el crupier.")
        elif valor > valor_crupier and valor <= 21:
            print(f"{jugadores[i]} ha ganado al crupier.")
        else:
            print(f"{jugadores[i]} ha perdido ante el crupier.")
    
if __name__ == "__main__":
    main()
