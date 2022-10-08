from person import Person
from team import Team


if __name__ == '__main__':
    kube = Person("Kube", "Engineer")
    polo = Person("Polo", "QA")
    john = Person("John", "Manager")

    teamA = Team("A")
    teamA.add(kube)
    teamA.add(polo)
    teamA.add(john)
    print(teamA.budget())
    print(teamA.member())

    kube.getPromote()

    print(teamA.budget())
    print(teamA.member())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
