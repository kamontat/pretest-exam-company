class Person:
    def __init__(self, name, role):
        self.name = name

        self.roleTitle = ""
        self.role = role

        if role == "Manager":
            self.salary = 50000.0
        elif role == "Engineer":
            self.salary = 30000.0
        elif role == "QA":
            self.salary = 15000.0
        else:
            self.salary = 0.0

    def getPromote(self):
        self.roleTitle = " Senior"
        self.salary += (self.salary * 0.15)
