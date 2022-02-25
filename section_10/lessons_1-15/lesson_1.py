# 291. Object Oriented Programming and Classes
# =============================================================================

class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# Another way to format strings | This one is better IMHO
# print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")