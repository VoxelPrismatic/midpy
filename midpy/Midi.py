def byte(b, n = 1):
    """
    Converts hex/int data into binary
    """
    if type(b) == int:
        return f"{b:b}".zfill(16 * n)
    elif type(b) == str:
        return f"{int(b, 16):b}".zfill(16 * n)
    raise TypeError("Invalid byte")

class MidiHeader:
    def __init__(self, length: int, fmt: int, n: int, division: int):
        self.length = length
        self.fmt = fmt
        self.n = n
        self.division = division
    def __str__(self):
        s = "MThd"
        s += byte(self.length, 4)
        s += byte(self.fmt, 2)
        s += byte(self.n, 2)
        s += byte(self.division, 2)
        return s

class MidiTrackEvent:
    def __init__(self):
        pass

class MidiMetaEvent:
    def __init__(self, type, data):
        self.type = type
        self.length = len(data)
        self.data = data
    def __str__(self):
        return byte(0xFF) + byte(self.type)

class MidiTrack:
    def __init__(self, length, events):
        self.length = length
        self.events = []
        if type(events) == MidiTrackEvent:
            self.events.append(events)
        elif type(events) in [list, tuple]:
            for event in events:
                if type(event) == MidiTrackEvent:
                    self.events.append(event)

    def __str__(self):
        s = "MTrk"
        s += hex(self.length)[2:].zfill(8)
        for event in events:
            s += str(event)
        return s
    def add_events(other):
        if type(other) == self.__class__:
            self.events += other.events
        elif type(other) in [list, tuple]:
            for event in other:
                if type(event) == MidiTrackEvent:
                    self.events.append(event)
        elif type(other) == MidiTrackEvent:
            self.events.append(event)
    def __getitem__(self, index):
        return self.events[index]
    def __setitem__(self, index, value):
        if type(value) == MidiTrackEvent:
            self.events[index] = value
    def __delitem__(self, index):
        del self.events[index]
    def __lshift__(self, value):
        self.add_events(value)
            
class Midi:
    def __init__(self):
        self.header = 
