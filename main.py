#teen simulator
from person import Person, Player, NPC, personlist
from room import Room


daniel = Player("Daniel")
daniel.location = [0,0]
print (daniel.location)
while True:
  cmd = input(">")
  cmd = cmd.split(" ")
  daniel.move(cmd)
  print (daniel.location)

