class Vehicle():
    type = "Truck"
    use = "undefined"
    wheels = 0
    country_of_origin = "USA"

    def get_origin(self):
        return self.country_of_origin
    def get_use(self):
        return self.use


class Class_A(Vehicle):
    type = "Car"
    usage = "personal"
    wheels = 4
    emissions = "required"
    fuel = "gasoline"
    def get_attrs(self):
        print(self.type)
        print(self.usage)
        print(self.fuel)


class Class_C(Vehicle):
    type = "passenger"
    usage = "commercial"
    wheels = 8
    fuel = "Electric"
    def get_attributes(self, test):
        print(test)
        return self.fuel
# class Media(object):
#     def __init__(self):
#         title = "TBD"
#         year = 1900
#         genre = "action"
#         how_many = "Movie or Series"
#         studio = "Disney"
#
# # inheritance
# class Movie(Media):
#     sequel = bool
#
#     def get_title(self):
#         return self.title
#
# class Series(Media):
#     seasons = 7
#     first_season = 1900
#     last_season = 2016

# Mr_Robot = Media()

# Mr_Robot.Movie(title="Mr Robot")

