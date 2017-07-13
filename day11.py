import argparse
import itertools
import logging
logger = logging.getLogger(__name__)

# Goal: get all Generators and Microchips to Floor 4 - how many steps?
#
# Preconditions:
#
#  - Elevator starts on the first Floor.
#
# Rules:
#
#  - A paired Microchip can share a Floor with any other Generator (paired or non-paired).
#  - A non-paired Microchip cannot share a Floor with any other Generator except its own.
#  - The Elevator can only carry up to two Microchips or Generators, or one of both.
#  - The Elevator must carry at least one Microchip or Generator to function.
#  - The Elevator can only move one floor at a time.


# Use depth-first search to find possible solutions.
# Keep track of states in current partial solution to avoid loops.
# Keep track of step length of best solution found so far.
# Backtrack any partial solutions that exceed best solution.
# Backtrack any loops.
# Backtrack any solutions.


class Microchip(object):
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "M." + self.type


class Generator(object):
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "G." + self.type


class Floor(object):
    def __init__(self):
        self.generators = []
        self.microchips = []

    def __str__(self):
        return " ".join([str(x) for x in self.generators] + [str(x) for x in self.microchips])

    def load(self, generators, microchips):
        self.generators = generators
        self.microchips = microchips

    def empty(self):
        return not self.microchips and not self.generators

    def valid(self):
        # if there are any generators on this floor, then all microchips must be paired
        if self.generators:
            for microchip in self.microchips:
                if microchip not in self.generators:
                    return False

    def get_items(self):
        return self.generators + self.microchips


def find_generators(words):
    generators = []
    for i, word in enumerate(words):
        if word.startswith("generator"):
            generators.append(Generator(words[i - 1].upper()[:3]))
    return generators


def find_microchips(words):
    microchips = []
    for i, word in enumerate(words):
        if word.startswith("microchip"):
            microchips.append(Microchip(words[i - 1].split('-')[0].upper()[:3]))
    return microchips


def load_floor(line):
    floor_map = {"first": 0,
                 "second": 1,
                 "third": 2,
                 "fourth": 3}
    words = line.split()
    floor_index = floor_map[words[1]]
    generators = find_generators(words[4:])
    microchips = find_microchips(words[4:])
    return floor_index, generators, microchips


class State(object):
    def __init__(self):
        self.floors = [Floor(), Floor(), Floor(), Floor()]
        self.num_floors = len(self.floors)
        self.top_floor = self.num_floors - 1
        self.elevator = 0

    def __str__(self):
        result = ""
        for i, floor in enumerate(self.floors[::-1]):
            result += f"F{self.num_floors - i} {'E' if self.elevator == self.num_floors - i - 1 else ' '} {floor}\n"
        return result

    def is_complete(self):
        # elevator is at the top and all floors except the top floor are empty
        return self.elevator == self.top_floor \
            and all([x.empty() for x in self.floors[:-1]]) \
            and not self.floors[-1].empty()

    def is_valid(self):
        return all([x.valid() for x in self.floors])

    def show(self):
        print(str(self))

    def load(self, line):
        floor_index, generators, microchips = load_floor(line)
        self.floors[floor_index].load(generators, microchips)

    def get_items_from_elevator_floor(self):
        return self.floors[self.elevator].get_items()


# From a given state, iterate through each of the combination of one or two items on the floor that the elevator
# is on, and consider the result from taking this combination down, or up.
# If the resultant state is invalid, backtrack.
# If the resultant state is valid, repeat.
# If the resultant state is complete, record length and backtrack.
# If the resultant state is a repeat, backtrack.

def iterate(states):
    head = states[-1]
    logger.info("head is \n{0}".format(head))
    floor_items = head.get_items_from_elevator_floor()
    elevator_candidates = floor_items + list(itertools.combinations(floor_items, 2))

    # for each payload
    for payload in elevator_candidates:

        if head.elevator < head.top_floor:
            # try a move up
            new_state = move_up(head, payload)
            if new_state.is_valid():
                logger.info("move up with {0}".format(payload))
                iterate(states + new_state)

        if head.elevator > 0:
            # try a move down
            new_state = move_down(head, payload)
            if new_state.is_valid():
                logger.info("move down with {0}".format(payload))
                iterate(states + new_state)


# TODO: treat states as immutable
def move_up(state, payload):
    # remove payload from current floor

    # move elevator up one level

    # add payload to new floor
    return state


def move_down(state, payload):
    return state


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)

    s = State()

    for line in args.file.readlines():
        s.load(line)

    solution = iterate((s,))
    print(solution)
#    s.show()

#    print(s.is_complete())

if __name__ == "__main__":
    main()
