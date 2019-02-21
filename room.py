from person import personlist
wall_list = []
class Room(object):
  def __init__(self,name,location):
    global personlist
    self.name = name
    self.location = location
    self.people = []
  def refresh(self):
    global personlist
    for person in personlist:
      if person.location == self.location:
        self.people.append(person)

class Wall(Room):
  def __init__(self,location):
    global wall_list
    super().__init__(self,location)
    self.name = "Wall"
    wall_list.append(self)


wall1 = Wall([-1,0])
wall2 = Wall([-1,1])
wall3 = Wall([-1,2])
wall4 = Wall([0,3])
wall5 = Wall([1,3])
wall6 = Wall([2,3])
wall7 = Wall([3,3])
wall8 = Wall([3,0])