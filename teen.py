class Person(object):
  def __init__(self,name):
    self.name = name
    self.inventory = []

class NPC(Person):
  def __init__(self, name):
    super().__init__(name)
    self.lines = {}

ross = Person("Ross")
print (ross.name)