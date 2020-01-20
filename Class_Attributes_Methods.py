# define a class with instanse attributes
class Teacher:
    def __init__(self, name, surname, age, sex, salary, academic_rank):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.salary = salary
        self.academic_rank = academic_rank

    # methods
    def givesalary(self):
        print(self.name + " " + "earns " + str(self.salary) + " manet per month")


# instanse
tech1 = Teacher("Valodya", "Hakobyan", 67, "male", 1000, "professor")
print(tech1.name)
tech1.givesalary()
