from spell import *

class Character:
    """
    life
    mana
    earth
    fire
    water
    air
    lighting
    spells
    """

    def __init__(self, life, mana, earth, fire, water, air, light):
        self._life = life
        self._mana = mana
        self._earth = earth
        self._fire = fire
        self._water = water
        self._air = air
        self._light = light
        self._spells = []

    def __repr__(self):
        string = "Vie :"+self._life+" - Mana :"+self._mana
        return string

    def __str__(self):
        return repr(self)

    def get_damage(self,hit):
        self._life -= hit

    def attack(self,ennemy,spell):
        i = 0
        for spell in spells:
            print spell["name"], " : ", i
            i+=1
        
        index = input('')
        
        ennemy.get_damage(self._spells[].launch(
                earth=self._earth, 
                fire=self._fire, 
                water=self._water, 
                air=self._air, 
                light=self._light))
        
        
    def is_alive(self):
        return self._life > 0

    def add_spell(self, spell):
        self._spells.append(spell)
