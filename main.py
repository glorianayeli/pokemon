from pokemon import Pokemon
from user import User

def selecciona_pokemon(pokemons):
    exist = True
    ataque_exist = lambda pokemon : not pokemon in pokemons
    print("\nSelecciona un pokemon de tu equipo de pokemon:")
    while exist:
        for pokemon in pokemons:
            print(f'{pokemon} "HP" {pokemons[pokemon].stats["hp"]} "Velocidad" {pokemons[pokemon].stats["velocidad"]} "Ataque" {pokemons[pokemon].stats["ataque"]} "defensa" {pokemons[pokemon].stats["defensa"]}')
        pokemon = input("Seleccion:")
        exist = ataque_exist(pokemon)
        print(exist)
    return pokemons[pokemon]

def crear_jugador():
    jugador_nombre = input("Ingresa tu nombre:")
    return User(jugador_nombre)

def bienvenida(name):
    print(f'\n Hola {name} estas apunto de comenzar una increible aventura')

#declarar jugadores
print("Jugador uno")
jugador_uno = crear_jugador()

print("Jugador dos:")
jugador_dos = crear_jugador()

#Elegir pokemon 

#Jugador uno
bienvenida(jugador_uno.name)
pokemon_jugador_uno = selecciona_pokemon(jugador_uno.equipo_pokemon)

#Jugador dos
bienvenida(jugador_dos.name)
pokemon_jugador_dos = selecciona_pokemon(jugador_dos.equipo_pokemon)

pokemon_jugador_uno.pelea(pokemon_jugador_dos)
pokemon_jugador_dos.centro_pokemon()
pokemon_jugador_uno.centro_pokemon()
