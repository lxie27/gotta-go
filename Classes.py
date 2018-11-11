from sets import Set

# A Drop is the port-a-potty
# Drops have:
#   deployed - initiliazed to False
#   posn - current position of the Drop
#   locked - initialized to True
class drop:
    deployed = None
    locked = None
    posn = 0

    def __init__(self, posn):
        self.deployed = False
        self.locked = True
        self.posn = posn

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def deploy(self, posn):
        self.deployed = True
        self.posn = posn
        

# A Transport is the vehicle
# Transporters have:
#   slots - initialized to 2
#       slots are represented as an array of booleans, where True indicates an open slot
#   posn - current position of the transporter
#       TODO not sure how posns are represented
class transporter:
    slots = []
    posn = 0

    def __init__(self, posn):
        self.slots = [True, True]
        self.posn = posn

    def addSlot(self):
        self.slots.append[True]

    def updatePosn(self, posn):
        self.posn = posn

# A Network is the set of all nodes
# Networks have:
# couriers - a dictionary (hashtable) initialized to no nodes
class network:
    couriers = {}
    size = 0
    
    def __init__(self):
    self.size = 0

    def addNode(self, trnsp): 
        self.couriers.add(self.size + 1, trnsp)
        self.size++

    def getNode(self, key):
        return self.couriers[key]
