from person import personlist
class Room(object):
  def __init__(self,name,coordinates):
    global personlist
    self.name = name
    self.coordinates = coordinates
    self.people = []
  def refresh(self):
    global personlist
    for person in personlist:
      if person.location == self.coordinates:
        self.people.append(person)