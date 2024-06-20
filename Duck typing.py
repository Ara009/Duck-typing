#concept where the class of an object is less important than the method/attributes
#class type is not checked if minimum methods/attributes are present

class duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quaking")


class chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")
class person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")
duck = duck()
chicken = chicken()
person = person()

person.catch(chicken)