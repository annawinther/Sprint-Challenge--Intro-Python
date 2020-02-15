# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class
class Vehicle:
    pass

# Vehicle has a Flight Vehicle and Startship
class FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

# sub classes
class GroundVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

# Aggregation
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass