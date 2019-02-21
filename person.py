personlist = []
from room import wall_list

class Person(object):
    def __init__(self, name):
        global personlist
        self.name = name
        self.location = None
        personlist.append(self)


class Player(Person):
    def __init__(self, name):
        super().__init__(name)

    def move(self, cmd):
        wall = False
        frontdirs = [
            "forward",
            "ahead",
        ]
        backdirs = ["back", "backwards"]
        leftdirs = ["left"]
        rightdirs = ["right"]
        if self.location:
            if cmd[1] in frontdirs:
                for wall in wall_list:
                    if self.location[1] + 1 == wall.location[1]:
                        print("you ran into a wall")
                        wall = True
                        pass
                if not wall:
                    self.location[1]+=1
                   
            if cmd[1] in backdirs:
                for wall in wall_list:
                    if self.location[1] - 1 == wall.location[1]:
                        print("you ran into a wall")
                        wall = True
                        pass
                if not wall:
                    self.location[1]-=1

              
            if cmd[1] in leftdirs:
                for wall in wall_list:
                    if self.location[0] + 1 == wall.location[0]:
                        print("you ran into a wall")
                        wall = True
                        pass
                if not wall:
                    self.location[0] -= 1
            if cmd[1] in rightdirs:
                 for wall in wall_list:
                      if self.location[0]+1 == wall.location[0]:
                        print ("you ran into a wall")
                        wall = True
                        pass
                 if not wall:
                    self.location[0]+=1


class NPC(Person):
    def __init__(self, name):
        super().__init__(name)
        self.lines = {}
        self.isteacher = None
        self.subject = None
