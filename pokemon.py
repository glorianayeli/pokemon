tipos_pokemon = {
  "agua": {
    "resistencias":["acero", "agua", "hielo", "fuego"],
    "debilidades":["electrico", "planta"],
    "inmune":[]
  },
  "fuego": {
    "resistencias":["planta", "hielo", "bicho", "acero", "hada"],
    "debilidades":["fuego", "agua", "roca", "dragon"],
    "inmune":[]
  },
  "planta": {
    "resistencias": ["agua", "tierra", "roca"],
    "debilidades": ["fuego", "planta", "veneno", "volador", "bicho", "dragon"],
    "inmune":[]
  }
}
class Pokemon:
  dano_base = 10
  
  def __init__(self, especie, stats, ataques, tipo, fortalezas, debilidades):
    self.especie = especie
    self.stats = stats
    self.current_stats = self.stats.copy()
    self.tipo = tipo
    self.debilidades = debilidades
    self.fortalezas = fortalezas
    self.ataques = ataques
  
  print("acero" in tipos_pokemon["agua"]["resistencias"])

  def centro_pokemon(self):
    self.current_stats = self.stats

  def selecciona_ataque(self):
    ataque_exist = lambda self, ataque : not ataque in self.ataques
    exist = True
    while exist:
      print(f'Selecciona un ataque:')
      for ataque in self.ataques:
        print(f"{ataque} tipo: {self.ataques[ataque]['tipo']} poder:{self.ataques[ataque]['poder']}")
      ataque = input('Ingresa el ataque:')
      exist = ataque_exist(self,ataque)
    return self.ataques[ataque]

  #modificador de ataque basado en tipo de ataque
  def modificador_ataque(self, tipo_ataque):
    if tipo_ataque in tipos_pokemon[self.tipo]["debilidades"]:
      return 2
    elif tipo_ataque in tipos_pokemon[self.tipo]['inmune']:
      return 0
    else:
      return 1
  
  def modificador_defensa(self, rival, tipo_ataque):
    if tipo_ataque in tipos_pokemon[rival.tipo]["debilidades"]:
      return 2
    elif tipo_ataque in tipos_pokemon[rival.tipo]['inmune']:
      return 0
    else:
      return 1
  
  def pelea(self, rival):    
    # Tu rival es furte o debil a ti?
    if self.tipo in rival.fortalezas:
      modificador_ataque = 1/2
      print(f"{rival.especie} es fuerte a los ataques de {self.especie} \n")
    elif self.tipo in rival.debilidades:
      modificador_ataque = 2
      print(f"{rival.especie} es debil a los ataques de {self.especie} \n")
    else:
      modificador_ataque = 1
    
    #eres fuerte o debil a tu rival?
    if rival.tipo in self.fortalezas:
      modificador_defensa = 1/2
      print(f"{self.especie} es fuerte a los ataques de {rival.especie} \n")
    elif rival.tipo in self.debilidades:
      modificador_defensa = 2
      print(f"{self.especie} es debil a los ataques de {rival.especie} \n")
    else:
      modificador_defensa = 1

    # quien ataca primero
    if self.current_stats["velocidad"] >= rival.current_stats["velocidad"]:
      mi_turno = True
    else:
      mi_turno = False
    
    # combate por turnos
    while (self.current_stats["hp"] > 0) & (rival.current_stats["hp"] > 0):
      if mi_turno:
        #seleccionar ataque 
        poder = self.selecciona_ataque()
        poder_total = poder["poder"]
        #efectividad de ataque
        power_up = self.modificador_ataque(poder["tipo"])      
        # atacando
        dano = int(
            self.dano_base * 
            (((self.current_stats["ataque"] * poder_total) / 50) / rival.current_stats["defensa"]) * 
            modificador_ataque * power_up) 
        rival.current_stats["hp"] -= dano
        print(f"{self.especie} hizo {dano} de daño a {rival.especie}")
        print(f"A {rival.especie} le quedan {rival.current_stats['hp']} puntos de vida")
      else:
        # defendiendo
        # seleccionar ataque
        poder = rival.selecciona_ataque()
        poder_total = poder["poder"]
        power_up = rival.modificador_defensa(rival, poder['tipo'])
        dano = int(
            rival.dano_base *
            (((rival.current_stats["ataque"] * poder_total) / 50) / self.current_stats["defensa"]) * 
            modificador_defensa * power_up)
        self.current_stats["hp"] -= dano
        print(f"{rival.especie} hizo {dano} de daño a {self.especie}")
        print(f"A {self.especie} le quedan {self.current_stats['hp']} puntos de vida")
      mi_turno = not mi_turno
    else:
      if self.current_stats["hp"] <= 0:
        print(f'{rival.especie} ha ganado la pelea \n')
      else:
        print(f'{self.especie} ha ganado la pelea \n')