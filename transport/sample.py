SMALL_LOAD = 3
MEDIUM_LOAD = 7
LARGE_LOAD = 15

class Item():
    def __init__(self, name):
        self.name = name

class Load():
    item = Item
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

class City():
    name = ""
    unit = ""
    vault = {}
    transport_rules = {}

    def __str__(self):
        return "{}".format(self.name)


    def transport(self, to_destiny_city, load):
        print(self.vault)
        self.vault[self.unit] -= load
        (city_unit, prize), = self.transport_rules[to_destiny_city][load].items()
        if city_unit in self.vault:
            self.vault[city_unit] += prize
        else:
            self.vault[city_unit] = prize
        print(self.vault)


# thetford.transport("to_martlock", SMALL_LOAD)


class Thetford(City):
    def __init__(self, vault):
        self.name = "Thetford"
        self.unit = "t"
        self.vault = vault
        self.transport_rules = {
            "to_martlock": {
                SMALL_LOAD: { "m": 4 },
                MEDIUM_LOAD: { "m": 9 },
                LARGE_LOAD: { "m": 19 }
            }
        }

class Martlock(City):
    def __init__(self, vault):
        self.name = "Martlock"
        self.unit = "m"
        self.vault = vault
        self.transport_rules = {
            "to_thetford": {
                SMALL_LOAD: { "t": 5 },
                MEDIUM_LOAD: { "t": 10 },
                LARGE_LOAD: { "t": 21 }
            }
        }


thet_heart = Item("Thetford Heart")
mart_heart = Item("Martlock Heart")

thetford_vault = { "t": 12 }
martlock_vault = { "m": 12 }

thetford = Thetford(thetford_vault)
martlock = Martlock(martlock_vault)

thetford.transport("to_martlock", SMALL_LOAD)



class CityAlt():
    name = ""
    vault = {}
    def __str__(self):
        vault_description = f'\n{self.name} vault: \n ----- \n'
        for load in self.vault:
            vault_description += f'[{load.quantity}] {load.item.name}\n'
        return vault_description


    def transport(self, to_destiny_city, load):
        # transport_load = 
        print(self.vault)
        import ipdb; ipdb.set_trace()
        # import ipdb; ipdb.set_trace()
        # self.vault[self.unit] -= load
        # (city_unit, prize), = self.transport_rules[to_destiny_city][load].items()
        # if city_unit in self.vault:
        #     self.vault[city_unit] += prize
        # else:
        #     self.vault[city_unit] = prize
        # print(self.vault)
        
class ThetfordAlt(CityAlt):
    def __init__(self, vault):
        self.name = "Thetford"
        self.vault = vault
        self.transport_rules = {
            "to_martlock": {
                SMALL_LOAD: { Load(mart_heart, 4) },
                MEDIUM_LOAD: { Load(mart_heart, 9) },
                LARGE_LOAD: { Load(mart_heart, 19) }
            }
        }
        # for key, value in self.vault:
            # print(key, value)
        # import ipdb; ipdb.set_trace()


load_1 = Load(thet_heart, 12)
thetford_vault_alt = { load_1, load_1 }
thetford_alt = ThetfordAlt(thetford_vault_alt)

print(thetford_alt)
# import ipdb; ipdb.set_trace()

# print(f'{}'.(thetford_alt.vault)

# thetford_alt.transport("to_martlock", SMALL_LOAD)
