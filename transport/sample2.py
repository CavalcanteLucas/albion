SMALL_LOAD = 3
MEDIUM_LOAD = 7
LARGE_LOAD = 15

class Item():
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

thet_heart = Item("Thetford Heart")
mart_heart = Item("Martlock Heart")

class Load():
    item = Item
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __str__(self):
        return f'[{self.quantity}] {self.item.name}\n'

load_1 = Load(thet_heart, 12)

class Vault():
    content = []

    def __init__(self, item_list):
        for item in item_list:
            self.content.append(item)

    def __str__(self):
        vault_description = f''
        for load in self.content:
            vault_description += str(load)
        return vault_description

    def deposit(self, input_load):
        import ipdb; ipdb.set_trace()

thetford_vault = Vault([load_1])
print(thetford_vault)

thetford_vault.deposit(load_1)

class City():
    name = ""
    vault = Vault
    def __str__(self):
        city_vault_description = f'\n{self.name} vault: \n ----- \n {self.vault}'
        return city_vault_description


    def transport(self, to_destiny_city, load):
        pass
        # transport_load = 
        # print(self)
        # import ipdb; ipdb.set_trace()
        # import ipdb; ipdb.set_trace()
        # self.vault[self.unit] -= load
        # (city_unit, prize), = self.transport_rules[to_destiny_city][load].items()
        # if city_unit in self.vault:
        #     self.vault[city_unit] += prize
        # else:
        #     self.vault[city_unit] = prize
        # print(self.vault)
        
class Thetford(City):
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


thetford_vault = { load_1, load_1 }
thetford = Thetford(thetford_vault)

# thetford.transport("to_martlock", SMALL_LOAD)
