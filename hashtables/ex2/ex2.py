#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    cache = {}
    for i in range(length):
        cache[tickets[i].source] = tickets[i].destination

    route.append(cache["NONE"])
    while len(route) < length:
        if route[-1] in cache:
            route.append(cache[route[-1]])

    return route
