# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

class Cat:
    species = 'mamal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('jojo', 10)
cat2 = Cat('koko', 15)
cat3 = Cat('bobo', 9)


def oldest_cat(*ages):
    age_max=0
    for item in ages:


        if item > age_max:
            age_max = item
    return age_max

print(oldest_cat(cat1.age,cat2.age,cat3.age))

