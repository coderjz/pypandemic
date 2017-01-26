#We want a single reference for the mediator to be used in all classes.
#For now just make it a static class variable
from mediator import Mediator

class MediatorResource:
    Mediator = Mediator()
