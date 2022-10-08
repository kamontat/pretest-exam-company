from person import Person


class Team:
    def __init__(self, name):
        self.name = name
        self.person: list[Person] = []

    def add(self, person: Person):
        self.person.append(person)

    def budget(self):
        money = 0
        for p in self.person:
            money += p.salary
        return money

    def member(self):
        output = "Team " + self.name + "\n"
        for p in self.person:
            output += ("- " + p.roleTitle + " " + p.role + "\n")
        return output
