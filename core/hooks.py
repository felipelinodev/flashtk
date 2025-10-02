
class useState:
    def __init__(self, initial):
        self.initial = initial
        self.state = initial
        self.prev = self.state

    def set_state(self, value):
        self.prev = self.state
        self.state = value


_effects = {}

def useEffect(key, callback, dependence):
    global _effects

    prev = _effects.get(key) #None

    if prev != dependence:
        callback()
        _effects[key] = dependence