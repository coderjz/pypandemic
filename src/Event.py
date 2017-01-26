from mediator import Event


class CubesUnavailableEvent(Event):
    event_name = 'cubes_unavaiable'


class OutbreakEvent(Event):
    event_name = 'outbreak'


class CubesTooManyEvent(Event):
    event_name = 'cubes_too_many'
    def __init__(self):
        self.city = None
