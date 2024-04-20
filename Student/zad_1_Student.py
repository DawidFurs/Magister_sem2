class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if sum(self.marks)/len(self.marks) > 50:
            print(True)
        else:
            print(False)


Dawid = Student("Dawid", [30, 40, 50, 50, 80, 90, 95])
Dagmara = Student("Dagmara", [30, 40, 45, 45, 50, 50, 50])

# Dawid.is_passed()
# Dagmara.is_passed()

