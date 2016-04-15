import sys
import os
import random

sys.stdout.write("heh")
print random.randint(1,2)

class Char:
    def __init__(self, name, clas):

        self.name = name
        self.clas = clas

        if clas == "Warrior":
            self.hp = 100
            self.actualhp = self.hp
            self.mana = 50
            self.actualmana = self.mana
            self.atk = 10
            self.defn = 10
            self.speed = 10
            self.matk = 2
            self.mdefn = 10

        if clas == "Mage":
            self.hp = 80
            self.actualhp = self.hp
            self.mana = 100
            self.actualmana = self.mana
            self.atk = 5
            self.defn = 6
            self.speed = 15
            self.matk = 10
            self.mdefn = 8

        if clas == "Goblin":
            self.hp = 200
            self.actualhp = self.hp
            self.mana = 50
            self.actualmana = self.mana
            self.atk = 10
            self.defn = 10
            self.speed = 10
            self.matk = 0
            self.mdefn = 10

class Fight:
    def __init__(self, Allies, Fiends):
        self.allies = Allies
        self.enemies = Fiends
        self.turn_order = []

    def print_fight(self):
        #os.system('clear')
        self.print_allies()
        print '\n'
        self.print_enemies()

    def print_allies(self):
        print 'Allies :\n'
        for al in self.allies:
            print '{}: {}'.format(al.name, al.clas)
            print '\t{}/{}'.format (al.hp  , al.actualhp)
            print '\t{}/{}'.format (al.mana, al.actualmana)

    def print_enemies(self):
        print 'Enemies :\n'
        for e in self.enemies:
            print '{}: {}'.format(e.name, e.clas)
            print '\t{}/{}'.format (e.hp  , e.actualhp)
            print '\t{}/{}'.format (e.mana, e.actualmana)

    def create_turn_order(self):
        order = []
        for al in self.allies:
            order.append((al.speed,'allie',al))
        for e in self.enemies:
            order.append((e.speed,'enemy',e))
        order.sort(reverse=True)
        return order

    def fight(self):
        self.print_fight()
        enemies_dead = False
        self.turn_order = self.create_turn_order()
        while not enemies_dead:
            for chr in self.turn_order:
                if chr[1] == 'allie':
                    self.print_actions()
                    action = self.action_selection()
                    self.make_action()
                elif chr[1] == 'enemy':
                    self.enemy_action()




if __name__ == '__main__':

    Bob = Char("Bob", "Warrior")
    Kek = Char("Kek", "Mage")
    a = [Bob, Kek]
    Enemy = Char("Derp", "Goblin")
    e = [Enemy]
    F = Fight(a,e)
    F.fight()