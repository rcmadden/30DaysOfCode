class Car():
    maxSpeed = 100
    minSpeed = 0
    weight = 4079
    isTheCarOn = True
    nameOfCar = "Lucy"
    maxFuel = 16
    currentFuel = 8
    mpg = 26.4
    numberOfPeopleInCar = 1

    # Python Constructor?
    def Car(customMaxSpeed, customWeight, customIsTheCarOn):
        maxSpeed = customMaxSpeed
        weight = customWeight
        isTheCarOn = customIsTheCarOn

    def printVariables(self):
        print("This is the maxspeed" + maxSpeed)
        print(minSpeed)
        print(weight)
        print(isTheCarOn)
        print(condition)
        print(nameOfCar)

    def upgradeMinSpeed(self):
        minSpeed = maxSpeed
        maxSpeed = maxSpeed + 1

    def getIn():
        # numberOfPeopleInCar = numberOfPeopleInCar + 1
        numberOfPeopleInCar +=

    def getOut():
        numberOfPeopleInCar -=

    def howManyMilesTillOutOfGas():
        return currentFuel * mpg

    def maxMilesPerFillU():
        return maxFuel * mpg

#inside main

birthdayPresent = Car(500, 5000.545, True)
birthdayPresent.printVariables()
christmasPresent = Car(550, 2000, False)
christmasPresent.printVariables()
