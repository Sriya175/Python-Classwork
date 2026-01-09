class Vehicle:

    def __init__(self, max_speed, milage):

        self.max_speed = max_speed
        self.milage = milage

model1X = Vehicle(240,18)

print("Model Max speed:", model1X.max_speed)
print("Model Milage:", model1X.milage)
