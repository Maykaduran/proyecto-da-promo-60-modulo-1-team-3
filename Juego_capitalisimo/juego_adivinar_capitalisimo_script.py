import sys
print("Python executable:", sys.executable)
import random

# Bloque 1: Datos originales (lista gigante)
paises = "Afganistán, Albania, Alemania, Andorra, Angola, Antigua y Barbuda, Arabia Saudi, Argelia, Argentina, Armenia, Australia, Austria, Azerbaiyán, Las Bahamas, Baréin, Bangladesh, Barbados, Bélgica, Belice, Benín, Bielorrusia, Birmania, Bolivia, Bosnia y Herzegovina, Botsuana, Brasil, Brunéi, Bulgaria, Burkina Faso, Burundi, Bután, Cabo Verde, Camboya, Camerún, Canadá, Qatar, Chad, Chile, China, Chipre, Ciudad del Vaticano, Colombia, Unión de las Comoras, Corea del Norte, Corea del Sur, Costa de Marfil, Costa Rica, Croacia, Cuba, Dinamarca, Dominica, Ecuador, Egipto, El Salvador, Emiratos Árabes Unidos, Eritrea, Eslovaquia, Eslovenia, España, Estonia, Etiopía, Islas Fiyi, Filipinas, Finlandia, Francia, Gabón, Gambia, Georgia, Ghana, Granada (Isla), Grecia, Guatemala, Guinea, Guinea-Bisáu, Guinea Ecuatorial, Guyana, Haití, Honduras, Hungría, India, Indonesia, Iraq, Irán, Irlanda, Islandia, Islas Marshall, Islas Salomón, Israel, Italia, Jamaica, Japón, Jordania, Kazajistán, Kenia, Kirguistán, Kiribati, Kosovo, Kuwait, Laos, Lesoto, Letonia, Líbano, Liberia, Libia, Liechtenstein, Lituania, Luxemburgo, Macedonia del Norte, Madagascar, Malasia, Malaui, Maldivas, Mali, Malta, Marruecos, República de Mauricio, Mauritania, México, Micronesia, Moldavia, Mónaco, Mongolia, Montenegro, Mozambique, Namibia, República de Nauru, Nepal, Nicaragua, Niger, Nigeria, Noruega, Países Bajos, Pakistán, Palaos, Panamá, Papúa Nueva Guinea, Paraguay, Perú, Polonia, Portugal, Reino Unido, República Centroafricana, República Checa, República del Congo, República Democrática del Congo, República Dominicana, Ruanda, Rumanía, Rusia, Samoa, San Cristóbal y Nieves, San Marino, San Vicente y las Granadinas, Santa Lucía, Santo Tomé y Príncipe, Senegal, Serbia, Seychelles, Singapur, Sierra Leona, Siria, Somalia, Sri Lanka, Sudáfrica, Sudán, Sudán del Sur, Suecia, Suiza, Surinam, Suazilandia, Tailandia, Tanzania, Tayikistán, Timor Oriental, Togo, Tonga, Trinidad y Tobago, Túnez, Turkmenistán, Turquía, Tuvalu, Ucrania, Uganda, Uruguay, Uzbekistán, Vanuatu, Venezuela, Vietnam, Yemen, Yibuti, Zambia, Zimbabue, Taiwán, Palestina, Sáhara Occidental, Somalilandia, Abjasia, Osetia del Sur, Transnistria, Artsaj"
paises_mundo = list(paises.split(', '))
capitales = "Kabul, Tirana, Berlín, Andorra, Luanda, Saint John's, Riad, Argel, Buenos Aires, Ereván, Canberra, Viena, Bakú, Nasáu, Manama, Daca, Bridgetown, Bruselas, Belmopán, Porto Novo, Minsk, Naipyidó, Sucre, Sarajevo, Gaborone, Brasilia, Bandar Seri Begawan, Sofía, Uagadugú, Gitega, Timbu, Praia, Nom Pen, Yaundé, Ottawa, Doha, Yamena, Santiago, Pekín, Nicosia, Ciudad del Vaticano, Bogotá, Moroni, Pionyang, Seúl, Yamusukro, San José, Zagreb, La Habana, Copenhague, Roseau, Quito, El Cairo, San Salvador, Abu Dabi, Asmara, Bratislava, Liubliana, Madrid, Tallin, Adis Abeba, Suva, Manila, Helsinki, París, Libreville, Banjul, Tiflis, Acra, Saint George's, Atenas, Ciudad de Guatemala, Conakri, Bisau, Malabo, Georgetown, Puerto Príncipe, Tegucigalpa, Budapest, Nueva Delhi, Yakarta, Bagdad, Teherán, Dublín, Reikiavik, Majuro, Honiara, Jerusalem, Roma, Kingston, Tokio, Amán, Astana, Nairobi, Biskek, Tarawa del Sur, Pristina, Kuwait, Vientián, Maseru, Riga, Beirut, Monrovia, Trípoli, Vaduz, Vilnius, Luxemburgo, Skopje, Antananarivo, Kuala Lumpur, Lilongüe, Malé, Bamako, La Valeta, Rabat, Port Louis, Nuakchot, Ciudad de México, Palikir, Chisinau, Mónaco, Ulan Bator, Podgorica, Maputo, Windhoek, Yaren, Katmandú, Managua, Niamey, Abuya, Oslo, Ámsterdam, Islamabad, Ngerulmud, Ciudad de Panamá, Port Moresby, Asunción, Lima, Varsovia, Lisboa, Londres, Bangui, Praga, Brazzaville, Kinsasa, Santo Domingo, Kigali, Bucarest, Moscú, Apia, Basseterre, San Marino, Kingstown, Castries, Santo Tomé, Dakar, Belgrado, Victoria, Freetown, Singapur, Damasco, Mogadiscio, Sri Jayawardenapura Kotte, Pretoria, Jartum, Yuba, Estocolmo, Berna, Paramaribo, Mbabane, Bangkok, Dodoma, Dusamb, Dili, Lomé, Nukualofa, Puerto España, Túnez, Asjabad, Ankara, Funafuti, Kiev, Kampala, Montevideo, Taskent, Port Vila, Caracas, Hanói, Saná, Yibuti, Lusaka, Harare, Taipei, Ramala, El Aaiún, Hargeisa, Sujumi, Tsjinvali, Tiráspol, Stepanakert"
capitales_mundo = list(capitales.split(', '))
# Creación del diccionario
capitalisimo_paises = {}
for i in range(len(paises_mundo)):
    capitalisimo_paises[paises_mundo[i]] = capitales_mundo[i]
