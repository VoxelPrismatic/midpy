class MidiHeader:
    def __init__(self, length: int, fmt: int, n: int, division: int):
        self.length = length
        self.fmt = fmt
        self.n = n
        self.division = division
    def __str__(self):
        s = "MThd"
        s += hex(self.length)[2:].zfill(8)
        s += hex(self.fmt)[2:].zfill(4)
        s += hex(self.n)[2:].zfill(4)
        s += hex(self.division)[2:].zfill(4)
        return s

class MidiEvent:
    def __init__(self):
        pass
        

class MidiTrack:
    def __init__(self, length, events):
        self.length = length
        self.events = []
        if type(events) == MidiEvent:
            self.events.append(events)
        elif type(events) in [list, tuple]:
            for event in events:
                if type(event) == MidiEvent:
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
                if type(event) == MidiEvent:
                    self.events.append(event)
        elif type(other) == MidiEvent:
            self.events.append(event)
    def __getitem__(self, index):
        return self.events[index]
    def __setitem__(self, index, value):
        if type(value) == MidiEvent:
            self.events[index] = value
    def __delitem__(self, index):
        del self.events[index]
    def __lshift__(self, value):
        self.add_events(value)
            
class Midi:
    def __init__(self):
        self.header = 
