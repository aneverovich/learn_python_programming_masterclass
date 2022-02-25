from player import Player
# from enemy import Enemy
from enemy import Troll
# from enemy import Vampyre
from enemy import VampyreKing

tim = Player("Tim")

ugly_troll = Troll("Pug")
print(f"Ugly torll - {ugly_troll}")

another_troll = Troll("Ug")
print(f"Another troll - {another_troll}")

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

print("-" * 40)

dracula = VampyreKing("Dracula")
print(dracula)

print("-" * 40)

dracula.take_damage(40)
print(dracula)

brother.take_damage(14)
print(brother)

another_troll.take_damage(30)
print(another_troll)

while dracula._alive:
    dracula.take_damage(1)
    print(dracula)
