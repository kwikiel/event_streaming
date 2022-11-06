# 1) Stwórz klasę Tank (zbiornik).
# Zbiornik posiada następujące atrybuty: nazwę oraz pojemność.
# Należy stworzyć następujące operacje:
# pour_water(volume) - ale w zbiorniku nie może być więcej wody niż pojemność
# pour_out_water(volume) - ale nie można odlać więcej wody niż jest dostępne w zbiorniku
# transfer_water(from, volume) - przelewa wodę ze zbiornika "from" do naszego (pod warunkiem, że przelewanie jest możliwe)
# Dodatkowo stworzyć metody, które pozwalają:
# Znaleźć zbiornik, w którym jest najwięcej wody
# Znaleźć zbiornik, który jest najbardziej zapełniony
# Znaleźć wszystkie puste zbiorniki m
# 2) Każda operacja na zbiorniku jest rejestrowana.
# Dla każdej operacji pamiętamy: datę i czas jej wykonania, jej nazwę, zbiornik, na którym była ona wykonana oraz ilość wody, jaka była brana pod uwagę oraz to, czy operacja się powiodła czy nie.
#
# Należy zaimplementować taką funkcjonalność oraz dodatkowo stworzyć metody, które:
# Pozwalają znaleźć zbiornik, na którym było najwięcej operacji zakończonych niepowodzeniem
# Pozwalają znaleźć zbiornik, w którym było najwięcej operacji danego typu (typ podajemy jako argument metody)
#
# 3) To co zaimplementowaliśmy powyżej to demo "Event Sourcingu" - na czym ono polega?
# Zaimplementuj metodę check_state(volumeName), która pozwoli określić, czy stan wody jest spójny z tym, co mamy na liście historii operacja dla danego zbiornika.
import datetime
import enum

from pydantic import BaseModel
from typing import List, Optional
from typing import Dict

class EventState(enum.Enum):
    PENDING = 1
    SUCCESS = 2
    FAILED = 3

class Tank:
    def __init__(self, uid, capacity):
        self.uid = uid
        self.capacity = capacity


class Event:
    def __init__(self, source, destination, volume):
        self.source = source
        self.destination = destination
        self.volume = volume
        self.state = EventState.PENDING
        self.execution_time = None


class EventStream:
    def __init__(self):
        self.events = []
        self.state = State(tank_list=)

    def add_event(self, event):
        self.events.append(event)

    def process_events(self):
        # Make list of tanks UID based on events
        tank_set =
        for event in self.events:



class State:
    class TankState:
        def __init__(self, capacity):
            self.capacity = capacity
            self.volume = 0

    def __init__(self, tank_list):
        self.tank_states = {tank.uid: self.TankState(tank.capacity) for tank in tank_list}



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
