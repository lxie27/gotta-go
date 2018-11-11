import Classes

#find_closest mask for a network
def find_best(user_posn, network):
    if network.isEmpty():
        return "No available couriers in the network. Add some to the network and try again."
    else:
        posns = []
        for n in nrange(0, len(network.couriers)):
            posns[n] = network.couriers[n]

        return find_closest(user_posn, posns)
    

