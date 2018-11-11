import Classes

def find_best(user_posn, network):
    if network.isEmpty():
        return "No available couriers in the network. Add some to the network and try again."
    else:
        count = 1
        best = network.getNode(1)

        #this is O(n) currently
        for drop in network:
            while count != network.size:
                count += 1
                dis = best.posn - user.posn
                try:
                    odis = network.getNode(count).posn - user.posn
                    if (odis < dis):
                        best = odis
                except:
                    print("Couldn't get distance from new courier")
        
        return best
    

