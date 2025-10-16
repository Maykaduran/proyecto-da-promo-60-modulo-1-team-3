import random

piedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

tijeras = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

imagenes = {"piedra": piedra, "papel": papel,"tijeras": tijeras}

opciones = ["piedra", "papel", "tijeras"]

victorias_user1 = 0
victorias_userbot = 0

print("\n🪨📄✂️  ¡Bienvenido al juego Piedra, Papel o Tijeras!  ✂️📄🪨")
print("----------------------------------------------------------")

while victorias_user1 < 3 or victorias_userbot < 3:

    user_bot = random.choice(opciones)
    user1 = input("\n👉 Elige piedra, papel o tijeras: ").lower()

    if user1 not in opciones:
        print("⚠️ Opción no válida")
        continue

    print("\nTú elegiste:")
    print(imagenes[user1])
    print("El bot eligió:")
    print(imagenes[user_bot])

    if user1 == "tijeras" and user_bot == "papel" or user1 == "papel" and user_bot == "piedra" or user1 == "piedra" and user_bot == "tijeras":
       victorias_user1 += 1
       print("🏆 Gana user1")
       print(f"Llevas {victorias_user1} victorias")
       print("___________________________________")

    elif user1 == user_bot:
        print("🤝 Empate")
        print("___________________________________")
        
    elif user_bot == "tijeras" and user1 == "papel" or user_bot == "papel" and user1 == "piedra" or user_bot == "piedra" and user1 == "tijeras":
        victorias_userbot += 1
        print("💻 Gana user_bot")
        print(f"Lleva {victorias_userbot} victorias")
        print("___________________________________")

    if victorias_user1 == 3:
        print("\n🏆 ¡User 1 ha ganado el juego!")
        break

    elif victorias_userbot == 3:
        print("\n🤖 ¡User_bot ha ganado el juego!")
        break
