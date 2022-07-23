from pokemon import Pokemon
squirtle = Pokemon(
    especie = "Squirtle",
    stats = {
        "velocidad": 43,
        "hp": 44,
        "ataque": 48,
        "defensa": 65},
    ataques = {
        'golpe cabeza': {'poder': 70, 'tipo': 'normal'},
        'placaje': {'poder': 40, 'tipo': 'normal'}
    },
    tipo = "agua",
    fortalezas = ["fuego", "tierra", "Roca"],
    debilidades = ["agua", "planta", "dragon", "electrico"])

charmander = Pokemon(
    especie = "Charmander",
    stats = {
        "velocidad": 65,
        "hp": 39,
        "ataque": 52,
        "defensa": 43},
    ataques = {
        'aranazo': {'poder': 40, 'tipo': 'normal'},
        'grunido': {'poder': 35, 'tipo': 'normal'}
    },
    tipo = "fuego",
    fortalezas = ["planta", "bicho", "hielo", "acero", "hada"],
    debilidades = ["agua", "agua", "roca", "dragon"])

bulbasaur = Pokemon(
    especie = "Bulbasaur",
    stats = {
        "velocidad": 45,
        "hp": 45,
        "ataque": 49,
        "defensa": 49},
    tipo = "planta",
    ataques = {
        'corte': {'poder': 50, 'tipo': 'normal'},
        'atadura': {'poder': 15, 'tipo': 'normal'}
    },
    fortalezas = ["Agua", "tierra", "roca"],
    debilidades = ["fuego", "planta", "veneno", "volador", "bicho", "dragon"])

squirtle.pelea(charmander)
squirtle.centro_pokemon()
charmander.centro_pokemon()