# Creación de la lista de validación
lista_todas_capitales_normalizadas = []
for capital in capitales_mundo:
    capital_limpia = capital.strip().lower()
    lista_todas_capitales_normalizadas.append(capital_limpia)

# --- FUNCIÓN PRINCIPAL DEL JUEGO (10 rondas y puntuación) ---
def jugar_capitalisimo():
    puntuacion = 10
    max_rondas = 10
    ronda_actual = 1
    paises_usados = []

    input("Presiona Enter para empezar el juego...\n")  # Pausa inicial

    print("=" * 60)
    print(f"\n    SI ESTÁS LEYENDO ESTO, HAS SIDO SELECCIONADA PARA UNA OPORTUNIDAD ÚNICA, SOLO SABRÁS CUÁL ES AL FINAL DE ESTE JUEGO:\n\nVas a recibir un cuestionario con preguntas sobre este mundo, en esta ocasión querremos saber cuánto sabes de países y capitales.\n\nComienzas con {puntuacion} puntos. El máximo de rondas es: {max_rondas} rondas.\n")
    print("=" * 60)

    usuario = input('¿Te ves preparada? (SI/NO): ').strip().lower()
    if usuario != 'si':
        print("""
   |     '||'  '||'       '||''|.   '||'  '|' '||''''|  '|.   '|'  ..|''||   
   |||     ||    ||         ||   ||   ||    |   ||  .     |'|   |  .|'    ||  
  |  ||    ||''''||         ||'''|.   ||    |   ||''|     | '|. |  ||      || 
 .''''|.   ||    ||         ||    ||  ||    |   ||        |   |||  '|.     || 
.|.  .||. .||.  .||.       .||...|'    '|..'   .||.....| .|.   '|   ''|...|'  
                                                                              
                                                                              
 .|'''.|  '||''''|     '||    ||' '||''''|  
 ||..  '   ||  .        |||  |||   ||  .    
  ''|||.   ||''|        |'|..'||   ||''|    
.     '||  ||           | '|' ||   ||       
|'....|'  .||.....|    .|. | .||. .||.....| 
                                            
                                            
  ..|'''.| '||'  '|' '||' '||''|.       |     
.|'     '   ||    |   ||   ||   ||     |||    
||          ||    |   ||   ||    ||   |  ||   
'|.      .  ||    |   ||   ||    ||  .''''|.  
 ''|....'    '|..'   .||. .||...|'  .|.  .||. 
                                             """)
        print("\n\n")
        input("Pulsa Enter para salir...")  # Pausa antes de salir
        return

    while ronda_actual <= max_rondas and puntuacion > 0:  # Corregido: ahora verifica puntuacion > 0
        print(f"\n Ronda {ronda_actual} de {max_rondas} ")
        paises_disponibles = [pais for pais in capitalisimo_paises.keys() if pais not in paises_usados]
        if not paises_disponibles:
            print("No hay más países disponibles.")
            break

        pais_elegido = random.choice(paises_disponibles)
        paises_usados.append(pais_elegido)
        capital_correcta = capitalisimo_paises[pais_elegido]
        pregunta = f"Capital de {pais_elegido}: "
        respuesta_usuario = input(pregunta).strip().lower()
        capital_limpia = capital_correcta.strip().lower()

        if respuesta_usuario == capital_limpia:
            print('CORRECTO. Mantienes tu puntuación.')
            print('')
        else:
            es_capital_conocida = False
            for capital in capitalisimo_paises.values():
                if respuesta_usuario == capital.strip().lower():
                    es_capital_conocida = True
                    break
            if es_capital_conocida:
                puntuacion -= 1
                print(f'Es la capital de OTRO PAÍS, pero no de éste. La capital correcta es {capital_correcta}.\nPierdes 1 punto')
            else:
                puntuacion -= 3
                print(f"Respuesta absurda. La respuesta real es {capital_correcta}. Pierdes 3 puntos.")

        print(f"Puntuación actual: {puntuacion} puntos")
        input("Pulsa Enter para continuar...")  # Pausa después de cada ronda
        ronda_actual += 1

    print("\n" + "=" * 60)
    print(f"Hasta aquí nuestro cuestionario\n\nTu puntuación final es: {puntuacion}")
    print("\n" + "=" * 60)

    if puntuacion >= 8:
        print(f"\nENHORABUENA: Has ganado con {puntuacion} puntos\n".upper())
        print("¡HAS SIDO ELEGIDA PRESIDENTE DEL MUNDO!\n\n¡ESPERAMOS MUCHO DE TI! MUCHA SUERTE...")
    elif puntuacion <= 3:
        print(f"\nHas perdido con {puntuacion} puntos.\nEl mundo no es lo tuyo, aunque perder también tiene recompensa:".upper())
        print("\n¡HAS SIDO ELEGIDA PARA SER EXPULSADA DEL PLANETA!\n\nESTAMOS PREPARÁNDOTE UNA BURRA PARA QUE NO TE FALTE DE NADA AL ABANDONAR LA TIERRA.\n\nPronto recibirás la fecha.")
        print("\n\nRecuerda revisar tu carpeta de spam.")
    else:
        print(f'Ni has perdido ni has ganado, tienes {puntuacion} puntos. La mediocridad no es mala: al final son solo capitales'.upper())

    input("\nPulsa Enter para salir...")  # Pausa final

jugar_capitalisimo()
