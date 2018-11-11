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

    def __init__(self):
        self.deployed = False
        self.locked = True
        self.posn = 0

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def recover(self):
        self.deployed = False
        self.posn = 0

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

    def __init__(self, node1, node2):
        self.slots = [node1, node2]
        self.posn = posn

    def addDrop(self, node):
        self.slots.append(node)
        node.recover()

    def dropDrop(self, node):
        self.slots.remove(node) #this might need a try
        node.deploy(posn)  

    def updatePosn(self, posn):
        self.posn = posn

    def getNodes(self):
        return self.slots

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
        for node in trnsp:
            self.courses.nodes.add(node)
        self.size += 1

    def getNode(self, key):
        return self.couriers[key]

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
