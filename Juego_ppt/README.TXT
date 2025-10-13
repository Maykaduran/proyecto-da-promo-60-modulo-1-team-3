## Juego de Piedra, Papel o Tijeras

Este es un sencillo juego de Piedra, Papel o Tijeras en Python, donde un usuario compite contra un bot hasta que uno de los dos alcance 3 victorias.

# Cómo jugar

	1	Ejecuta el código en Python.
	2	Se te pedirá que ingreses tu elección: "piedra", "papel" o "tijeras".
	3	El bot hará su elección de manera aleatoria.
	4	Se mostrarán los resultados de cada ronda y el número de victorias acumuladas.
	5	El juego continúa hasta que uno de los jugadores alcance 3 victorias.
	6	Cuando un jugador llega a 3 victorias, se anuncia al ganador y el juego termina.

# Reglas

	•	Piedra gana a Tijeras
	•	Tijeras gana a Papel
	•	Papel gana a Piedra
	•	Si ambos eligen lo mismo, la ronda termina en empate.
	•	Si ingresas un valor diferente de "piedra", "papel" o "tijeras", se mostrará un mensaje de opción no válida y se pedirá tu elección nuevamente.

# Variables principales

	•	victorias_user1: Contador de victorias del usuario.
	•	victorias_userbot: Contador de victorias del bot.
	•	opciones: Lista con las opciones posibles ("piedra", "papel", "tijeras").


# Ejemplo de ejecución

Ingresa tu elección: piedra
Gana user1
LLevas 1 victorias
___________________________________
Ingresa tu elección: papel
Empate
___________________________________
…
user 1 ha ganado el juego!

# Requisitos
	•	Python 3.x
	•	Biblioteca random (incluida en la librería estándar de Python)