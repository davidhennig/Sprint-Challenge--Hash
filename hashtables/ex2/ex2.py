#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    dic = {}
    storage = "NONE"
    for tix in tickets:   
        if tix.source not in dic:
            dic[tix.source] = tix.destination
    while len(route) < length:
        for tix in dic:
            if tix == storage and dic[tix] not in route:
                route.append(dic[tix])
                storage = dic[tix]
            else:
                continue
    return route

