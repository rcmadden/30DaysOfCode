class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        if initialAge < 0:
            self.initialAge = 0
            print("Age is not valid, setting age to 0")
        return self.initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        pass
    def yearPasses(self):
        # Increment the age of the person in here
        pass


Cameron = Person(14)
Cameron.initialAge

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")