import random
#武器类
class Mono(object):
    name:str
    cost:int
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    def getcost(self):
        return self.cost
class Weapon(Mono):
    damage:float
    def __init__(self,name,damage,cost):
        super().__init__(name,cost)
        self.damage=damage
    def built(self):
        self.damage+=random.randint(0,5)

class Armour(Mono):
    defense:float
    durability:int
    max_durability:int
    delta_d:int=1
    def __init__(self,name,defense,cost,max_durability):
        super().__init__(name,cost)
        self.defense=defense
        self.durability=max_durability
        self.max_durability=max_durability
    def use(self,delta_d:int)->bool:
        if self.durability - delta_d < 0:
            return False
        else:
            self.durability-=delta_d
            return True
    def use(self)->bool:
        if self.durability - self.delta_d < 0:
            return False
        else:
            self.durability-=self.delta_d
            return True
    def set_default_use_durability(self,delta_d:int):
        self.delta_d=delta_d
    def fix(self) -> int:
        fixed=self.max_durability-self.durability
        self.durability=self.max_durability
        return fixed

class Equipments(object):
    equips:dict={}
    def __init__(self,weapon:Weapon,armour:Armour) -> None:
        self.equips=dict()
        self.equips['weapon']=weapon
        self.equips['armour']=armour
    def tdamage(self):
        return self.equips['weapon'].damage
    def tdefense(self):
        return self.equips['armour'].defense

class Entity(object):
    name:str;
    health:float
    strength:float #Damage
    strudy:float   #Defense
    equips:Equipments
    damage:int=0
    defense:int=0
    def __init__(self,name,health,strength,strudy,equips:Equipments) -> None:
        self.name=name
        self.health=health
        self.strength=strength
        self.strudy=strudy
        self.equips=equips
        self.damage=self.strength+self.equips.tdamage()
        self.defense=self.strudy+self.equips.tdefense()
class Enemy(Entity):
    reward_exp:int
    reward_money:int
    rewards:list
    def __init__(self,name,health,strength,strudy,equips,reward_exp,reward_money,rewards):
        super().__init__(name,health,strength,strudy,equips)
        self.reward_exp=reward_exp
        self.reward_money=reward_money
        self.rewards=rewards

class Player(Entity):
    money:int
    inventory:list
    def __init__(self,name,health,strength,strudy,equips,money,inventory):
        super().__init__(name,health,strength,strudy,equips)
        self.money=money
        self.inventory=inventory

p=Player("1",2,3,4,Equipments(Weapon(10,10,10),Armour(0,0,0,100)),0,[])
q=Player.damage
print(q)