# %r, %d, %s vs. .format syntax?

my_name = 'James Bond'
my_age = 29
my_height = 72
my_weight = 180
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about{}.".format(my_name))
print("He's {} inches tall.".format(my_height))
print("He's {} pounds heavy.".format(my_weight))
print("Actually that's not too heavy".format(my_eyes))
print("He's got {} eyes an {} hair".format(my_eyes,my_hair))
print("His teeth are usually {} depending on the coffee".format(my_teeth))
print("If I add {}, {}, and {} I get {}".format(my_age, my_height, my_weight, my_age + my_age + my_height + my_weight))

w = "world"
print("hello {}".format(w))
