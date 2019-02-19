#teen simulator
personlist = []
class Person(object):
  def __init__(self,name):
    global Personlist
    self.name = name
    self.inventory = []
    self.location = False
    personlist.append(self)
    

class NPC(Person):
  def __init__(self,name):
    super().__init__(name)
    self.lines = {}

ross = NPC("Ross")
print (ross.inventory)

class Room(object):
  def __init__(self,name,coordinates):
    global personlist
    self.name = name
    self.coordinates = coordinates
    self.people = []
    for person in personlist:
      if person.location == self.coordinates:
        self.people.append(person)
    


