class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def make_friend(self, other_person):
        self.friends.append(other_person)
        other_person.friends.append(self)

    def display_friends(self):
        print(f"{self.name}'s friends:")
        for friend in self.friends:
            print(f" - {friend.name}")


class Community:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def display_members(self):
        print(f"Члени {self.name}:")
        for member in self.members:
            print(f" - {member.name}")


person1 = Person("Alica", 25)
person2 = Person("Sasha", 30)
person3 = Person("Karina", 28)

community = Community("Programming Enthusiasts")

community.add_member(person1)
community.add_member(person2)
community.add_member(person3)

person1.make_friend(person2)
person2.make_friend(person3)

community.display_members()
person1.display_friends()
person2.display_friends()
person3.display_friends()
