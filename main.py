class Men:
    gender = "male"
    species = "human"
    age = 30,25,45

    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

man1 = Men("Sasha", 30, "police-man")
man2 = Men("Misha", 25, "Barmen")
man3 = Men("Artem", 45, "teacher")

class Women:
    gender = "female"
    species = "human"
    age = 0

    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

woman1 = Women("Emily", 28, "lawyer")
woman2 = Women("Sophia", 35, "scientist")
woman3 = Women("Olivia", 40, "artist")