import math

# A Drop is the port-a-potty
# Drops have:
#   deployed - initiliazed to False
#   posn - current position of the Drop
#   locked - initialized to True
#   inuse - initialized to False

class drop:
    deployed = None
    locked = None
    in_use = None
    posn = {}

    def __init__(self):
        self.deployed = False
        self.locked = True
        self.in_use = False
        self.posn.update(lat=0)
        self.posn.update(lng=0)

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def use(self):
        self.in_use = True

    def end_use(self):
        self.in_use = False

    def recover(self):
        self.deployed = False
        self.posn.update(lat=0)
        self.posn.update(lng=0)

    def deploy(self, posn):
        self.deployed = True
        self.posn['lat'] = posn['lat']
        self.posn['lng'] = posn['lng']
        

# A Transport is the vehicle
# Transporters have:
#   slots - initialized to 2
#       slots are represented as an array of booleans, where True indicates an open slot
#   posn - current position of the transporter
#       TODO not sure how posns are represented
class transporter:
    slots = []
    posn = {}

    def __init__(self, node1, node2):
        self.slots = [node1, node2]
        self.posn.update(lat=0)
        self.posn.update(lng=0)

    def addDrop(self, node):
        self.slots.append(node)
        node.recover()

    def dropDrop(self, node):
        self.slots.remove(node) #this might need a try
        node.deploy(posn)  

    def updatePosn(self, posn):
        self.posn['lat'] = posn['lat']
        self.posn['lng'] = posn['lng']


    def getNodes(self):
        return self.slots

# A Network is the set of all nodes
# Networks have:
# couriers - a dictionary (hashtable) initialized to no nodes
class network:
    couriers = []
    size = 0

    def __init__(self):
        self.size = 0

    def addNode(self, trnsp): 
        self.couriers.append(trnsp)
        self.size += 1

    def getNode(self, key):
        return self.couriers[key]

    def retrieve(self, drop):
        avail = []

        for transp in self.couriers:
            if transp.slots < 2:
                avail.append(transp)
        
        posns = []
        for i in irange(0, len(avail)):
            posns[i] = avail[i].posn
        
        best = find_closest(drop.posn, posns)

        for x in xrange(0, len(avail)):
            if avail[x] == best:
                return avail[x]

        

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

#B and A are posns (hashtable of lat and lng)
def distance(b, a):
    return math.sqrt((math.pow(b['lng'] - a['lng']), 2) + (math.pow(b['lat'] - a['lat']), 2))

def find_closest(target, posns):
    if (posns < 1):
        return "Posns cannot be 0"
    else:
        best = posns[0]
        for c in crange(1, len(posns)):
            if distance(best, target) < distance(posns[c], target):
                best = posns[c]

    return best


        
